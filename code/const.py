import pygame
#c
C_ORANGE = (255, 165, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 128)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

#E
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_DAMEGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Player1': 1,
    'Player1Shoot': 25,
    'Player2': 1,
    'Player2Shoot': 20,
    'Enemy1': 1,
    'Enemy1Shoot': 20,
    'Enemy2': 1,
    'Enemy2Shoot': 15
}

ENTITY_HEALTH = {
    'Level1Bg0': 9999,
    'Level1Bg1': 9999,
    'Level1Bg2': 9999,
    'Level1Bg3': 9999,
    'Level1Bg4': 9999,
    'Level1Bg5': 9999,
    'Level1Bg6': 9999,
    'Player1': 300,
    'Player1Shoot': 1,
    'Player2': 300,
    'Player2Shoot': 1,
    'Enemy1': 60,
    'Enemy1Shoot': 1,
    'Enemy2': 40,
    'Enemy2Shoot': 1

}

ENTITY_SCORE= {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Player1': 0,
    'Player1Shoot': 0,
    'Player2': 0,
    'Player2Shoot': 0,
    'Enemy1': 100,
    'Enemy1Shoot': 0,
    'Enemy2': 125,
    'Enemy2Shoot': 0
}

ENTITY_SHOT_DELAY = {
    'Player1': 25,
    'Player2': 20,
    'Enemy1': 100,
    'Enemy2': 120
}

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Player1': 3,
    'Player1Shoot': 1,
    'Player2': 3,
    'Player2Shoot': 3,
    'Enemy1': 2,
    'Enemy1Shoot': 3,
    'Enemy2': 1,
    'Enemy2Shoot': 2
}



#M
MENU_OPTION = (
    'NEW GAME 1P',
    'NEW GAME 2P COPERATIVE',
    'NEW GAME 2P COMPETITIVE',
    'SCORES',
    'EXIT'
)

#P
PLAYER_KEY_UP = {
    'Player1': pygame.K_UP,
    'Player2': pygame.K_w
}

PLAYER_KEY_DOWN = {
    'Player1': pygame.K_DOWN,
    'Player2': pygame.K_s
}

PLAYER_KEY_LEFT = {
    'Player1': pygame.K_LEFT,
    'Player2': pygame.K_a
}

PLAYER_KEY_RIGHT = {
    'Player1': pygame.K_RIGHT,
    'Player2': pygame.K_d
}

PLAYER_KEY_SHOOT = {
    'Player1': pygame.K_LSHIFT,
    'Player2': pygame.K_RCTRL
}

#S
SPAWN_TIME = 4000

#W
WIN_WIDTH = 576
WIN_HEIGHT = 324