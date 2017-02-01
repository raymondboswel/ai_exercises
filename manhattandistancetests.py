import unittest
import manhattandistance

class TestStringMethods(unittest.TestCase):

    def test_distance(self):
        distance = manhattandistance.calculate([[7,2,4],[5,0,6],[8,3,1]])
        self.assertEqual(18, distance)

if __name__ == '__main__':
    unittest.main()