import pygame
import sys
import random
import pygame_menu
pygame.init()

bg_image = pygame.image.load('/Users/Svetlana/PythonLearning/Snake game/images/IMG_1512.jpg')

FRAME_COLOR = (255, 182, 193)
HEADER_COLOR = (255, 182, 193)
PITCH_COLOR = (255, 239, 213)
BALL_COLOR = (255, 105, 180)
GUARD_COLOR = (154, 205, 50)
TEXT_COLOR = (255, 255, 255)
TARGET_COLOR = (220, 20, 60)
SURPRISE_COLOR = (128, 0, 0)

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
SURPRISE_SIZE_X = TARGET_SIZE_X // 1.3
SURPRISE_SIZE_Y = TARGET_SIZE_Y // 1.3

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
    def __init__(self, size_x, size_y, color, place_on_pitch_x, place_on_pitch_y, pitch: Pitch, life_num, surprise = None):
        self.size_x = size_x
        self.size_y = size_y
        self.color = color
        self.place_on_pitch_x = place_on_pitch_x
        self.place_on_pitch_y = place_on_pitch_y
        self.pitch = pitch
        self.surprise = surprise
        self.life_num = life_num

        if self.surprise == None:
            self.has_surprise = False
        else:
            self.has_surprise = True
    
    def change_color(self):
        if self.life_num == 2:
            return (0, 128, 128)
        elif self.life_num == 1:
            return (255, 0, 255)

    def draw_target(self, screen):
        return pygame.draw.rect(screen, self.color, [self.place_on_pitch_x + self.pitch.ost_margins, self.place_on_pitch_y + self.pitch.top_margin, self.size_x, self.size_y])

    def __del__(self):
        if self.has_surprise:
            self.surprise.release()

