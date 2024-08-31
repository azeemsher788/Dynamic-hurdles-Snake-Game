import time
from turtle import Screen
from player_detail import Player, Timer
from boundries import Boundary
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from highest_score import update_score, highest_score

# Screen settings
screen = Screen()
screen.setup(width=1366, height=768)
screen.tracer(0)
screen.title("Snake game")
screen.bgpic("image.png")

# Creating objects from classes
timer = Timer()
player = Player()
boundary = Boundary()
snake = Snake()
food = Food()
score = ScoreBoard()

# key pressing function
screen.listen()
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.pause, "p")
screen.onkey(boundary.pause_boundaries, "b")


def wall_collision():
    for segment in boundary.boundary_segment_list:
        if snake.head.distance(segment) < 35:
            return True
        for snake_segment in snake.segment_list[1:]:
            if snake_segment.distance(segment) < 3:
                player.reduce_health()
                return player.health_zero()
    return False

def change_hurdle_color():
    for hurdle_seg in boundary.boundary_segment_list:
        for snake_segment in snake.segment_list[1:]:
            if snake_segment.distance(hurdle_seg) < 3 and hurdle_seg.fillcolor() == 'Red':
                hurdle_seg.color("Dark Red")
            elif snake_segment.distance(hurdle_seg) < 3 and hurdle_seg.fillcolor() != 'Dark Red':
                hurdle_seg.color("Red")


body_collide = False
wall_collide = False
while not wall_collide and not body_collide:
    screen.update()
    time.sleep(0.1)
    score.highest_score(highest_score)
    snake.move()
    timer.increase_time()
    food.mega_food_counter()
    wall_collide = wall_collision()
    body_collide = snake.snake_body_collision()
    snake.turn_back_snake()
    boundary.move_boundaries()
    change_hurdle_color()
    # Detect snake collision with food
    if snake.head.distance(food) < 15:
        food.new_food()
        snake.increase_size()
        score.increase_score()
    if score.score > 4 and snake.head.distance(food.previous_mega_food) < 15:
        score.mega_score()
        player.increase_health()
        food.hide_mega_food()

snake.die()
screen.update()
if score.score >= highest_score:
    update_score(player.name, score.score)
score.game_over()
screen.exitonclick()
