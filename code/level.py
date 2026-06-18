#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.entity import Entity
from code.entityFactory import EntityFactory
import pygame
from pygame import Surface, Rect, Font
from code.const import C_WHITE, WIN_HEIGHT


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 2000
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] =[]
        self.entity_list.extend(EntityFactory.get_entity('LevelBg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))

    def run(self):
        pygame.mixer.music.load('./assets/' + self.name + '.mp3')
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source =ent.surf, dest =ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}', C_WHITE, (10, 5))
            self.level_text(14, f'FPS: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont('Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[0])
        self.window.blit(source=text_surf, dest=text_rect)