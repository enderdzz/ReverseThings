import pygame as pg
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
DEFAULT_FONT = pg.font.Font('fonts/arial.ttf', 22)

class Label:
    def __init__(self, x, y, text='', color=None, font=None):
        self.color = color if color else COLOR_INACTIVE
        self.coords = (x, y)
        self.text = text
        self.font = font if font else DEFAULT_FONT
        self.txt_surface = self.font.render(text, True, self.color)

    def handle_event(self, event):
        return

    def update(self):
        return

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, self.coords)

    def change_text(self, text):
        self.txt_surface = self.font.render(text, True, self.color)

class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = DEFAULT_FONT.render(text, True, self.color)
        self.active = False
        self.submitted = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Set active control or not, depending on click location.
                self.active = True
            else:
                self.active = False
            # Change the current color of the input box.
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    self.submitted = True
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = DEFAULT_FONT.render(self.text, True, self.color)

    def update(self):
        # Change the current color of the input box.
        self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE

    def draw(self, screen):
        # Blit the text.
        displayable_txt_surface = self.txt_surface.subsurface(
            (0,
             0,
             min(self.rect.w-10, self.txt_surface.get_width()),
             self.txt_surface.get_height())
        )
        screen.blit(displayable_txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)

class Button:
    def __init__(self, x, y, w, h, text='', color=COLOR_ACTIVE, font=DEFAULT_FONT, callback=None):
        self.rect = pg.Rect(x, y, w, h)
        self.text = text
        self.color = color
        self.font = font
        self.txt_surface = font.render(text, True, self.color)
        self.down_img = pg.transform.scale2x(pg.image.load('img/btndown.png'))
        self.up_img = pg.transform.scale2x(pg.image.load('img/btnup.png'))
        self.pressed = False
        self.callback = callback

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                self.pressed = True
                if self.callback:
                    self.callback()

        elif event.type == pg.MOUSEBUTTONUP:
            if self.rect.collidepoint(event.pos):
                self.pressed = False
        elif event.type == pg.MOUSEMOTION:
            if self.pressed and not self.rect.collidepoint(event.pos):
                self.pressed = False

    def update(self):
        return

    def draw(self, screen):
        # Blit the button image
        btn_image = self.down_img if self.pressed else self.up_img
        screen.blit(btn_image, self.rect)
        width = self.txt_surface.get_width()
        height = self.txt_surface.get_height()
        text_offset_x = (self.rect.w - width) / 2
        text_offset_y = (self.rect.h - height) / 2
        text_x = self.rect.x + text_offset_x
        text_y = self.rect.y + text_offset_y
        # Center button text on button surface
        screen.blit(self.txt_surface, (text_x, text_y))

class ImageButton:
    def __init__(self, x, y, w, h, up_img, down_img=None, callback=None):
        self.rect = pg.Rect(x, y, w, h)
        self.down_img = down_img if down_img else up_img
        self.up_img = up_img
        self.pressed = False
        self.callback = callback

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                self.pressed = True
                if self.callback:
                    self.callback()

        elif event.type == pg.MOUSEBUTTONUP:
            if self.rect.collidepoint(event.pos):
                self.pressed = False
        elif event.type == pg.MOUSEMOTION:
            if self.pressed and not self.rect.collidepoint(event.pos):
                self.pressed = False

    def update(self):
        return

    def draw(self, screen):
        # Blit the button image
        btn_image = self.down_img if self.pressed else self.up_img
        screen.blit(btn_image, self.rect)

class Image:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img

    def handle_event(self, event):
        return

    def update(self):
        return

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
        return