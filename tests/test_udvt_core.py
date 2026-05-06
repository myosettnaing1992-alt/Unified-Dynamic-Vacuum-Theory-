import unittest
from udvt_myo_limit import MyoLimitCheck
from core import UDVT_Engine

class TestUDVTCore(unittest.TestCase):
    def setUp(self):
        self.engine = UDVT_Engine(beta=0.0038)
        self.limit = MyoLimitCheck()

    def test_beta_bound(self):
        """Ensure beta does not exceed the Margolus-Levitin bound"""
        self.assertLessEqual(self.engine.beta, 0.01, "Beta exceeds safety limit!")

    def test_vsl_logic(self):
        """Check if light speed scales correctly at z=1000"""
        a_rec = 1.0 / (1.0 + 1000)
        c_factor = self.engine.vsl_factor(a_rec)
        self.assertGreater(c_factor, 1.0, "VSL should be higher in the early universe")

if __name__ == "__main__":
    unittest.main()
  
