from turtle import Turtle

UP=90
DOWN=270
LEFT=180
RIGHT=0
MOVE_DISTANCE=20

class Snack:

    starting_position=[(0,0),(-20,0),(-40,0)]




    def __init__(self):
        self.segments=[]
        for position in self.starting_position:
            self.add_segment(position)

        self.head=self.segments[0]

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)


    def up(self):
            if self.head.heading()!=DOWN:
                self.head.setheading(UP)

    def down(self):
            if self.head.heading()!=UP:
                self.head.setheading(DOWN)

    def left(self):
            if self.head.heading()!=RIGHT:
                self.head.setheading(LEFT)

    def right(self):
            if self.head.heading()!=LEFT:
                self.segments[0].setheading(RIGHT)