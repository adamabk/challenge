import re
from argparse import ArgumentParser


class Instruction(object):

    def __init__(self):
        self.zone, self.drops = self._parser_helper()

    def _parser_helper(self):
        parser = ArgumentParser()
        parser.add_argument("command", type=str, help="The Delivery Instruction Please")
        args = parser.parse_args()

        command_pattern = r'((([\d+])x([\d+])(\s\([\d+]\,\s[\d+]\))*))'
        zn = re.match(command_pattern, args.command)
        assert zn is not None, "Please provide command in '#x# (#, #) (#, #)...' format"
        assert zn.group(5) is not None, "Please provide drop zone in '(#, #) ...' format"

        coordinate_pattern = r'\(([\d+])\,\s([\d+])\)'
        ls = re.findall(coordinate_pattern, zn.group(1))

        return tuple(map(int, zn.group(3, 4))), [tuple(map(int, num)) for num in ls]
