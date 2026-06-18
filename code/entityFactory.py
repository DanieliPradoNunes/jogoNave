#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.background import Background
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(self, entity_name: str, position=(0,0)):
        match entity_name:
            case 'LevelBg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'LevelBg{i}', position(0,0)))
                    list_bg.append(Background(f'LevelBg{i}', position(WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2))
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2))