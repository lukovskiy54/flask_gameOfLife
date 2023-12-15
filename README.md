# Game Of Life

Rule of State

Every cell on the surface of the universe can be in two states: to be alive (filled) or to be dead (empty).

White is an empty cell, green is a living cell, and maroon is a dead cell that was alive in the previous generation


The distribution of living cells at the beginning of the game is called the first generation. Each next generation is calculated based on the previous one according to these rules:

- in an empty (dead) cell, next to which there are exactly three living cells, life is born; in an empty (dead) cell, next to which there are exactly three living

cells, life is born;

- if a living cell has two or three living neighbors, this cell continues to live; otherwise, if there are less than two or more than three neighbors, the cell dies ("from loneliness" or "from overpopulation").

We will not implement stopping the game by the end rule. It will be enough to determine by eye.

As you can see, the player cannot interact with the world. All that is available to him is the generation of the first generation at the press of a button.


![image](https://github.com/lukovskiy54/flask_gameOfLife_/assets/88405806/2eb58b46-b530-4410-b213-7bdefe87c5a2)
![image](https://github.com/lukovskiy54/flask_gameOfLife_/assets/88405806/d0732915-37fe-4dcc-b558-7f73cc58285c)

![image](https://github.com/lukovskiy54/flask_gameOfLife_/assets/88405806/f4ec233d-bcb4-4442-b133-091f0baaf33f)
![image](https://github.com/lukovskiy54/flask_gameOfLife_/assets/88405806/9d0c19f1-239f-4e6b-84ee-9f1a68bc5053)
