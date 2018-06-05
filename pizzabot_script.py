import re
import sys
import argparse
from ast import literal_eval


parser = argparse.ArgumentParser()
parser.add_argument("delivery_command", type=str, help="The Dimension of the Delivery")
args = parser.parse_args()

coordinate_pattern = r'(\([0-9]\,\s[0-9]\))'
command_ls = re.findall(coordinate_pattern, args.delivery_command)
if not command_ls:
    sys.exit("Please provide delivery direction in '(#, #)' format")

command_ls = list(map(literal_eval, command_ls))

dimension_pattern = r'([0-9])x([0-9])'
dimension_groups = re.match(dimension_pattern, args.delivery_command)

# Run Time dimension checking
if dimension_groups:
    horizontal_dimension = int(dimension_groups.group(1))
    vertical_dimension = int(dimension_groups.group(2))
else:
    sys.exit("Please provide delivery dimension in '<Horizontal>x<Vertical>'")

# Coordinate Movements
x_coord, y_coord = (0, 0)
movement = list()
for val in command_ls:
    x_move, y_move = val
    assert x_move <= horizontal_dimension
    assert y_move <= vertical_dimension
    horizontal_movement = x_move - x_coord
    if horizontal_movement > 0:
        movement.append('E'*horizontal_movement)
    elif horizontal_movement < 0:
        movement.append('W'*abs(horizontal_movement))
    else:
        pass
    vertical_movement = y_move - y_coord
    if vertical_movement > 0:
        movement.append('N'*vertical_movement)
    elif vertical_movement < 0:
        movement.append('S'*abs(vertical_movement))
    else:
        pass
    movement.append('D')
    x_coord, y_coord = x_move, y_move

print(''.join(movement))
