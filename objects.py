import pygame
from os import listdir
from os.path import isfile, join
from player import * 
from game_logic import *


def draw(window, background, bg_image, player, objects, offset_x):
    for tile in background:
        window.blit(bg_image, tile)

    for obj in objects:
        obj.draw(window, offset_x)

    player.draw(window, offset_x)

    pygame.display.update()

def get_block(size):
    path = join("assets", "Terrain", "Terrain.png", )
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 128, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_grass_block(size):
    path = join("assets", "Terrain", "Terrain.png", )
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_ice_block(size):
    path = join("assets", "Traps", "Sand Mud Ice", "Sand Mud Ice (16x6).png", )
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(128, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_swamp_mini_block(size):
    path = join("assets", "Traps", "Sand Mud Ice", "Sand Mud Ice (16x6).png", )
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(65, 48, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_gold_pad(size):
    path = join("assets", "Terrain", "Terrain.png", )
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(272, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_wood_pad(size):
    path = join("assets", "Terrain", "Terrain.png", )
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(272, 16, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_gold_x_border(size):
    path = join("assets", "Terrain", "Terrain.png", )
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(272, 128, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_gold_y_border(size):
    path = join("assets", "Terrain", "Terrain.png", )
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(320, 128, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)



class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name

    def draw(self, win, offset_x):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))

class Block(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class GrassBlock(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_grass_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class IceBlock(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_ice_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
    
class SwampMiniBlock(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, 60, 60)
        block = get_swamp_mini_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
    
class GoldPad(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, 10)
        goldPad = get_gold_pad(size)
        self.image.blit(goldPad, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class WoodPad(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, 10)
        woodPad = get_wood_pad(size)
        self.image.blit(woodPad, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class XGoldBorder(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, 32)
        woodPad = get_gold_x_border(size)
        self.image.blit(woodPad, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class YGoldBorder(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, 32, 97)
        woodPad = get_gold_y_border(size)
        self.image.blit(woodPad, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
        
class Fire(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "fire")
        self.fire = load_sprite_sheets("Traps", "Fire", width, height)
        self.image = self.fire["off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "off"

    def on(self):
        self.animation_name = "on"

    def off(self):
        self.animation_name = "off"

    def loop(self):
        sprites = self.fire[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0


# def draw(self, win, offset_x):
#     win.blit(self.image, (self.rect.x - offset_x, self.rect.y))
#     red_surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
#     red_surface.fill((255, 0, 0, 128))
#     win.blit(red_surface, (self.rect.x - offset_x, self.rect.y))