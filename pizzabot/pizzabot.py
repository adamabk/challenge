from lib.point import Point
from lib.instruction import Instruction


class PizzaBot(Instruction):
    def __init__(self):
        super(PizzaBot, self).__init__()
        self.origin = Point((0, 0))

    def _horizontal_movement(self, movement: list, x_destination):
        move = x_destination - self.origin.x
        if move > 0:
            movement.append('E'*move)
        elif move < 0:
            movement.append('W'*abs(move))
        else:
            pass

        self.origin.x = x_destination

    def _vertical_movement(self, movement: list, y_destination):
        move = y_destination - self.origin.y
        if move > 0:
            movement.append('N'*move)
        elif move < 0:
            movement.append('S'*abs(move))
        else:
            pass

        self.origin.y = y_destination

    def deliver_pizza(self):
        dim = Point(self.zone)
        drops = map(Point, self.drops)
        movement = list()
        for drop in drops:
            assert drop.x <= dim.x
            assert drop.y <= dim.y
            self._horizontal_movement(movement=movement, x_destination=drop.x)
            self._vertical_movement(movement=movement, y_destination=drop.y)
            movement.append('D')

        print(''.join(movement))


if __name__ == '__main__':
    PizzaBot().deliver_pizza()
