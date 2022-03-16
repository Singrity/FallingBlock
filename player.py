import pygame
from settings import WIDTH, HEIGHT


class Player(pygame.sprite.Sprite):

    def __init__(self, x=WIDTH/2, y=HEIGHT/2):
        super().__init__()
        self.image = pygame.Surface((32, 60))
        self.rect = self.image.get_rect(center=(x, y))

        self.speed = 1300
        self.score = 0

        # Flags
        self.moving_right = False
        self.moving_left = False

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

    def update(self, frame_time_s):
        self.process_movement(frame_time_s)


    def process_movement(self, frame_time_s):
        if self.moving_right:
            self.rect.x += self.speed * frame_time_s
        elif self.moving_left:
            self.rect.x -= self.speed * frame_time_s

    def handle_key_down_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.moving_right = True
        if event.key == pygame.K_LEFT:
            self.moving_left = True
        if event.key == pygame.K_UP:
            pass
        if event.key == pygame.K_DOWN:
            pass

    def handle_key_up_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.moving_right = False
        if event.key == pygame.K_LEFT:
            self.moving_left = False
        if event.key == pygame.K_UP:
            pass
        if event.key == pygame.K_DOWN:
            pass
