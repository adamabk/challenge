import sys
import unittest
from io import StringIO
from unittest import mock
from pizzabot import PizzaBot


class Test_PizzaBot(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def mock_arg_parser(self):
        return '5x5 (1, 0) (0, 1) (0, 1)'

    def incorrect_arg_parser(self):
        return '5x5 (6, 0)'

    @mock.patch.object(PizzaBot, "_parser_helper", mock_arg_parser)
    def test_deliver_pizza(self):
        PizzaBot().deliver_pizza()
        exp_res = sys.stdout.getvalue()
        self.assertEqual(exp_res, 'EDWNDD\n')

    @mock.patch.object(PizzaBot, "_parser_helper", incorrect_arg_parser)
    def test_error_deliver_pizza(self):
        bot = PizzaBot()
        self.assertRaises(AssertionError, bot.deliver_pizza)


if __name__ == '__main__':
    unittest.main()
