from lib.point import Point
from lib.instruction import Instruction

class PizzaBot(Instruction):
    def __init__(self):
        super(PizzaBot, self).__init__()
        self.origin = Point((0, 0))

    def _horizontal_movement(self, movement:list, x_destination):
        if self.origin.x < x_destination:
            move = x_destination - self.origin.x
            movement.append('E'*move)
        elif self.origin.x > x_destination:
            move = self.origin.x - x_destination
            movement.append('W'*move)
        else:
            pass

        self.origin.x = x_destination

    def _vertical_movement(self, movement:list, y_destination):
        if self.origin.y < y_destination:
            move = y_destination - self.origin.y
            movement.append('N'*move)
        elif self.origin.y > y_destination:
            move = self.origin.y - y_destination
            movement.append('S'*move)
        else:
            pass

        self.y_origin = y_destination

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
