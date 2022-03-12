import random
from turtle import Turtle

# build snake body
STARTINGPOSITION = [(0, 0), (-20, 0), (-40, 0)]
ANGLES = {'Up': 90, 'Down': 270, 'Right': 0, 'Left': 180}
COLORS = ['#FFC300', '#DAF7A6', '#581845', '#58D68D', '#5DADE2']
color_random = random.randint(0, len(COLORS)) - 1

class Snake:
    # Constructor
    def __init__(self):
        # Storage the segmes of the snake
        self.segments = []
        # Method to create the snake
        self.createSnake()
        # head atribute
        self.head = self.segments[0]

    def createSnake(self):
        for position in STARTINGPOSITION:
            self.addSegment(position)

    def addSegment(self, position):
        snakeSegment = Turtle('circle')
        snakeSegment.color(COLORS[color_random])
        snakeSegment.penup()
        snakeSegment.goto(position)
        self.segments.append(snakeSegment)

    def extend(self):
        self.addSegment(self.segments[-1].position())

    def move(self):
        for segNum in range(len(self.segments) - 1, -0, -1):

            newX = self.segments[segNum - 1].xcor()
            newY = self.segments[segNum - 1].ycor()
            self.segments[segNum].goto(newX, newY)

        self.head.forward(20)

    def up(self):
        if self.head.heading() != ANGLES['Down']:
            self.head.setheading(ANGLES['Up'])

    def down(self):
        if self.head.heading() != ANGLES['Up']:
            self.head.setheading(ANGLES['Down'])

    def left(self):
        if self.head.heading() != ANGLES['Right']:
            self.head.setheading(ANGLES['Left'])

    def right(self):
        if self.head.heading() != ANGLES['Left']:
            self.head.setheading(ANGLES['Right'])
