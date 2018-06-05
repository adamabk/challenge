import re
from ast import literal_eval
from argparse import ArgumentParser


class Instruction(object):
    zone_pattern = r'([0-9])x([0-9])'
    coordinate_pattern = r'(\([0-9]\,\s[0-9]\))'

    def __init__(self):
        self.command = self._parser_helper()
        self.zone = self._zone_setter(self.command)
        self.drops = self._drop_setter(self.command)

    def _parser_helper(self):
        parser = ArgumentParser()
        parser.add_argument("command", type=str, help="The Delivery Instruction Please")
        args = parser.parse_args()
        return args.command

    def _zone_setter(self, command: str):
        zn = re.match(self.zone_pattern, command)
        if zn.group(1) and zn.group(2):
            return int(zn.group(1)), int(zn.group(2))
        else:
            raise Exception

    def _drop_setter(self, command: str):
        ls = re.findall(self.coordinate_pattern, command)
        if not ls:
            raise Exception
        else:
            return list(map(literal_eval, ls))
