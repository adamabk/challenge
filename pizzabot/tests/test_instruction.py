import unittest
from unittest import mock
from lib.instruction import Instruction


class Test_Instruction(unittest.TestCase):
    def mock_arg_parser(self):
        return '5x5 (1, 0) (0, 1) (0, 1)'

    def fail_mock_dimension(self):
        return '6s6'

    def fail_mock_directions(self):
        return '5x5 4,3'

    @mock.patch.object(Instruction, "_parser_helper", mock_arg_parser)
    def test_zone_setter(self):
        exp_res = (5, 5)
        self.assertEqual(exp_res, Instruction().zone)

    @mock.patch.object(Instruction, "_parser_helper", mock_arg_parser)
    def test_drop_setter(self):
        exp_res = [(1, 0), (0, 1), (0, 1)]
        self.assertEqual(exp_res, Instruction().drops)

    @mock.patch.object(Instruction, "_parser_helper", mock_arg_parser)
    def test_fail_zone(self):
        exp = Instruction()
        self.assertRaises(Exception, exp.zone)

    @mock.patch.object(Instruction, "_parser_helper", mock_arg_parser)
    def test_fail_directions(self):
        exp = Instruction()
        self.assertRaises(Exception, exp.drops)


if __name__ == '__main__':
    unittest.main()
