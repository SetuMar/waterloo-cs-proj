from pytmx.util_pygame import load_pygame
import pygame
# import pygame and pytmx

import block
import enemy
from settings import *
# import game files

import powerups

class GameOverHandler:
    def __init__(self) -> None:
        self.current_level_completed = False
        self.level_number = 1
        
        self.current_level = r"Graphics/Levels/l1.tmx"
        
    def complete_level(self, tiles, player):
        self.level_number += 1
        self.current_level = f'Graphics/Levels/l{self.level_number}.tmx'
        tiles, player.rect.topleft = self.generate_level()
        
        self.current_level_completed = False
    
        return tiles
    
    def generate_level(self):
        tmx_data = load_pygame(self.current_level)
        # get the data for a specific level
        
        tiles = {}
        # list of all tiles
        
        player_position = None
        
        for layer in tmx_data.visible_layers:
            # go through all visible layers
            
            layer_tiles = []
            
            for tile_data in layer.tiles():
                image = tile_data[2]
                position = pygame.Vector2(tile_data[0] * BLOCK_SIZE, tile_data[1] * BLOCK_SIZE)
                if layer.name in powerups.Powerup.powerup_layer_names: 
                    layer_tiles.append(powerups.Powerup(image, position, layer.name))
                elif layer.name == "player":
                    player_position = position
                elif layer.name == "walker_enemy":
                    layer_tiles.append(enemy.Walker(image, position))
                else:
                    layer_tiles.append(block.Tile(image, position))
            # add tile to list of tiles
            
            tiles.update({layer.name:layer_tiles})
                
        return tiles, player_position
        # return list of tiles and player position