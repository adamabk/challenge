import re
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("delivery_command", type=str, help="The Dimension of the Delivery")
args = parser.parse_args()

sep = re.compile(r'[\s\(\)\,]')
command_ls = sep.split(args.delivery_command)
command_ls = [val for val in command_ls if val != '']

dimension_val = command_ls[0]
del command_ls[0]
dimension_pattern = r'([0-9])x([0-9])'
dimension_groups = re.match(dimension_pattern, dimension_val)

# Run Time dimension checking
if dimension_groups:
    pass
else:
    sys.exit("Please provide delivery dimension in '<Horizontal>x<Vertical>'")

horizontal_dimension = int(dimension_groups.group(1))
vertical_dimension = int(dimension_groups.group(2))

command_ls = list(map(int, command_ls))

origin = [0, 0]
i = 0
movement = list()
for val in command_ls:
    i += 1
    if i % 2 == 1:
        assert val <= horizontal_dimension
        horizontal_movement = val - origin[0]
        for v in range(0, abs(horizontal_movement)):
            if horizontal_movement > 0:
                movement.append('E')
            elif horizontal_movement < 0:
                movement.append('W')
            else:
                pass
        origin[0] = val
    else:
        assert val <= vertical_dimension
        vertical_movement = val - origin[1]
        for v in range(0, abs(vertical_movement)):
            if vertical_movement > 0:
                movement.append('N')
            elif vertical_movement < 0:
                movement.append('S')
            else:
                pass
        origin[1] = val
        movement.append('D')

print(''.join(movement))
