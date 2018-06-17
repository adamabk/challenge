import unittest
from lib.bot import PizzaBot


class Test_PizzaBot(unittest.TestCase):
    def test_deliver_pizza(self):
        exp_res = 'ENNNDEEEND'
        test_res = PizzaBot(zone=(5, 5), drops=[(1, 3), (4, 4)]).deliver_pizza()
        self.assertEqual(exp_res, test_res)

    def test_error_deliver_pizza(self):
        bot = PizzaBot(zone=(4, 4), drops=[(5, 4)])
        self.assertRaises(AssertionError, bot.deliver_pizza)

    def test_no_movement(self):
        exp_res = 'DENDDD'
        bot = PizzaBot(zone=(4, 4), drops=[(0, 0), (1, 1), (1, 1), (1, 1)])
        self.assertEqual(exp_res, bot.deliver_pizza())

    def test_solution(self):
        exp_res = 'DENNNDEEENDSSDDWWWWSDEEENDWNDEESSD'
        bot = PizzaBot(
                zone=(5, 5),
                drops=[(0, 0), (1, 3), (4, 4), (4, 2), (4, 2), (0, 1), (3, 2), (2, 3), (4, 1)])
        self.assertEqual(exp_res, bot.deliver_pizza())


if __name__ == '__main__':
    unittest.main()
