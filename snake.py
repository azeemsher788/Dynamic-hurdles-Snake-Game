import time
from turtle import Turtle, Screen

screen = Screen()
screen.tracer(0)

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segment_list = []
        self.last_direction_change_time = time.time()
        self.create_snake()
        self.head = self.segment_list[0]
        self.tail = self.segment_list[-1]
        self.head.color("#B2FA0B")
        self.tail.color("#FE9E45")
        self.head.shapesize(1.1)
        self.is_paused = False

    def create_snake(self):
        for i in range(5):
            new_segment = Turtle(shape="circle")
            new_segment.speed(0)
            new_segment.penup()
            new_segment.color("#fcfa5b")
            # Append new segment to 20 steps backward for every iteration
            new_segment.setposition(-i*20, 0)
            self.segment_list.append(new_segment)

    def increase_size(self):
        """Change tail_segment color to green and create new tail_segment with different color"""
        self.tail = self.segment_list[-1]
        self.tail.color("#fcfa5b")
        new_segment = Turtle(shape="circle")
        new_segment.speed(2)
        new_segment.penup()
        new_segment.color("#FE9E45")
        new_segment.setposition(self.tail.position())
        self.segment_list.append(new_segment)

    def pause(self):
        if not self.is_paused:
            self.is_paused = True
        else:
            self.is_paused = False


    def move(self):
        """Set location of last segment to second_last and so on"""
        if not self.is_paused:
            for seg_num in range(len(self.segment_list) - 1, 0, -1):
                new_x = self.segment_list[seg_num - 1].xcor()
                new_y = self.segment_list[seg_num - 1].ycor()
                self.segment_list[seg_num].goto(new_x, new_y)
            self.head.speed(1)
            self.head.forward(20)

    def can_change_direction(self):
        current_time = time.time()
        return (current_time - self.last_direction_change_time) > 0.07  # 200 milliseconds delay

    def update_direction_change_time(self):
        self.last_direction_change_time = time.time()

    def up(self):
        if self.head.heading() != DOWN and self.can_change_direction():
            self.head.setheading(UP)
            self.update_direction_change_time()

    def down(self):
        if self.head.heading() != UP and self.can_change_direction():
            self.head.setheading(DOWN)
            self.update_direction_change_time()

    def left(self):
        if self.head.heading() != RIGHT and self.can_change_direction():
            self.head.setheading(LEFT)
            self.update_direction_change_time()

    def right(self):
        if self.head.heading() != LEFT and self.can_change_direction():
            self.head.setheading(RIGHT)
            self.update_direction_change_time()

    def turn_back_snake(self):
        if self.head.xcor() < -680:
            self.head.setposition(680, self.head.ycor())
        elif self.head.xcor() > 680:
            self.head.setposition(-680, self.head.ycor())
        elif self.head.ycor() < -400:
            self.head.setposition(self.head.xcor(), 400)
        elif self.head.ycor() > 400:
            self.head.setposition(self.head.xcor(), -400)

    def snake_body_collision(self):
        # excluding head and comparing other
        for segment in self.segment_list[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False

    def die(self):
        for segment in self.segment_list:
            segment.color("Gray")
