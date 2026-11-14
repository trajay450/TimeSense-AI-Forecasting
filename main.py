import json
from pathlib import Path
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,mean_squared_error

def data(n=600,seed=42):
    rng=np.random.default_rng(seed);t=np.arange(n);y=10+np.sin(t/12)*2+np.sin(t/45)+.003*t+rng.normal(0,.2,n);return y

def supervised(y,lag=24):return np.array([y[i-lag:i] for i in range(lag,len(y))]),y[lag:]

def evaluate(out='outputs'):
    y=data();X,target=supervised(y);cut=int(len(target)*.75);model=RandomForestRegressor(n_estimators=60,max_depth=9,random_state=42,n_jobs=1).fit(X[:cut],target[:cut]);pred=model.predict(X[cut:]);naive=X[cut:,-1]
    resid=np.abs(target[:cut]-model.predict(X[:cut]));radius=float(np.quantile(resid,.95))
    actual=target[cut:];anomaly=np.abs(actual-pred)>radius
    result={'test_points':len(actual),'model_mae':float(mean_absolute_error(actual,pred)),'naive_mae':float(mean_absolute_error(actual,naive)),'model_rmse':float(np.sqrt(mean_squared_error(actual,pred))),'interval_coverage':float(np.mean(np.abs(actual-pred)<=radius)),'anomaly_flags':int(anomaly.sum()),'interval_radius':radius}
    d=Path(out);d.mkdir(parents=True,exist_ok=True);(d/'metrics.json').write_text(json.dumps(result,indent=2));np.savetxt(d/'forecast.csv',np.column_stack([actual,pred,pred-radius,pred+radius]),delimiter=',',header='actual,pred,lower,upper',comments='');return result
if __name__=='__main__':print(json.dumps(evaluate(),indent=2))
