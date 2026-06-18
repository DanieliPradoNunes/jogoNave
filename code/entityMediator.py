from code import entity
from code.const import WIN_WIDTH
from code.enemy import Enemy
from code.playerShoot import PlayerShoot
from code.enemyShoot import EnemyShoot

class EntityMediator:
    @staticmethod
    def __verify_collision_window(ent = entity):
        if isinstance(ent, Enemy):
            if ent.rect.left < 0:
                ent.health = 0
        if isinstance(ent, PlayerShoot):
            if ent.rect.right > WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShoot):
            if ent.rect.left < 0:
                ent.health = 0
            pass

    @staticmethod
    def verify_collision(entity_list: list[entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

    @staticmethod
    def verify_health(entity_list: list[entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)