from lib.point import Point


class PizzaBot(object):
    def __init__(self, zone: tuple, drops: list, origin=(0, 0)):
        self.origin = Point(origin)
        self.zone = Point(zone)
        self.drops = map(Point, drops)

    def _horizontal_movement(self, x_destination):
        move = x_destination - self.origin.x
        if move >= 0:
            moves = 'E' * move
        elif move < 0:
            moves = 'W' * abs(move)

        return moves

    def _vertical_movement(self, y_destination):
        move = y_destination - self.origin.y
        if move >= 0:
            moves = 'N' * move
        elif move < 0:
            moves = 'S' * abs(move)

        return moves

    def deliver_pizza(self):
        self.movement = list()
        for drop in self.drops:
            assert drop.x <= self.zone.x, "Horizontal movement beyond horizontal dimension is not allowed"
            assert drop.y <= self.zone.y, "vertical movement beyond vertical dimension is not allowed"
            h_move = self._horizontal_movement(x_destination=drop.x)
            v_move = self._vertical_movement(y_destination=drop.y)
            self.movement.append(h_move + v_move + 'D')

            self.origin = drop

        return ''.join(self.movement)
