import unittest
import puzzlesolver

class TestStringMethods(unittest.TestCase):

    def test_swap_left(self):
        initial = [[1,2,5],[3,4,0],[6,7,8]]
        zero_index = puzzlesolver.find_zero_index(initial)
        print(zero_index)
        successor = puzzlesolver.swap_left(zero_index, initial)
        self.assertListEqual([3, 0, 4], successor[1])

    def test_swap_up(self):
        initial = [[1,2,5],[3,4,0],[6,7,8]]
        zero_index = puzzlesolver.find_zero_index(initial)
        print(zero_index)
        successor = puzzlesolver.swap_up(zero_index, initial)
        self.assertListEqual([1,2,0], successor[0])

    def test_swap_down(self):
        initial = [[1,2,5],[3,4,0],[6,7,8]]
        zero_index = puzzlesolver.find_zero_index(initial)
        print(zero_index)
        successor = puzzlesolver.swap_down(zero_index, initial)
        self.assertListEqual([6,7,0], successor[2])

    def test_swap_down(self):
        initial = [[1,2,5],[3,0,4],[6,7,8]]
        zero_index = puzzlesolver.find_zero_index(initial)
        print(zero_index)
        successor = puzzlesolver.swap_right(zero_index, initial)
        self.assertListEqual([3,4,0], successor[1])

    def test_generate_legal_actions_1(self):
        state = [[0,2,5],[3,4,1],[6,7,8]]
        actions = puzzlesolver.generate_legal_actions(state)
        self.assertListEqual(["swap_down", "swap_right"], actions)

    def test_generate_legal_actions_2(self):
        state = [[1,0,5],[3,4,1],[6,7,8]]
        actions = puzzlesolver.generate_legal_actions(state)
        self.assertListEqual(["swap_down", "swap_left", "swap_right"], actions)

    def test_generate_legal_actions_3(self):
        state = [[1,5,0],[3,4,1],[6,7,8]]
        actions = puzzlesolver.generate_legal_actions(state)
        self.assertListEqual(["swap_down", "swap_left"], actions)

    def test_generate_legal_actions_4(self):
        state = [[1,5,3],[0,4,1],[6,7,8]]
        actions = puzzlesolver.generate_legal_actions(state)
        self.assertListEqual(["swap_up", "swap_down", "swap_right"], actions)

    def test_generate_legal_actions_5(self):
        state = [[1,5,3],[4,0,1],[6,7,8]]
        actions = puzzlesolver.generate_legal_actions(state)
        self.assertListEqual(["swap_up", "swap_down", "swap_left", "swap_right"], actions)

    def test_generate_legal_actions_6(self):
        state = [[1,5,3],[1,4,0],[6,7,8]]
        actions = puzzlesolver.generate_legal_actions(state)
        self.assertListEqual(["swap_up", "swap_down", "swap_left"], actions)

    def test_generate_legal_actions_7(self):
        state = [[1,5,3],[6,4,1],[0,7,8]]
        actions = puzzlesolver.generate_legal_actions(state)
        self.assertListEqual(["swap_up", "swap_right"], actions)

    def test_generate_legal_actions_8(self):
        state = [[1,5,3],[4,7,1],[6,0,8]]
        actions = puzzlesolver.generate_legal_actions(state)
        self.assertListEqual(["swap_up", "swap_left", "swap_right"], actions)

    def test_generate_legal_actions_9(self):
        state = [[1,5,3],[2,4,1],[6,8,0]]
        actions = puzzlesolver.generate_legal_actions(state)
        self.assertListEqual(["swap_up", "swap_left"], actions)

    def test_is_goal_state(self):
        state = [[0,1,2],[3,4,5],[6,7,8]]
        is_goal_state = puzzlesolver.is_goal_state(state)
        self.assertEqual(True, is_goal_state)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()