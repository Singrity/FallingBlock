import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/box.png')
        self.rect = self.image.get_rect(topleft=position)

        self.y = position[1]
        self.speed = 100

    def update(self, frame_time_s):
        self.y += self.speed * frame_time_s
        self.rect.y = self.y

    def draw(self, surface):
        surface.blit(self.image, self.rect)
