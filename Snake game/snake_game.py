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
    def __init__(self, snake_color, pitch: SnakePitch):
        self.snake_color = snake_color
        self.pitch = pitch
        self.head, self.tail = self.get_snake_head_and_tail()
    
    def get_snake_head_and_tail(self):
        head_x = self.pitch.count_blocks // 2
        head_y = self.pitch.count_blocks // 2 + 1
        head_block = SnakeBlock(head_x, head_y)
        mid_block = SnakeBlock(head_x, head_y - 1)
        tail_block = SnakeBlock(head_x, head_y - 2)

        head_block.next = mid_block
        mid_block.prev = head_block

        mid_block.next = tail_block
        tail_block.prev = mid_block
        return head_block, tail_block

    def draw_snake(self):
        block = self.head
        while block != None:
            draw_block(self.snake_color, block.x, block.y)
            block = block.next

    def is_valid(self):
        return not self.is_in_snake(self.head, include_head = False) and self.head.is_inside(self.pitch)

    def make_move(self, d_row, d_col):
        new_head = SnakeBlock(self.head.x + d_row, self.head.y + d_col)
        
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

class Apple:
    def __init__(self, apple_color, pitch: SnakePitch, snake: Snake):
        self.apple_color = apple_color
        self.pitch = pitch
        self.snake = snake
        self.apple_block = self.place_apple()

    def place_apple(self):
        x = random.randint(0, self.pitch.count_blocks - 1)
        y = random.randint(0, self.pitch.count_blocks - 1)
        apple_block = SnakeBlock(x, y)
        while self.snake.is_in_snake(apple_block):
            apple_block.x = random.randint(0, self.pitch.count_blocks - 1)
            apple_block.y = random.randint(0, self.pitch.count_blocks - 1)
        return apple_block

    def draw_apple(self):
        draw_block(self.apple_color, self.apple_block.x, self.apple_block.y)

    def is_eaten(self):
        return self.apple_block == self.snake.head


def draw_block(color, row, column):
    return pygame.draw.rect(screen, color, [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1), 
    HEADER_MARGIN + SIZE_BLOCK+ row * SIZE_BLOCK + MARGIN * (row + 1), SIZE_BLOCK, SIZE_BLOCK])

def start_the_game():
    pitch = SnakePitch(WHITE, BLUE, MARGIN, SIZE_BLOCK, COUNT_BLOCKS, HEADER_MARGIN)
    snake = Snake(SNAKE_COLOR, pitch)
    apple = Apple(RED, pitch, snake)

    d_row = 0
    d_col = 1
    total = 0
    speed = 1
    was_keydown = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('exit')
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and not was_keydown:
                was_keydown = True
                if event.key == pygame.K_UP and d_col != 0:
                    d_row = -1
                    d_col = 0
                elif event.key == pygame.K_DOWN and d_col != 0:
                    d_row = 1
                    d_col = 0
                elif event.key == pygame.K_LEFT and d_row != 0:
                    d_row = 0
                    d_col = -1
                elif event.key == pygame.K_RIGHT and d_row != 0:
                    d_row = 0
                    d_col = 1

        
        screen.fill(FRAME_COLOR)
        pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])
        text_total = courier.render(f'Total: {total}', 0, WHITE)
        screen.blit(text_total, (SIZE_BLOCK, SIZE_BLOCK))
        text_speed = courier.render(f'Speed: {speed}', 0, WHITE)
        screen.blit(text_speed, (SIZE_BLOCK + 230, SIZE_BLOCK))
        
        pitch.draw_pitch()
        apple.draw_apple()
        snake.draw_snake()

        if not snake.is_valid():
            print('crash')
            break
            #pygame.quit()
            #sys.exit()
        
        if apple.is_eaten():
            total += 1
            speed = total // 5 + 1

            apple.apple_block.prev = snake.tail
            snake.tail.next = apple.apple_block
            snake.tail = apple.apple_block

            apple = Apple(RED, pitch, snake)

        was_keydown = False

        snake.make_move(d_row, d_col)

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