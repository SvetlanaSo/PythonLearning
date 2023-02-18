import pygame
import sys
import random
import pygame_menu
pygame.init()
bg_image = pygame.image.load('/Users/Svetlana/PythonLearning/Snake game/images/IMG_1512.jpg')
FRAME_COLOR = (0, 255, 204)
WHITE = (255, 255, 255)
BLUE = (204, 255, 255)
RED = (224, 0, 0)
YELLOW = (224, 144, 0)
SNAKE_COLOR = (0, 144, 0)
HEADER_COLOR = (0, 204, 153)
SIZE_BLOCK = 20
COUNT_BLOCKS = 20
MARGIN = 1
HEADER_MARGIN = 70

size = [SIZE_BLOCK * COUNT_BLOCKS + MARGIN * COUNT_BLOCKS + 2 * SIZE_BLOCK, 
SIZE_BLOCK * COUNT_BLOCKS + MARGIN * COUNT_BLOCKS + 2 * SIZE_BLOCK + HEADER_MARGIN]

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')
timer = pygame.time.Clock()
courier = pygame.font.SysFont('courier', 36)

class Beyond_SnakePitch:
    pass

class SnakePitch:
    def __init__(self, odd_block_color, even_block_color, margin, size_block, count_blocks, header_margin):
        self.odd_block_color = odd_block_color
        self.even_block_color = even_block_color
        self.margin = margin
        self.size_block = size_block
        self.count_blocks = count_blocks
        self.header_margin = header_margin
        self.size_x, self.size_y = self.get_size()

    def get_size(self):
        return self.size_block * self.count_blocks + self.margin * self.count_blocks + 2 * self.size_block, \
        self.size_block * self.count_blocks + self.margin * self.count_blocks + 2 * self.size_block + self.header_margin

    def draw_pitch(self):
        for row in range(self.count_blocks):
            for column in range(self.count_blocks):
                if (column + row) % 2 == 0:
                    color = self.even_block_color
                else:
                    color = self.odd_block_color
                draw_block(color, row, column)
        
class SnakeController:
    def __init__(self, up, down, left, right):
        self.up = up
        self.down = down
        self.right = right
        self.left = left
        self.controls = [up, down, right, left]
        
    def get_drow_dcol(self, event, cur_d_row, cur_d_col):
        if event.key == self.up and cur_d_col != 0:
            return  -1, 0
        elif event.key == self.down and cur_d_col != 0:
            return 1, 0
        elif event.key == self.left and cur_d_row != 0:
            return 0, -1
        elif event.key == self.right and cur_d_row != 0:
            return 0, 1
        return cur_d_row, cur_d_col
class SnakeBlock:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.prev = None
        self.next = None
    def is_inside(self, pitch: SnakePitch):
        return 0 <= self.x < pitch.count_blocks and 0 <= self.y < pitch.count_blocks
    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y

class Snake:
    def __init__(self, snake_color, pitch: SnakePitch, controller: SnakeController, player):
        self.snake_color = snake_color
        self.pitch = pitch
        self.player = player
        self.head, self.tail, self.d_row, self.d_col = self.get_snake()
        self.controller = controller
        
    def get_snake(self):
        if self.player == 0:
            head_x = self.pitch.count_blocks // 2
            head_y = self.pitch.count_blocks // 2 + 1
            head_block = SnakeBlock(head_x, head_y)
            mid_block = SnakeBlock(head_x, head_y - 1)
            tail_block = SnakeBlock(head_x, head_y - 2)
            d_row, d_col = 0, 1

        elif self.player == 1:
            head_x = self.pitch.count_blocks // 3
            head_y = self.pitch.count_blocks // 3 + 1
            head_block = SnakeBlock(head_x, head_y)
            mid_block = SnakeBlock(head_x, head_y - 1)
            tail_block = SnakeBlock(head_x, head_y - 2)
            d_row, d_col = 0, 1

        elif self.player == 2:
            head_x = self.pitch.count_blocks - self.pitch.count_blocks // 3
            head_y = self.pitch.count_blocks - self.pitch.count_blocks // 3 - 1
            head_block = SnakeBlock(head_x, head_y)
            mid_block = SnakeBlock(head_x, head_y + 1)
            tail_block = SnakeBlock(head_x, head_y + 2)
            d_row, d_col = 0, -1

        head_block.next = mid_block
        mid_block.prev = head_block

        mid_block.next = tail_block
        tail_block.prev = mid_block
        return head_block, tail_block, d_row, d_col

    def draw_snake(self):
        block = self.head
        while block != None:
            draw_block(self.snake_color, block.x, block.y)
            block = block.next

    def is_valid(self, all_snakes):
        inside_pitch = self.head.is_inside(self.pitch)
        doesnt_hit_all_snakes = True
        for snake in all_snakes:
            if snake.is_in_snake(self.head, include_head = snake != self):
                return False
        return inside_pitch and doesnt_hit_all_snakes


    def make_move(self, event):
        if event != None:
            self.d_row, self.d_col = self.controller.get_drow_dcol(event, self.d_row, self.d_col)
        new_head = SnakeBlock(self.head.x + self.d_row, self.head.y + self.d_col)
        
        new_head.next = self.head
        self.head.prev = new_head
        self.head = new_head

        new_tail = self.tail.prev
        new_tail.next = None
        self.tail.prev = None
        del self.tail
        self.tail = new_tail
    
    def is_in_snake(self, block: SnakeBlock, include_head = True):
        if include_head:
            snake_block = self.head
        else:
            snake_block = self.head.next
        while snake_block != None:
            if snake_block == block:
                return True
            snake_block = snake_block.next
        return False
    
    def add_tail(self, block: SnakeBlock):
        block.prev = self.tail
        self.tail.next = block
        self.tail = block



