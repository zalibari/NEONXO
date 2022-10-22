import pygame

class Button_img:
    def __init__(self, x, y, image, scale=1):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        pos = pygame.mouse.get_pos()
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def check_pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            return True