# PizzaBot

## Set Up
Please make sure to set your `PYTHONTPATH` to be your `pwd`
``` 
>>> export $PYTHONPATH=$(pwd)
```

## Running the Script
To run the `pizza_bot_script.py` use:

``` Python
python3 pizzabot_scripty.py '5x5 (3, 5), (5, 3)'
```
The Dimension and the coordinates can be changed depending on the needs.

To run the `pizzabot.py` use:

```
>>> cd pizzabot/
>>> python3 pizzabot.py '5x5 (3, 5), (3, 4)'
```
There is an assertion made to follow exactly the pattern as written in the direction.

## Running the Unittest
To run the unittest for `pizzabot.py`.
```
>>> cd pizzabot/
>>> python3 unittest -m test_pizzabot.py
>>> python3 unittest -m test_instruction.py
```
