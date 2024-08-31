from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SHAPE = "square"


class CreateBoundary:

    def __init__(self):
        self.colors = ["#67DED6", "#FBFF77"]

    def create_boundary(self, x_pos, y_pos, boundary_segment_list, location):
        for i in range(15):
            new_boundary_segment = Turtle(shape=SHAPE)
            new_boundary_segment.speed(0)
            new_boundary_segment.penup()
            new_boundary_segment.color(self.colors[i % 2])
            if location == "left":
                new_boundary_segment.setposition(x_pos, y_pos - i * 20)
            elif location == "right":
                new_boundary_segment.setposition(x_pos, y_pos + i * 20)
            elif location == "top":
                new_boundary_segment.setposition(x_pos - i * 20, y_pos)
            else:
                new_boundary_segment.setposition(x_pos + i * 20, y_pos)
            boundary_segment_list.append(new_boundary_segment)

class Boundary(CreateBoundary):

    def __init__(self):
        super().__init__()
        self.boundary_segment_list = []
        self.colors = ["#67DED6", "#FBFF77"]
        self.is_paused = False
        self.create_boundary(-400, 220, self.boundary_segment_list, "left")
        self.create_boundary(400, -220, self.boundary_segment_list, "right")
        self.create_boundary(260, 320, self.boundary_segment_list, "top")
        self.create_boundary(-260, -320, self.boundary_segment_list, "bottom")
        # Assigning heads of all boundaries
        self.left_boundary_head = self.boundary_segment_list[0]
        self.right_boundary_head = self.boundary_segment_list[15]
        self.top_boundary_head = self.boundary_segment_list[30]
        self.bottom_boundary_head = self.boundary_segment_list[45]

    def pause_boundaries(self):
        if not self.is_paused:
            self.is_paused = True
        else:
            self.is_paused = False

    def move_left_boundary(self):
        for seg_num in range(14, 0, -1):
            new_x = self.boundary_segment_list[seg_num - 1].xcor()
            new_y = self.boundary_segment_list[seg_num - 1].ycor()
            self.boundary_segment_list[seg_num].goto(new_x, new_y)
        self.left_boundary_head.speed(1)
        self.left_boundary_head.setheading(UP)
        # if head of boundary reach at turning location then turn it 90 degree
        if self.left_boundary_head.xcor() > 380:
            self.left_boundary_head.setheading(DOWN)
        elif self.left_boundary_head.ycor() > 300:
            self.left_boundary_head.setheading(RIGHT)
        if self.left_boundary_head.ycor() < -300:
            self.left_boundary_head.setheading(LEFT)
            if self.left_boundary_head.xcor() < -380:
                self.left_boundary_head.setheading(UP)
        self.left_boundary_head.forward(20)

    def move_right_boundary(self):
        for seg_num in range(29, 15, -1):
            new_x = self.boundary_segment_list[seg_num - 1].xcor()
            new_y = self.boundary_segment_list[seg_num - 1].ycor()
            self.boundary_segment_list[seg_num].goto(new_x, new_y)
        self.right_boundary_head.speed(1)
        self.right_boundary_head.setheading(DOWN)
        # if head of boundary reach at turning location then turn it 90 degree
        if self.right_boundary_head.xcor() < -390:
            self.right_boundary_head.setheading(UP)
        elif self.right_boundary_head.ycor() < -300:
            self.right_boundary_head.setheading(LEFT)
        if self.right_boundary_head.ycor() > 300:
            self.right_boundary_head.setheading(RIGHT)
            if self.right_boundary_head.xcor() > 380:
                self.right_boundary_head.setheading(DOWN)
        self.right_boundary_head.forward(20)

    def move_top_boundary(self):
        for seg_num in range(44, 30, -1):
            new_x = self.boundary_segment_list[seg_num - 1].xcor()
            new_y = self.boundary_segment_list[seg_num - 1].ycor()
            self.boundary_segment_list[seg_num].goto(new_x, new_y)
        self.top_boundary_head.speed(1)
        self.top_boundary_head.setheading(RIGHT)
        # if head of boundary reach at turning location then turn it 90 degree
        if self.top_boundary_head.ycor() < -300:
            self.top_boundary_head.setheading(LEFT)
        elif self.top_boundary_head.xcor() > 380:
            self.top_boundary_head.setheading(DOWN)
        if self.top_boundary_head.xcor() < -390:
            self.top_boundary_head.setheading(UP)
            if self.top_boundary_head.ycor() > 300:
                self.top_boundary_head.setheading(RIGHT)
        self.top_boundary_head.forward(20)

    def move_bottom_boundary(self):
        for seg_num in range(len(self.boundary_segment_list) - 1, 45, -1):
            new_x = self.boundary_segment_list[seg_num - 1].xcor()
            new_y = self.boundary_segment_list[seg_num - 1].ycor()
            self.boundary_segment_list[seg_num].goto(new_x, new_y)
        self.bottom_boundary_head.speed(1)
        self.bottom_boundary_head.setheading(LEFT)
        # if head of boundary reach at turning location then turn it 90 degree
        if self.bottom_boundary_head.ycor() > 300:
            self.bottom_boundary_head.setheading(RIGHT)
        elif self.bottom_boundary_head.xcor() < -380:
            self.bottom_boundary_head.setheading(UP)
        if self.bottom_boundary_head.xcor() > 380:
            self.bottom_boundary_head.setheading(DOWN)
            if self.bottom_boundary_head.ycor() < -300:
                self.bottom_boundary_head.setheading(LEFT)
        self.bottom_boundary_head.forward(20)

    def move_boundaries(self):
        if not self.is_paused:
            self.move_left_boundary()
            self.move_right_boundary()
            self.move_top_boundary()
            self.move_bottom_boundary()
