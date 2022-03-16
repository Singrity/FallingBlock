import pygame
import sys
from settings import *
from level import Level


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Lupa & Pupa")

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.level = Level()

        self.is_running = False

    def run(self):
        self.is_running = True
        while self.is_running:

            frame_time_ms = self.clock.tick(FPS)
            frame_time_s = frame_time_ms / 1000.

            self.handle_events()
            self.draw()
            self.update(frame_time_s)

    def stop(self):
        self.is_running = False
        pygame.quit()
        sys.exit()

    def draw(self):
        self.screen.fill('black')
        self.level.draw()
        pygame.display.update()

    def update(self, time):
        self.level.update(time)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.stop()
                self.level.handle_key_down_events(event)
            if event.type == pygame.KEYUP:
                self.level.handle_key_up_events(event)


if __name__ == '__main__':
    game = Game()
    game.run()




