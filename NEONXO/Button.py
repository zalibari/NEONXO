import pygame


class Button:
    def __init__(self, text='PLAY', width=200, height=100, pos=(0, 0), elevation=10, font=None,
                 font_size=60, top_color=(101, 230, 255), bottom_color=(255, 201, 51),
                 collide_color=(255, 255, 255), text_color=(8, 13, 43)):
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]
        self.font = pygame.font.Font(font, font_size)
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = top_color
        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = bottom_color
        self.collide_color = collide_color
        self.text = text
        self.text_surf = self.font.render(text, True, text_color)
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def change_text(self, newtext='HELLO', text_color=(8, 13, 43)):
        self.text_surf = self.font.render(newtext, True, text_color)
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self, screen, top_color):
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation
        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=0)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=0)
        pygame.Surface.blit(screen, self.text_surf, self.text_rect)
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = self.collide_color
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
        else:
            self.top_color = top_color
        if pygame.mouse.get_pressed()[0] == 0:
            self.dynamic_elevation = self.elevation

    def check_pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            return True