class Apple:
    def __init__(self, apple_color, pitch: SnakePitch, snakes):
        self.apple_color = apple_color
        self.pitch = pitch
        self.snakes = snakes
        self.apple_block = self.place_apple()

    def place_apple(self):
        x = random.randint(0, self.pitch.count_blocks - 1)
        y = random.randint(0, self.pitch.count_blocks - 1)
        apple_block = SnakeBlock(x, y)

        apple_is_in_snake = True
        while apple_is_in_snake:
            apple_is_in_snake = False
            for snake in self.snakes:
                if snake.is_in_snake(apple_block):
                    apple_is_in_snake = True
                    apple_block.x = random.randint(0, self.pitch.count_blocks - 1)
                    apple_block.y = random.randint(0, self.pitch.count_blocks - 1)
                    break

        return apple_block

    def draw_apple(self):
        draw_block(self.apple_color, self.apple_block.x, self.apple_block.y)

    def is_eaten(self):
        for snake in self.snakes:
            if self.apple_block == snake.head:
                snake.add_tail(self.apple_block)
                return True
        return False


def draw_block(color, row, column):
    return pygame.draw.rect(screen, color, [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1), 
    HEADER_MARGIN + SIZE_BLOCK+ row * SIZE_BLOCK + MARGIN * (row + 1), SIZE_BLOCK, SIZE_BLOCK])

def start_the_game():
    controller1 = SnakeController(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
    controller2 = SnakeController(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
    pitch = SnakePitch(WHITE, BLUE, MARGIN, SIZE_BLOCK, COUNT_BLOCKS, HEADER_MARGIN)
    snake1 = Snake(SNAKE_COLOR, pitch, controller1, 1)
    snake2 = Snake(SNAKE_COLOR, pitch, controller2, 2)
    snakes = [snake1, snake2]
    apple = Apple(RED, pitch, snakes)
    
    total = 0
    speed = 1
    
    while True:
        all_good = True
        for snake in snakes:
            if not snake.is_valid(snakes):
                print('crash')
                all_good = False
                break
        if not all_good:
            break

        screen.fill(FRAME_COLOR)
        pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])
        text_total = courier.render(f'Total: {total}', 0, WHITE)
        screen.blit(text_total, (SIZE_BLOCK, SIZE_BLOCK))
        text_speed = courier.render(f'Speed: {speed}', 0, WHITE)
        screen.blit(text_speed, (SIZE_BLOCK + 230, SIZE_BLOCK))

        pitch.draw_pitch()
        apple.draw_apple()
        for snake in snakes:
            snake.draw_snake()

        events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('exit')
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                events.append(event)
                
            
        if apple.is_eaten():
            total += 1
            speed = total // 5 + 1
            apple = Apple(RED, pitch, snakes)
        
        for snake in snakes:
            snake_moved = False
            for event in events:
                if event.key in snake.controller.controls:
                    snake.make_move(event)
                    snake_moved = True
                    break
            if not snake_moved:
                snake.make_move(None)

        pygame.display.flip()
        timer.tick(3 + speed)


menu = pygame_menu.Menu('Welcome', 300, 300,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='Player 1')
menu.add.button('Play', start_the_game)
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