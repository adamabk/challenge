import unittest
from unittest import mock
from lib.instruction import Instruction
from argparse import ArgumentParser


class TestParser():
    def __init__(self, command=None):
        self.command = command
        pass

    def command(self):
        return self.command


class Test_Instruction(unittest.TestCase):
    def mock_arg_parser(self):
        return TestParser('5x5 (1, 0) (0, 1) (0, 1)')

    def fail_mock_dimension(self):
        return TestParser('6s6')

    def fail_mock_directions(self):
        return TestParser('5x5 4,3')

    def fail_mock_direction_standard(self):
        return TestParser('(4, 3) (3, 4) 5x5 (3, 5)')

    @mock.patch.object(ArgumentParser, "parse_args", mock_arg_parser)
    def test_zone_setter(self):
        exp_res = (5, 5)
        self.assertEqual(exp_res, Instruction().zone)

    @mock.patch.object(ArgumentParser, "parse_args", mock_arg_parser)
    def test_drop_setter(self):
        exp_res = [(1, 0), (0, 1), (0, 1)]
        self.assertEqual(exp_res, Instruction().drops)

    @mock.patch.object(ArgumentParser, "parse_args", fail_mock_dimension)
    def test_fail_zone(self):
        self.assertRaises(AssertionError, Instruction)

    @mock.patch.object(ArgumentParser, "parse_args", fail_mock_directions)
    def test_fail_directions(self):
        self.assertRaises(AssertionError, Instruction)

    @mock.patch.object(ArgumentParser, "parse_args", fail_mock_direction_standard)
    def test_fail_direction_standard(self):
        self.assertRaises(AssertionError, Instruction)


if __name__ == '__main__':
    unittest.main()
