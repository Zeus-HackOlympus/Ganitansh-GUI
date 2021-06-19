import random
import pygame
from pygame.locals import *
from pygame.math import *

pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
running = True

cell_size = 40
cell_number = 100

screen = pygame.display.set_mode((1600,900))
clock = pygame.time.Clock()

# background

pygame.mixer.init()
pygame.mixer.music.load("../assets/music/game_music1.ogg")

class Snake:
    def __init__(self):
        # snake starts from certer
        self.direction = Vector2(0,0)
        self.body = [Vector2(5,5),Vector2(4,5),Vector2(3,5),Vector2(2,5)]
        self.new_block = False


        self.head_up = pygame.image.load('../assets/snake/Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('../assets/snake/Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('../assets/snake/Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('../assets/snake/Graphics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('../assets/snake/Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('../assets/snake/Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('../assets/snake/Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('../assets/snake/Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('../assets/snake/Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('../assets/snake/Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('../assets/snake/Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('../assets/snake/Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('../assets/snake/Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('../assets/snake/Graphics/body_bl.png').convert_alpha()
        self.crunch_sound = pygame.mixer.Sound('../assets/snake/Sound/crunch.wav')

        # self.pixel = Rect(self.x,self.y,30,30)
    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        for index,block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

            if index == 0 :
                screen.blit(self.head,block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail,block_rect)

            else :
                previous_block = self.body[index+1] - block
                next_block = self.body[index-1] - block
                if (previous_block.x == next_block.x) :
                    screen.blit(self.body_vertical,block_rect)
                elif (previous_block.y == next_block.y):
                    screen.blit(self.body_horizontal,block_rect)
                else:
                    if (previous_block.x == -1 and next_block.y == -1) or (previous_block.y == -1 and next_block.x == -1):
                        screen.blit(self.body_tl,block_rect)
                    elif (previous_block.x == -1 and next_block.y == 1) or (previous_block.y == 1 and next_block.x == -1):
                        screen.blit(self.body_bl,block_rect)
                    elif (previous_block.x == 1 and next_block.y == -1) or (previous_block.y == -1 and next_block.x == 1):
                        screen.blit(self.body_tr,block_rect)
                    elif (previous_block.x == 1 and next_block.y == 1) or (previous_block.y == 1 and next_block.x == 1):
                        screen.blit(self.body_br,block_rect)



    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1, 0): self.head = self.head_right
        elif head_relation == Vector2(0, 1): self.head = self.head_up
        elif head_relation == Vector2(0, -1): self.head = self.head_down
    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0): self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1): self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1): self.tail = self.tail_down
    def move_snake(self):
        if self.add_block() == True :
            body = self.body[:]
            body.insert(0,body[0] + self.direction)
            self.body = body[:]
            self.new_block = False
        else:
            body = self.body[:-1]
            body.insert(0,body[0] + self.direction)
            self.body = body[:]

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def add_block(self):
        self.new_block = True
    def reset(self):
        self.body = [Vector2(5,5),Vector2(4,5),Vector2(3,5),Vector2(2,5)]
        self.direction = Vector2(0,0)



class FRUIT:
    def __init__(self,a,b):
        # a and b : a * b = ab
        self.a = a
        self.b = b
        # TODO: ADD REMAINING SPAWN POINTS
        self.spawn =  [
            Vector2(50, 75),  Vector2(400, 75), Vector2(1000, 75), Vector2(1500, 75),
            Vector2(50, 215), Vector2(400, 215), Vector2(1000, 215), Vector2(1200, 215), Vector2(1400, 215), Vector2(1500, 215),
            Vector2(50, 355), Vector2(1000, 355),  Vector2(1400, 355), Vector2(1500, 355),
            Vector2(50, 455),  Vector2(1000, 455), Vector2(1500, 455)
        ]
        self.pos_of_random = []

    def update_coordinates(self):
        pos = random.randint(0,len(self.spawn)-1)
        a = self.spawn[pos]
        self.spawn.remove(self.spawn[pos])
        return a

    def draw_cicle(self,pos:tuple):
        self.pos_of_ans = pos
        circle = pygame.draw.circle(screen, Color("red"), pos, 40)
        font = pygame.font.Font('../assets/Fonts/Comic_Neue/ComicNeue-Bold.ttf', 40)
        font = font.render(str(self.a * self.b), True, Color("gold"))
        screen.blit(font, font.get_rect(center=circle.center))
    def update_coordinates_random(self):
        arr = []
        for i in range(8):
            a = self.spawn[random.randint(0,len(self.spawn)-1)]
            self.spawn.remove(a)
            arr.append(a)
        return arr

    def draw_random(self,pos,random):
        # pos
        for index,i in enumerate(pos) :
            self.pos_of_random.append(i)
            circle = pygame.draw.circle(screen, Color("red"), i, 40)
            font = pygame.font.Font('../assets/Fonts/Comic_Neue/ComicNeue-Bold.ttf', 40)
            font = font.render(str(random[index]* random[index+1]), True, Color("gold"))
            screen.blit(font, font.get_rect(center=circle.center))


class Main:
    def __init__(self):
        a = random.randint(10, 99)
        b = random.randint(10, 99)
        self.snake = Snake()
        self.a = a
        self.b = b
        self.fruit = FRUIT(a,b)
        self.randomize()
    def randomize(self):
        self.random_prod = self.get_random_product()
        self.co_of_random = self.fruit.update_coordinates_random()
        self.co_of_ans = self.fruit.update_coordinates()
        self.co_of_random = self.fruit.update_coordinates_random()
    def get_a(self):
        return self.a
    def get_b(self):
        return self.b

    def check_collision(self):
        print(self.fruit.pos_of_ans)
        if self.fruit.pos_of_ans == self.snake.body[0]:
            print("COLLISION COLLISION COLLISION COLLISION COLLISION COLLISION COLLISION COLLISION")
            self.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()

            for block in self.snake.body[1:]:
                if block == self.snake.body[0]:
                    self.randomize()
    def check_fail(self):
        if (self.snake.body[0].x > screen.get_width()-50) or (self.snake.body[0].y >screen.get_height()-50 ):
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0] :
                self.game_over()
    def game_over(self):
        print("game over")
        self.snake.reset()

    def draw_score(self):
        score_text = str(len(self.snake.body) - 4)
        score_surface = game_font.render("Score: " + score_text,True,Color("Black"))
        score_x = int(cell_size*cell_number - cell_number - 60)
        score_y = int(cell_size*cell_number - cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        screen.blit(screen,score_rect)

    def draw_equation(self):
        font = pygame.font.Font("../assets/Fonts/Comic_Neue/ComicNeue-Bold.ttf",40)
        font = font.render(str(self.a) +" x " + str(self.b),True,Color("White"),Color("Black"))
        screen.blit(font,(1600-200,900-50))

    def get_update(self):
        self.snake.move_snake()
        self.check_fail()
        self.check_collision()

    def get_random_product(self):
        arr = []
        for i in range(8):
            x = random.randint(5,self.a)
            y = random.randint(5, self.b)
            arr.append(x)
            arr.append(y)
        return arr

    def draw_objects(self):
        self.rock1 = pygame.image.load("../assets/images/rock2.png")
        self.rock2 = pygame.image.load("../assets/images/rock1.png")
        self.wall1 = pygame.image.load("../assets/images/wall2.jpg")
        self.bg    = pygame.image.load("../assets/images/grass.png")
        screen.blit(self.bg, (0, 0))

        # self.draw_grass()
        screen.blit(self.bg, (1600 - 1024, 0))
        # screen.blit(self.rock1, (screen.get_width() / 4 - 200, screen.get_height() / 2 - 120))
        # screen.blit(self.rock1, (3 * screen.get_width() / 4 - 160, screen.get_height() / 2 - 120))
        # screen.blit(self.wall1, (screen.get_width() / 2 - 280, 0))
        # screen.blit(self.wall1, (screen.get_width() / 2 - 280, screen.get_height() - 200))
        self.draw_score()
        self.snake.draw_snake()
        self.draw_equation()
        self.fruit.draw_cicle(self.co_of_ans)
        self.fruit.draw_random(self.co_of_random,self.random_prod)
        # temp - just for testing and getting spawn points

"""
    TODO: 
        BACKGROUND - done 
        MAKE GRIDS ON BACKGROUND 
        MAKE SNAKE - done
        Add graphics to snake   
        MAKE FRUIT (MATHS EQUATION) - done 
        Add fruit spawn points 
        MAKE TOTAL SUM TO BE ACHIEVED
        COMPILE EVERYTHING
"""




# pygame.mixer.music.play()

main = Main()
game_font = pygame.font.Font('../assets/Fonts/Comic_Neue/ComicNeue-Bold.ttf',24)
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,200)

while running:
    for event in pygame.event.get():
        # if snake touches ball update pos_of_center and
        if event.type == pygame.QUIT : 
            running = False
        if event.type == SCREEN_UPDATE :
            main.get_update()
        if event.type == KEYDOWN:
            if event.key in (pygame.K_UP,pygame.K_w) :
                # if not moving downward so that it doesnt destroy itself
                if main.snake.direction.y != 1:
                    main.snake.direction = Vector2(0,-1)
            if event.key in (pygame.K_RIGHT,pygame.K_d):
                if main.snake.direction.x != -1 :
                    main.snake.direction = Vector2(1,0)
            if event.key in (pygame.K_DOWN,pygame.K_s) :
                if main.snake.direction.y != -1 :
                    main.snake.direction = Vector2(0,1)
            if event.key in (pygame.K_LEFT,pygame.K_a):
                if main.snake.direction.x != 1:
                    main.snake.direction = Vector2(-1,0)
    pygame.display.set_caption("Ganitansh-GUI")
    main.draw_objects()
    pygame.display.update()
    clock.tick(60) # fps = 60 
