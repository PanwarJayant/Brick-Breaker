# Brick Breaker

### By Jayant Panwar

This game was created using python3 and without any curses libraries like pygame or turtle.

## Controls

- Press **'Spacebar'** to begin the game when Welcome screen is displayed
- Press **Spacebar** to release the ball from the paddle
- Use **'A'** and **'D'** keys to move the paddle left and right respectively
- Hit **Q** anytime to quit the game

## Objective

- Destroy as many bricks as you can using the 3 lives
- A life is lost when the ball fails to land on the paddle and goes below

## Scoring

- Contact with any brekable brick, i.e., Red or Green or Orange, earns you 5 points
- Grey bricks are unbreakable
- Colliding with Red brick will change its color to Orange brick and colliding with Orange brick will change its color to Green brick.
- Colliding with green brick will completely destroy that brick place
- Hitting the line of yellow colored **exploding** bricks will award you with 90 points plus the points of all the adjacent bricks combined

## Requirements and Installation

python version >= 3.8 and **colorama** module

```python3
pip3 install colorama
```

## Running the game

The game will run with **main.py** file

```python3
python3 main.py
```
