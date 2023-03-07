import pygame
pygame.init()

PIXEL = 30
PIXELS_X = 30
PIXELS_Y = 20
TOP_MENU, BOTTOM_MENU = 80, 80
WHITE = (255, 255, 255)
MENU_COLOR = (152, 251, 152)

screen_size = [PIXEL * PIXELS_X, PIXEL * PIXELS_Y + TOP_MENU + BOTTOM_MENU]
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Paint')
timer = pygame.time.Clock()
courier = pygame.font.SysFont('courier', 12)

class Canvas:
    def __init__(self, pixels_x, pixels_y):
        self.pixels_x = pixels_x
        self.pixels_y = pixels_y
        self.pixels = self.init_pixels()
    def draw_canvas(self):
        for row in range(self.pixels_y):
            for col in range(self.pixels_x):
                self.pixels[(col, row)].draw_pixel(screen)
    def init_pixels(self):
        pixels = {}
        for x in range(self.pixels_x):
            for y in range(self.pixels_y):
                pixels[(x,y)] = Pixel(x, y, WHITE)
        return pixels
    def is_inside(self, x, y):
        return 0 <= x < self.pixels_x and 0 <= y < self.pixels_y

class Colors:
    def __init__(self):
        self.is_active = True
        self.canvas = canvas
        self.label_pos = (20, 700)
        self.label_size = (43, 43)
        self.block_size = (18, 18)
        self.palette_tuples = ((0, 0, 0), (255, 0, 0), (255, 255, 0), (128, 128, 128), (0, 0, 255), (0, 128, 0),
                               (0, 255, 255), (0, 255, 0), (128, 0, 128), (165, 42, 42), (210, 105, 30), (188, 143, 143),
                                (230, 230, 250), (221, 160, 221), (255, 165, 0), (255, 127, 80), (255, 20, 147),
                                (139, 0, 0), (127, 255, 0), (0, 100, 0), (128, 128, 0), (0, 128, 128), (30, 144, 255),
                                (25, 25, 112), (47, 79, 79), (119, 136, 153), (184, 134, 11), (75, 0, 130), 
                                (238, 130, 238), (255, 192, 203))
        self.active_color = self.palette_tuples[0]
    def set_palette(self):
        self.palette = {}
        i = 0
        for y in range(685, 736, 25):
            for x in range(70, 251, 20):
                self.palette[(x, y)] = self.palette_tuples[i]
                i += 1
    def show_palette(self, screen):
        self.set_palette()
        for key in self.palette:
            pygame.draw.rect(screen, self.palette[key], [key[0], key[1], self.block_size[0], self.block_size[1]])
    def pick_color(self):
        self.x, self.y = pygame.mouse.get_pos()
        for key in self.palette:
            if (key[0] <= self.x <= key[0] + self.block_size[0]) and (key[1] <= self.y <= key[1] + self.block_size[1]):
                self.make_active(key)
    def make_active(self, key):
        self.active_color = self.palette[key]
    def show_chosen(self, screen):
        pygame.draw.rect(screen, self.active_color, [self.label_pos[0], self.label_pos[1], self.label_size[0], self.label_size[1]])

class Pen:
    def __init__(self, canvas: Canvas, colors: Colors):
        self.is_active = False
        self.colors = colors
        self.canvas = canvas

    def draw_pen(self):
        if self.is_active and pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()         
            x, y = x // PIXEL, (y - TOP_MENU) // PIXEL
            if self.canvas.is_inside(x, y):
                self.canvas.pixels[(x, y)].color = self.colors.active_color

class Pixel:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    def draw_pixel(self, screen):
        pygame.draw.rect(screen, self.color, [self.x * PIXEL, 
        TOP_MENU + self.y * PIXEL, PIXEL, PIXEL])

class Rectangle:
    def __init__(self, canvas: Canvas, colors: Colors):
        self.is_active = False
        self.colors = colors
        self.canvas = canvas
        self.started = False
    def draw_rect_start(self):
        x_start, y_start = pygame.mouse.get_pos()
        self.x_start, self.y_start = x_start // PIXEL, (y_start - TOP_MENU) // PIXEL
        if self.canvas.is_inside(self.x_start, self.y_start):
            self.started = True
    def draw_rect_finish(self):
        if self.is_active:
            x_end, y_end = pygame.mouse.get_pos()
            x_end, y_end = x_end // PIXEL, (y_end - TOP_MENU) // PIXEL
            if self.canvas.is_inside(x_end, y_end) and self.started:
                for x in range(min(self.x_start, x_end), max(self.x_start, x_end) + 1):
                    for y in range(min(self.y_start, y_end), max(self.y_start, y_end) + 1):
                        self.canvas.pixels[(x, y)].color = self.colors.active_color   
            del self.x_start
            del self.y_start
            self.started = False

class Eraser:
    def __init__(self, canvas: Canvas):
        self.is_active = False
        self.canvas = canvas
    def erase(self):
        if self.is_active and pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            x, y = x // PIXEL, (y - TOP_MENU) // PIXEL
            if self.canvas.is_inside(x, y):
                self.canvas.pixels[(x, y)].color = WHITE

   
class InstrumentPanel:
    def __init__(self, labels):
        self.labels = labels
        self.active_label = self.labels[0]
        self.active_instrument = self.active_label.instrument
        self.active_instrument.is_active = True
        self.active_label.is_active = True
    def get_clicked_button(self):
        self.x, self.y = pygame.mouse.get_pos()
        for label in self.labels:
            if (label.position[0] <= self.x <= label.position[0] + label.label_size[0]) \
                    and (label.position[1] <= self.y <= label.position[1] + label.label_size[1]):
                self.make_active(label)
                break

    def make_active(self, label):
        self.active_instrument.is_active = False
        self.active_label.is_active = False
        self.active_label = label
        self.active_instrument = label.instrument
        self.active_instrument.is_active = True
        self.active_label.is_active = True

class Label:
    def __init__(self, image, position, instrument):
        self.image = image
        self.label_size = (self.image.get_height(), self.image.get_width())
        self.position = position
        self.instrument = instrument
        self.is_active = False
    def draw_label(self):
        if self.is_active:
            pygame.draw.rect(screen, (255, 20, 147),
                             [self.position[0] - 3, self.position[1] - 3,
                              self.label_size[0] + 6, self.label_size[1] + 6])
        screen.blit(self.image, self.position)

canvas = Canvas(PIXELS_X, PIXELS_Y)
colors = Colors()
pen = Pen(canvas, colors)
rectangle = Rectangle(canvas, colors)
eraser = Eraser(canvas)
pen_label = Label(pygame.image.load('/Users/Svetlana/PythonLearning/Paint/pen.png'), (20, 20), pen)
rect_label = Label(pygame.image.load('/Users/Svetlana/PythonLearning/Paint/rect.png'), (90, 20), rectangle)
eraser_label = Label(pygame.image.load('/Users/Svetlana/PythonLearning/Paint/eraser.png'), (160, 20), eraser)
labels = [pen_label, rect_label, eraser_label]

instrument = InstrumentPanel(labels)

while True:
    screen.fill(MENU_COLOR)
    for label in labels:
        label.draw_label()

    colors.show_chosen(screen)

    canvas.draw_canvas()
        
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                instrument.get_clicked_button()
                rectangle.draw_rect_start()
                colors.pick_color()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                rectangle.draw_rect_finish()
    pen.draw_pen()
    eraser.erase()
    colors.show_palette(screen)

    pygame.display.flip()
    timer.tick(50)