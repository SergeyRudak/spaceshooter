import pygame
from data import*
from classes import*
from random import randint
from time import*


pygame.init()

window = pygame.display.set_mode((setting["WIDTH"], setting["HEIGHT"]))
pygame.display.set_caption(setting["NAME_GAME"])





def run():
    game = True
    level = 1
    clock = pygame.time.Clock()
    start_time_bot = pygame.time.get_ticks()
    end_time_bot = pygame.time.get_ticks()
    stop_shot = -3000
    hero = Hero(20, 20, 50, 75, image_hero, 4)
    bot = Bot(0, 0, 40, 40,bot_list_image,4)
    boss = Boss(setting["WIDTH"] // 2 - setting_boss["WIDTH"] // 2, 
    -setting_boss["HEIGHT"],
    setting_boss["WIDTH"],
    setting_boss["HEIGHT"],
    1,
    boss_image_list
    )
    shot = Shot(hero.x, hero.y, 5, 3, bullet_image, 3)
    
    


    while game:
        window.fill((75,0,130))
        window.blit(hero.image, (hero.x, hero.y))
        
        hero.hero_move()
        hero.move_images()

        for bullets in hero.bullets:
            bullets.move_bullet(hero,boss, bullets, who_shot = "hero")
            window.blit(bullets.image, (bullets.x, bullets.y))

        for buff in buff_list:
            buff.buff_move(buff)
            window.blit(buff.image,(buff.x, buff.y))
            if buff.colliderect(hero) and buff.buff == "heal":
                hero.hp += 1
                buff_list.remove(buff)
            if buff.colliderect(hero) and buff.buff == "gun":
                hero.gun = 2
                buff_list.remove(buff)
       
        end_time_bot = pygame.time.get_ticks()
        for bot in bot_list:
            window.blit(bot.image, (bot.x, bot.y))
            bot.bot_move(bot, hero)
            
            if bot.make_shot:
                bot_shot_list.append(Shot(bot.x + bot.width // 2 - 5, bot.y + bot.height, 10, 20, bullet_image, 3, bot = bot))
                bot.make_shot = False

        

        for bullet in bot_shot_list:
            window.blit(bullet.image, (bullet.x, bullet.y))
            bullet.move_bullet(hero,boss, bullet, who_shot = "bot")

        if end_time_bot - start_time_bot > 2000 and hero.points < 30:
            bot_list.append(Bot(randint(50, setting["WIDTH"] - 50), -100, 40, 40, bot_list_image, 1))
            start_time_bot = end_time_bot
            print("2")


        if hero.points >= 20:
            window.blit(boss.image,(boss.x, boss.y))

            boss.boss_move()
            if end_time_bot - start_time_bot > 2000:
                boss_shot_list.append([Shot(boss.x + setting_boss["WIDTH"] // 2 - 57, boss.y + setting_boss["HEIGHT"], 10, 20, bullet_image, 5 ),
                                       Shot(boss.x + 57, boss.y + setting_boss["HEIGHT"], 10, 20, bullet_image, 5)])
                start_time_bot = end_time_bot
            number_bullet = 0
            for bullets in boss_shot_list:
                for bullet in bullets:
                    bullet.move_bullet(hero,boss, bullet, who_shot = "boss", number_bullet = number_bullet)
                    window.blit(bullet.image, (bullet.x, bullet.y))
                number_bullet += 1
            #boss die 
            if boss.hp <= 0:
                hero.points += 100
                hero.all_points += hero.points
                hero.points = 0
                text(setting["HEIGHT"] / 2, setting["WIDTH"] / 2, str(level),window)
                level += 1
                pygame.display.flip()
                sleep(3)
                boss.hp = 10
                boss.x = setting["WIDTH"] // 2 - 100
                boss.y = -setting["HEIGHT"]
            

        
        if hero.colliderect(bot):
            hp -= 1
            if hp == 0:
                game = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    hero.move["UP"] = True
                if event.key == pygame.K_s:
                    hero.move["DOWN"] = True
                if event.key == pygame.K_d:
                    hero.image = hero_image1
                    hero.move["RIGHT"] = True
                if event.key == pygame.K_a:
                    hero.image = hero_image2
                    hero.move["LEFT"] = True
                if event.key == pygame.K_SPACE and end_time_bot - stop_shot > 3000:
                    hero.bullets.append(Shot(hero.x + 50 // 2 - 5 , hero.y, 10, 20, bullet_image, -10))
                    hero.bullet_counter += 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                        hero.move["UP"] = False
                if event.key == pygame.K_s:
                        hero.move["DOWN"] = False
                if event.key == pygame.K_d:
                        hero.move["RIGHT"] = False
                if event.key == pygame.K_a:
                        hero.move["LEFT"] = False                
        clock.tick(setting["FPS"])
        text(60, 50, str(hero.hp), window)
        text(80, 50,str(hero.points),window)
        pygame.display.flip()
           
run()