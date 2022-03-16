import pygame

import random

from block import Block
from player import Player
from settings import *


class Level:
    def __init__(self):
        self.surface = pygame.display.get_surface()
        self.blocks = pygame.sprite.Group()
        self.player = Player(y=660)

        self.spawn_time = 0
        self.spawn_cooldown = 2000

    def draw(self):
        self.blocks.draw(self.surface)
        self.player.draw(self.surface)

    def update(self, frame_time_s):
        frame_ticks = pygame.time.get_ticks()

        if frame_ticks - self.spawn_time >= self.spawn_cooldown:
            self.spawn_block()

        self.blocks.update(frame_time_s)
        self.player.update(frame_time_s)

        self.process_collision()

    def spawn_block(self):
        self.spawn_time = pygame.time.get_ticks()
        random_x = random.randint(0, 20) * BLOCK_SIZE
        Block((random_x, -BLOCK_SIZE), self.blocks)
        print(self.blocks.sprites())

    def handle_key_down_events(self, event):
        self.player.handle_key_down_events(event)

    def handle_key_up_events(self, event):
        self.player.handle_key_up_events(event)

# TODO: Check only first block collision
    def process_collision(self):
        for block in self.blocks:
            tmp_blocks = self.blocks.copy()
            tmp_blocks.remove(block)
            if block.rect.bottom > HEIGHT:
                block.speed = 0

            for tmp_block in tmp_blocks:
                if block.rect.bottom >= tmp_block.rect.top and block.rect.x == tmp_block.rect.x:
                    block.speed = 0







