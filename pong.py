import tkinter as tk

# Constants
WIDTH = 800
HEIGHT = 600
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
PADDLE_SPEED = 20
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100

# Initialize the window
root = tk.Tk()
root.title("Pong")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Draw the ball and paddles
ball = canvas.create_oval(WIDTH/2 - 10, HEIGHT/2 - 10, WIDTH/2 + 10, HEIGHT/2 + 10, fill="white")
player_paddle = canvas.create_rectangle(WIDTH - 20, HEIGHT/2 - 50, WIDTH - 10, HEIGHT/2 + 50, fill="white")
opponent_paddle = canvas.create_rectangle(10, HEIGHT/2 - 50, 20, HEIGHT/2 + 50, fill="white")

# Variables to store the ball's direction
ball_dx = BALL_SPEED_X
ball_dy = BALL_SPEED_Y

# Score variables
player_score = 0
opponent_score = 0

# Draw the score
player_score_text = canvas.create_text(WIDTH - 50, 30, text=str(player_score), font=("Arial", 24), fill="white")
opponent_score_text = canvas.create_text(50, 30, text=str(opponent_score), font=("Arial", 24), fill="white")

def update_score():
    canvas.itemconfig(player_score_text, text=str(player_score))
    canvas.itemconfig(opponent_score_text, text=str(opponent_score))

def move_ball():
    global ball_dx, ball_dy, player_score, opponent_score

    canvas.move(ball, ball_dx, ball_dy)
    ball_pos = canvas.coords(ball)

    # Ball collision with top and bottom walls
    if ball_pos[1] <= 0 or ball_pos[3] >= HEIGHT:
        ball_dy = -ball_dy

    # Ball collision with paddles
    if (ball_pos[2] >= canvas.coords(player_paddle)[0] and ball_pos[3] >= canvas.coords(player_paddle)[1] and ball_pos[1] <= canvas.coords(player_paddle)[3]) or (ball_pos[0] <= canvas.coords(opponent_paddle)[2] and ball_pos[3] >= canvas.coords(opponent_paddle)[1] and ball_pos[1] <= canvas.coords(opponent_paddle)[3]):
        ball_dx = -ball_dx

    # Ball goes out of bounds
    if ball_pos[0] <= 0:
        player_score += 1
        update_score()
        reset_ball()
    elif ball_pos[2] >= WIDTH:
        opponent_score += 1
        update_score()
        reset_ball()

    canvas.after(30, move_ball)

def reset_ball():
    global ball_dx, ball_dy
    canvas.coords(ball, WIDTH/2 - 10, HEIGHT/2 - 10, WIDTH/2 + 10, HEIGHT/2 + 10)
    ball_dx = BALL_SPEED_X if ball_dx > 0 else -BALL_SPEED_X
    ball_dy = BALL_SPEED_Y if ball_dy > 0 else -BALL_SPEED_Y

def move_paddle(event):
    if event.keysym == 'Up':
        canvas.move(player_paddle, 0, -PADDLE_SPEED)
    elif event.keysym == 'Down':
        canvas.move(player_paddle, 0, PADDLE_SPEED)

root.bind("<Up>", move_paddle)
root.bind("<Down>", move_paddle)

# Move the opponent paddle automatically
def move_opponent_paddle():
    ball_pos = canvas.coords(ball)
    paddle_pos = canvas.coords(opponent_paddle)
    if paddle_pos[1] < ball_pos[1]:
        canvas.move(opponent_paddle, 0, PADDLE_SPEED)
    elif paddle_pos[3] > ball_pos[3]:
        canvas.move(opponent_paddle, 0, -PADDLE_SPEED)

    canvas.after(30, move_opponent_paddle)

move_ball()
move_opponent_paddle()

root.mainloop()
