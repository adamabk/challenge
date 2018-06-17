from lib.bot import PizzaBot
from lib.instruction import Instruction


if __name__ == '__main__':
    command = Instruction()
    solution = PizzaBot(zone=command.zone, drops=command.drops).deliver_pizza()
    print(solution)
