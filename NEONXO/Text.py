import pygame


class Text:
    def __init__(self, text='HELLO', width=50, height=50, pos=(0,0), rect_color=(101, 230, 255),
                 text_color=(255, 255, 255), font_size=30, font=None, use_rect=False):
        self.font = pygame.font.Font(font, font_size)
        self.text_surf = self.font.render(text, True, text_color)
        self.text_rect = self.text_surf.get_rect(topleft=pos)
        self.rect = self.text_surf.get_rect(topleft=pos)
        self.rect.width += width
        self.rect.height += height
        self.rect_color = rect_color
        self.text = text
        self.use_rect = use_rect

    def draw_t(self, screen):
        self.text_rect.center = self.rect.center
        if self.use_rect:
            pygame.draw.rect(screen, self.rect_color, self.rect, border_radius=0)
        pygame.Surface.blit(screen, self.text_surf, self.text_rect)
