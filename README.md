# PizzaBot

## Running the Script
To run the `pizzabot.py` use:

### Set Up
```
>>> cd pizzabot/
>>> export $PYTHONPATH=$(pwd)
```

### Running the Program
```
>>> python3 pizzabot.py '5x5 (0, 0) (1, 3) (4, 4) (4, 2) (4, 2) (0, 1) (3, 2) (2, 3) (4, 1)'
```
There is an assertion made to follow exactly the pattern as written in the direction.

### Running the Unittest
To run the unittest for `pizzabot.py`.
```
>>> python3 -m unittest tests/test_pizzabot.py
>>> python3 -m unittest tests/test_instruction.py
```
