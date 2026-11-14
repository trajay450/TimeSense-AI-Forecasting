import unittest, tempfile
import main
class TestCore(unittest.TestCase):
    def test_import(self):
        self.assertTrue(hasattr(main,"__name__"))
    def test_features(self):
        self.assertEqual(main.supervised(main.data(40))[0].shape,(16,24))
    def test_forecast(self):
        with tempfile.TemporaryDirectory() as d:
            r=main.evaluate(d)
            self.assertGreater(r['test_points'],0)
            self.assertGreaterEqual(r['model_mae'],0)

if __name__=="__main__":unittest.main()
