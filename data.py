import pygame
import os

setting_win = {
    "WIDTH": 1440,
    "HEIGHT": 900,
    "FPS": 60,
    "NAME_GAME": "Space Shooter"
}

time_list = []

bots_list = []
bots_shot_list = []

abs_path  = os.path..abspath(__file__+"/..") + "\\image\\"


bg.image = pygame.transform.scale(pygame.image.load(abs_path + "background.jpg"), (setting_win["WIDTH"], setting_win["HEIGHT"])):
hero_image = pygame.image.load("hero.png") 
hero1_image = pygame.image.load(abs_path + "hero1.png")

hero_list_image = [hero_image, hero_image]
bot_list_image = [pygame.transform.rotate(hero_image, 180), pygame.transform.rotate(hero1_image, 100)]