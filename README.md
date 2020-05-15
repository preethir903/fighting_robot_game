# fighting_robot_game
Simple fighting robot game to help illustrate multiple inheritance in Python. 

All the code is included in the file fighting_robots.py

In order the run the script, type into the command-line: 
```python fighting_robots.py --name "User Name"```

Answer the questions asking what you want to name your robot and your opponent's robot. Then you start the game. You can choose to fight/ attack by typing "F" or healing yourself "H" every turn; typing "Q" will quit the game. A chaos robot does some random actions, between choosing to attack or heal or do nothing. The opponent will only attack. Initial health level, strength, and healing powers are randomly chosen from a distribution of values. The game is won when one person's health falls below critical levels (0.005).

Inspiration for the game was taken from this tutorial: https://www.python-course.eu/python3_multiple_inheritance_example.php

I used this to create the robot, fighting robot, nurse robot, and fighting nurse robot classes with similar functionalities, though I have modified the code and added a few new properties, methods, and functions (I have commented those). I created the chaos robot as well drawing on these functions, but that's not in the tutorial. And the actual main function is something I wrote, again not in the tutorial. 
