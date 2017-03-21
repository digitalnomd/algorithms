import unittest
import dynamic_programming as dp
import topcoder as tc

class TestLcs(unittest.TestCase):

    def test_lcs(self):
        self.assertEqual(dp.lcs("AGGTAB", "GXTXAYB"), "GTAB")
        self.assertEqual(dp.lcs("ACSBF", "FCSBZ"), "CSB")
        self.assertEqual(dp.lcs("ACSBF", ""), "")
        self.assertEqual(dp.lcs("", "FCSBZ"), "")

    def test_people_circle(self):
        self.assertEqual(tc.people_circle(25, 25, 1000), "MMMMMFFFFFFMFMFMMMFFMFFFFFFFFFMMMMMMMFFMFMMMFMFMMF")

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()
