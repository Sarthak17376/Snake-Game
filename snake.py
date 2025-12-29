from turtle import Turtle, Screen

screen = Screen()

STARTING_POSITIONS = [(20, 0), (0, 0), (-20, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.list_of_segments = []
        self.make_snake()

    def make_snake(self):
        for positions in STARTING_POSITIONS:
            new_snake_segment = Turtle()
            new_snake_segment.shape("square")
            new_snake_segment.color("white")
            new_snake_segment.penup()
            new_snake_segment.goto(positions)
            self.list_of_segments.append(new_snake_segment)
        self.list_of_segments[0].shape("arrow")
        self.list_of_segments[0].color("blue")
        self.list_of_segments[0].showturtle()

    def move_snake(self):

        for seg_num in range(len(self.list_of_segments)-1, 0, -1):
            new_x = self.list_of_segments[seg_num-1].xcor()
            new_y = self.list_of_segments[seg_num-1].ycor()
            if seg_num > 0:
                self.list_of_segments[seg_num].goto(new_x, new_y)
        self.list_of_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if not self.list_of_segments[0].heading() == 270:
            self.list_of_segments[0].setheading(90)

    def down(self):
        if not self.list_of_segments[0].heading() == 90:
            self.list_of_segments[0].setheading(270)

    def left(self):
        if not self.list_of_segments[0].heading() == 0:
            self.list_of_segments[0].setheading(180)

    def right(self):
        if not self.list_of_segments[0].heading() == 180:
            self.list_of_segments[0].setheading(0)

    def extend_snake(self):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        tail = self.list_of_segments[len(self.list_of_segments)-1]
        if tail.heading() == 90:
            tail.setheding(90)
            new_x = tail.xcor()
            new_y = tail.ycor()-20
            new_segment.goto(new_x, new_y)

        elif tail.heading() == 180:
            tail.setheding(180)
            new_x = tail.xcor() + 20
            new_y = tail.ycor()
            new_segment.goto(new_x, new_y)
        self.list_of_segments.append(new_segment)

    def snake_reset(self):
        for segments in self.list_of_segments:
            segments.hideturtle()
