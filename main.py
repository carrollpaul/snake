import pygame, sys, random
from rich.traceback import install

install()
pygame.init()

class Snake():

    def __init__(self):
        self.body = []
        self.body.append(Segment(WIDTH/2, HEIGHT/2)) # Make first segemnt and add to body
        self.x_change = 0
        self.y_change = 0
        self.len = 0
    
    def update(self):
        old_head = self.body[-1].copy() # Copy last segment in array aka first segment in snake
        new_head = self.body.pop(0) # Remove first segment in array aka last segment in snake
        new_head.x = (old_head.x + self.x_change) 
        new_head.y = (old_head.y + self.y_change)
        self.body.append(new_head)
    
    def show(self):
        # Make and draw every segment in the snake
        for segment in self.body:
            rect = [segment.x, segment.y, 10, 10]
            pygame.draw.rect(screen, WHITE, rect)
    
    def set_dir(self, x, y):
        self.x_change = x
        self.y_change = y
    
    def grow(self):
        self.len += 1
        head = self.body[-1].copy()
        self.body.append(head)
    
    def eat(self, x, y):
        if self.body[0].x == x and self.body[0].y == y:
            print('food eaten')
            self.grow()
            return True
        return False

class Segment():

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def copy(self):
        return Segment(self.x, self.y)

def get_food_location():
    x = random.randint(0, WIDTH/10) * 10
    y = random.randint(0, HEIGHT/10) * 10
    return x, y

def put_food(x, y):
    food = [x, y, 10, 10]
    pygame.draw.rect(screen, BLUE, food)

def game_over():
    x = snake.body[-1].x # X position of head
    y = snake.body[-1].y # Y position of head
    if (x <= 0 or x >= WIDTH or y <= 0 or y >= HEIGHT):
        return True
    if snake.len > 1:
        for segment in snake.body[:-1]:
            # If the head coordinates equal a segemnt in the body's coordinates, they must be touching
            if segment.x == x and segment.y == y: 
                return True
    return False

# SETUP
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WIDTH = 400
HEIGHT = 400

# Make screen
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
snake = Snake()
food_x, food_y = get_food_location() # Starting food location

# GAME LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.set_dir(-10, 0)
            elif event.key == pygame.K_RIGHT:
                snake.set_dir(10, 0)
            elif event.key == pygame.K_DOWN:
                snake.set_dir(0, 10)
            elif event.key == pygame.K_UP:
                snake.set_dir(0, -10)
    
    if snake.eat(food_x, food_y):
        food_x, food_y = get_food_location()

    screen.fill(BLACK)
    put_food(food_x, food_y)
    snake.update()
    snake.show()
    pygame.display.flip()

    if game_over():
        print("GAME OVER")
        break

    pygame.time.wait(100)

sys.exit()