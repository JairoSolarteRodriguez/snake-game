import time
from turtle import Screen
from scoreboard import ScoreBoard

# call class
from snake import Snake
from food import Food

# Creating board game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('#FF5733')
screen.title('Programate Snake Game')

screen.tracer(0)

# Instances for snake
snake = Snake()

#instances for food
food = Food()

#instances for score board
scoreBoard = ScoreBoard()

# Listening keys
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

# animate snake
gameIsOn = True

while gameIsOn:
    screen.update()
    time.sleep(0.09)

    # Moving of snake
    snake.move()

    # detect colision of food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreBoard.increaseScore()
        snake.extend()

    # detect colision of walls
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        gameIsOn = False
        scoreBoard.gameOver()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            gameIsOn = False
            scoreBoard.gameOver()


screen.mainloop()
