import pygame
import sys
import random
import pygame_menu
pygame.init()

FRAME_COLOR = (255, 182, 193)
HEADER_COLOR = (255, 182, 193)
PITCH_COLOR = (255, 239, 213)
BALL_COLOR = (255, 105, 180)
GUARD_COLOR = (154, 205, 50)
TEXT_COLOR = (255, 255, 255)
TARGET_COLOR = (220, 20, 60)

PITCH_SIZE_X = 660
PITCH_SIZE_Y = 500
TOP_MARGIN = 80
OST_MARGINS = 20
GUARD_SIZE_X = 150
GUARD_SIZE_Y = 20
GUARD_PITCH_Y = PITCH_SIZE_Y - GUARD_SIZE_Y
GUARD_PITCH_X = PITCH_SIZE_X // 2
BALL_X = PITCH_SIZE_X // 2 
BALL_Y = PITCH_SIZE_Y // 2 + PITCH_SIZE_Y // 3
BALL_RADIUS = 15
TARGET_SIZE_Y = 20
TARGET_SIZE_X = 37

size = [PITCH_SIZE_X + OST_MARGINS * 2, PITCH_SIZE_Y + TOP_MARGIN]

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Arcanoid')
timer = pygame.time.Clock()
courier = pygame.font.SysFont('courier', 36)

class Pitch:
    def __init__(self, size_x, size_y, color, top_margin, ost_margins):
        self.size_x = size_x
        self.size_y = size_y
        self.color = color
        self.ost_margins = ost_margins
        self.top_margin = top_margin
        
    def draw_pitch(self, screen):
        return pygame.draw.rect(screen, self.color, [self.ost_margins, self.top_margin, self.size_x, self.size_y])

class Target:
    def __init__(self, size_x, size_y, color, place_on_pitch_x, place_on_pitch_y, pitch: Pitch):
        self.size_x = size_x
        self.size_y = size_y
        self.color = color
        self.place_on_pitch_x = place_on_pitch_x
        self.place_on_pitch_y = place_on_pitch_y
        self.pitch = pitch
    
    def draw_target(self, screen):
        return pygame.draw.rect(screen, self.color, [self.place_on_pitch_x + self.pitch.ost_margins, self.place_on_pitch_y + self.pitch.top_margin, self.size_x, self.size_y])

class GuardController:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
    def get_place_on_pitch_x(self, event):
        if event.key == self.left:
            return -13
        elif event.key == self.right:
            return 13
        else:
            return 0

class Guard:
    def __init__(self, size_x, size_y, color, place_on_pitch_x, place_on_pitch_y, pitch: Pitch, controller: GuardController):
        self.size_x = size_x
        self.size_y = size_y
        self.color = color
        self.place_on_pitch_x = place_on_pitch_x
        self.place_on_pitch_y = place_on_pitch_y
        self.pitch = pitch
        self.controller = controller
        self.speed = 0

    def draw_guard(self, screen):
        return pygame.draw.rect(screen, self.color, [self.place_on_pitch_x + self.pitch.ost_margins, self.place_on_pitch_y + self.pitch.top_margin, self.size_x, self.size_y])

    def start_move(self, event):
        self.speed = self.controller.get_place_on_pitch_x(event)

    def stop_move(self):
        self.speed = 0

    def make_move(self):
        right_edge = self.pitch.size_x - self.size_x
        left_edge = 0
        self.place_on_pitch_x += self.speed

        if self.place_on_pitch_x > right_edge:
            self.place_on_pitch_x = right_edge
        if self.place_on_pitch_x < left_edge:
            self.place_on_pitch_x = left_edge

