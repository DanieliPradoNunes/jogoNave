#!/usr/bin/python
# -*- coding: utf-8 -*-

from entity import Entity
from code.const import ENTITY_SHOT_DELAY, ENTITY_SPEED
from code.enemyShoot import EnemyShoot

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shoot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
    
    def shoot(self):
        self.shoot_delay -= 1
        if self.shoot_delay == 0:
            self.shoot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShoot(name = f'{self.name}Shoot', position = (self.rect.centerx, self.rect.centery))

