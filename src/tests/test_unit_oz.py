import unittest
from oxrse_unit_conv.units import oz, lb, kg


class TestOunce(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(oz.si_unit.matches(kg))

    def test_basic_conversion(self):
        self.assertEqual(oz.to_si(1), 0.028349523125)
        self.assertAlmostEqual(oz.to_unit(10, oz), 10, 8)

    def test_from_si(self):
        self.assertAlmostEqual(kg.to_unit(0.028349523125, oz), 1, 8)

    def test_to_pound(self):
        self.assertAlmostEqual(oz.to_unit(16, lb), 1, 6)


if __name__ == '__main__':
    unittest.main()