class Ball:
    def __init__(self, x, y, radius, color, pitch: Pitch, guard: Guard, targets):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.pitch = pitch
        self.speed_x = 9
        self.speed_y = 9
        self.guard = guard
        self.targets = targets
    
    def draw_ball(self, screen):
        return pygame.draw.circle(screen, self.color, [self.x + self.pitch.ost_margins, self.y + self.pitch.top_margin], self.radius)
    
    def were_borders_clashed(self):
        right_edge, left_edge  = self.pitch.size_x - self.radius, self.radius
        top_edge = self.radius    
        if self.x > right_edge:
            self.x = right_edge
        if self.x < left_edge:
            self.x = left_edge
        
        if self.y < top_edge:
            self.y = top_edge        
        if self.x >= right_edge or self.x <= left_edge:
            self.speed_x *= - 1
        if self.y <= top_edge:
            self.speed_y *= - 1

    def was_top_clashed(self, other):
        same_level_as_other =  other.place_on_pitch_y + other.size_y >= self.y + self.radius >= other.place_on_pitch_y
        on_top_of_other = other.place_on_pitch_x <= self.x <= other.place_on_pitch_x + other.size_x
        return same_level_as_other and on_top_of_other

    def was_bottom_clashed(self, other):
        same_level_as_other = other.place_on_pitch_y <= self.y - self.radius <= other.place_on_pitch_y + other.size_y
        under_other = other.place_on_pitch_x <= self.x <= other.place_on_pitch_x + other.size_x
        return same_level_as_other and under_other

    def was_left_side_clashed(self, other):
        same_edge_as_other = other.place_on_pitch_x + other.size_x >= self.x + self.radius >= other.place_on_pitch_x
        within_other = other.place_on_pitch_y <= self.y <= other.place_on_pitch_y + other.size_y
        return same_edge_as_other and within_other
        
    def was_right_side_clashed(self, other):
        same_edge_as_other = other.place_on_pitch_x <= self.x - self.radius <= other.place_on_pitch_x + other.size_x
        within_other = other.place_on_pitch_y <= self.y <= other.place_on_pitch_y + other.size_y
        return same_edge_as_other and within_other

    def was_lost(self):
        return self.y + self.radius - 10 >= self.pitch.size_y

    def make_move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        self.were_borders_clashed()

        if self.was_top_clashed(self.guard):
            self.y = self.guard.place_on_pitch_y - self.radius
            self.speed_y *= - 1

        for target in self.targets:
            if self.was_bottom_clashed(target):
                self.y = target.place_on_pitch_y + self.radius + target.size_y
                self.speed_y *= - 1
                targets.remove(target)
                break
            if self.was_top_clashed(target):
                self.y = target.place_on_pitch_y - self.radius
                self.speed_y *= -1
                targets.remove(target)
                break
            if self.was_left_side_clashed(target):
                self.x = target.place_on_pitch_x - self.radius
                self.speed_x *= -1
                targets.remove(target)
                break
            if self.was_right_side_clashed(target):
                self.x = target.place_on_pitch_x + self.radius + target.size_x
                self.speed_x *= - 1
                targets.remove(target)
                break                


level = 1

controller = GuardController(pygame.K_LEFT, pygame.K_RIGHT)
pitch = Pitch(PITCH_SIZE_X, PITCH_SIZE_Y, PITCH_COLOR, TOP_MARGIN, OST_MARGINS)
guard = Guard(GUARD_SIZE_X, GUARD_SIZE_Y, GUARD_COLOR, GUARD_PITCH_X, GUARD_PITCH_Y, pitch, controller)
targets = []
ball = Ball(BALL_X, BALL_Y, BALL_RADIUS, BALL_COLOR, pitch, guard, targets)
#ball_new = Ball(BALL_X-100, BALL_Y-100, BALL_RADIUS, BALL_COLOR, pitch, guard, targets)

for i in range(70, pitch.size_y // 3, TARGET_SIZE_Y + 4):
    for j in range(4, pitch.size_x, TARGET_SIZE_X + 4):
        target = Target(TARGET_SIZE_X, TARGET_SIZE_Y, TARGET_COLOR, j, i, pitch)
        if target.size_x + target.place_on_pitch_x >= pitch.size_x:
            break
        targets.append(target)

while True:
    #level.create(1)
    #level.play()

    screen.fill(FRAME_COLOR)
    pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], TOP_MARGIN])
    text_level = courier.render(f'Level: {level}', 0, TEXT_COLOR)
    screen.blit(text_level, (20, 20))

    pitch.draw_pitch(screen)
    guard.draw_guard(screen)
    
    for target in targets:
        target.draw_target(screen)
    
    guard.make_move()
    ball.draw_ball(screen)
    ball.make_move()
    #ball_new.draw_ball(screen)
    #ball_new.make_move()
    
    if ball.was_lost():
        break

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            guard.start_move(event)
        elif event.type == pygame.KEYUP:
            guard.stop_move()


    pygame.display.flip()
    timer.tick(30)
    #pygame.display.update()