class GuardController:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
    def get_place_on_pitch_x(self, event):
        if event.key == self.left:
            return -16
        elif event.key == self.right:
            return 16
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
        self.speed_x = 4
        self.speed_y = 4
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
            part_guard = self.guard.size_x // 10
            total_speed = abs(self.speed_y) + abs(self.speed_x)
            if self.guard.place_on_pitch_x <= self.x < self.guard.place_on_pitch_x + part_guard:
                self.speed_x = -total_speed * 7 // 10
                self.speed_y = -total_speed * 3 // 10
            elif self.guard.place_on_pitch_x + part_guard <= self.x < self.guard.place_on_pitch_x + part_guard * 2:
                self.speed_x = -total_speed * 6 // 10
                self.speed_y = -total_speed * 4 // 10
            elif self.guard.place_on_pitch_x + part_guard * 4 <= self.x < self.guard.place_on_pitch_x + part_guard * 6:
                self.speed_x = (total_speed * 2 // 10) * (self.speed_x // (abs(self.speed_x)))
                self.speed_y = -total_speed * 8 // 10
            elif self.guard.place_on_pitch_x + part_guard * 8 <= self.x < self.guard.place_on_pitch_x + part_guard * 9:
                self.speed_x = total_speed * 6 // 10
                self.speed_y = -total_speed * 4 // 10
            elif self.guard.place_on_pitch_x + part_guard * 9 <= self.x < self.guard.place_on_pitch_x + part_guard * 10:
                self.speed_x = total_speed * 7 // 10
                self.speed_y = -total_speed * 3 // 10

        for target in self.targets:
            if self.was_bottom_clashed(target):
                self.y = target.place_on_pitch_y + self.radius + target.size_y
                self.speed_y *= - 1
                target.life_num -= 1
                if target.life_num == 0:
                    self.targets.remove(target)
                    break
                else:
                    target.color = target.change_color()
            if self.was_top_clashed(target):
                self.y = target.place_on_pitch_y - self.radius
                self.speed_y *= -1           
                target.life_num -= 1
                if target.life_num == 0:
                    self.targets.remove(target)
                    break
                else:
                    target.color = target.change_color()                
            if self.was_left_side_clashed(target):
                self.x = target.place_on_pitch_x - self.radius
                self.speed_x *= -1
                target.life_num -= 1
                if target.life_num == 0:
                    self.targets.remove(target)
                    break
                else:
                    target.color = target.change_color()
            if self.was_right_side_clashed(target):
                self.x = target.place_on_pitch_x + self.radius + target.size_x
                self.speed_x *= - 1
                target.life_num -= 1
                if target.life_num == 0:
                    self.targets.remove(target)
                    break 
                else:
                    target.color = target.change_color()               

class Surprise:
    def __init__(self, size_x, size_y, color, place_on_pitch_x, place_on_pitch_y, pitch: Pitch, guard: Guard, balls, targets):
        self.is_active = False
        self.size_x = size_x
        self.size_y = size_y
        self.color = color
        self.pitch = pitch
        self.guard = guard
        self.speed_x = 0
        self.speed_y = 3
        self.place_on_pitch_x = place_on_pitch_x
        self.place_on_pitch_y = place_on_pitch_y
        self.balls = balls
        self.targets = targets
    
    def release(self):
        self.is_active = True

    def draw_surprise(self, screen):
        if self.is_active:
            return pygame.draw.rect(screen, self.color, [self.place_on_pitch_x + self.pitch.ost_margins, self.place_on_pitch_y + self.pitch.top_margin, self.size_x, self.size_y])
    
    def speed_up_ball(self):
        for ball in self.balls:
            if ball.speed_x > 0:
                ball.speed_x += 2
            else:
                ball.speed_x -= 2
            if ball.speed_y > 0:
                ball.speed_y += 2
            else:
                ball.speed_y -= 2

    def slow_down_guard(self):
        if self.guard.speed < 0:
            self.guard.speed += 3
        elif self.guard.speed > 0:
            self.guard.speed -= 3

    def speed_up_guard(self):
        if self.guard.speed < 0:
            self.guard.speed -= 4
        elif self.guard.speed > 0:
            self.guard.speed += 4
    
    def add_balls(self):
        ball = Ball(BALL_X, BALL_Y, BALL_RADIUS, BALL_COLOR, self.pitch, self.guard, self.targets)
        ball.speed_y = -abs(self.balls[0].speed_y) 
        self.balls.append(ball)

    def apply_effect(self):
        lst_of_effects = [self.speed_up_ball, self.slow_down_guard, self.speed_up_guard, self.add_balls]
        return random.choice(lst_of_effects)

    def was_guard_clashed(self, other):
        same_level_as_other =  other.place_on_pitch_y + other.size_y >= self.place_on_pitch_y + self.size_y >= other.place_on_pitch_y
        on_top_of_other = other.place_on_pitch_x <= self.place_on_pitch_x <= other.place_on_pitch_x + other.size_x
        return same_level_as_other and on_top_of_other
    def was_end_of_pitch_reached(self):
        return self.place_on_pitch_y + self.size_y >= self.pitch.size_y
           
    def make_move(self):
        if self.is_active:
            self.place_on_pitch_y += self.speed_y
            if self.was_guard_clashed(self.guard):
                self.place_on_pitch_y = self.guard.place_on_pitch_y - self.size_y
                effect = self.apply_effect()
                effect()
                return True
            elif self.was_end_of_pitch_reached():
                self.place_on_pitch_y = self.pitch.size_y - self.size_y
                return True
        return False
class Level:
    def __init__(self, level_num):
        self.level_num = level_num
    
    def create_level (self):
        if self.level_num == 1:
            self.controller = GuardController(pygame.K_LEFT, pygame.K_RIGHT)
            self.pitch = Pitch(PITCH_SIZE_X, PITCH_SIZE_Y, PITCH_COLOR, TOP_MARGIN, OST_MARGINS)
            self.guard = Guard(GUARD_SIZE_X, GUARD_SIZE_Y, GUARD_COLOR, GUARD_PITCH_X, GUARD_PITCH_Y, self.pitch, self.controller)
            self.targets = []
            self.surprises = []
            self.balls = [Ball(BALL_X, BALL_Y, BALL_RADIUS, BALL_COLOR, self.pitch, self.guard, self.targets)]

            for i in range(70, self.pitch.size_y // 3, TARGET_SIZE_Y + 4):
                self.sample_for_j = random.sample(range(4, self.pitch.size_x, TARGET_SIZE_X + 4), 5)
                for j in range(4, self.pitch.size_x, TARGET_SIZE_X + 4):
                    if i == 70 + 2 * (TARGET_SIZE_Y + 4) and self.pitch.size_x // 3 <= j <= self.pitch.size_x - self.pitch.size_x // 3:
                        life_num = 3
                    else:
                        life_num = 1
                    if j in self.sample_for_j:
                        surprise = Surprise(SURPRISE_SIZE_X, SURPRISE_SIZE_Y, SURPRISE_COLOR, j + 4, i, self.pitch, self.guard, self.balls, self.targets)
                        target = Target(TARGET_SIZE_X, TARGET_SIZE_Y, TARGET_COLOR, j, i, self.pitch, life_num, surprise)
                        self.surprises.append(surprise)
                    else:
                        target = Target(TARGET_SIZE_X, TARGET_SIZE_Y, TARGET_COLOR, j, i, self.pitch, life_num)
                    if target.size_x + target.place_on_pitch_x >= self.pitch.size_x:
                        break
                    self.targets.append(target)

    def complete_level (self, screen):
        while True:
            screen.fill(FRAME_COLOR)
            pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], TOP_MARGIN])
            self.text_level = courier.render(f'Level: {self.level_num}', 0, TEXT_COLOR)
            screen.blit(self.text_level, (20, 20))

            self.pitch.draw_pitch(screen)
            self.guard.draw_guard(screen)
            
            for target in self.targets:
                target.draw_target(screen)
            

            self.guard.make_move()
            for ball in self.balls:
                ball.draw_ball(screen)
                ball.make_move()
                if ball.was_lost() and len(self.balls) == 1:
                    return False
                elif ball.was_lost() and len(self.balls) > 1:
                    self.balls.remove(ball)

                if len(self.targets) == 0:
                    return True
            
            for surprise in self.surprises:
                surprise.draw_surprise(screen)
                if surprise.make_move():
                    self.surprises.remove(surprise)


            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    self.guard.start_move(event)
                elif event.type == pygame.KEYUP:
                    self.guard.stop_move()
            
            pygame.display.flip()
            timer.tick(30)
            

def play_game():
    level = Level(1)
    while True:
        level.create_level()
        if level.complete_level(screen):
            level.level_num += 1
            #return
        else:
            return


gametheme = pygame_menu.themes.Theme(background_color=(0, 0, 0, 0), cursor_color=(47, 79, 79), 
                                     title_background_color=(4, 47, 126))

menu = pygame_menu.Menu('Welcome', 700, 580,
                       theme=gametheme)

menu.add.text_input('Name :', default='Player 1')
menu.add.button('Play', play_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

while True:
    screen.blit(bg_image, (0, 0))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if menu.is_enabled():
        menu.update(events)
        menu.draw(screen)

    pygame.display.update()