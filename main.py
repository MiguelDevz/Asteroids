import pygame
import sys
import time
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Asteroids')

    #Groups initialized
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Asteroids containers
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    asteroid_field = AsteroidField()

    #Player containers
    Player.containers = (updatable, drawable)
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    #Shots containers
    Shot.containers = (shots, updatable, drawable)

    #init score
    font = pygame.font.Font(None, 36)
    def game_over():
        #Game Over Text
        font = pygame.font.Font(None, 100)
        game_over = font.render("Game Over!", True, (255, 255, 255))
        game_rect = game_over.get_rect(center=(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2))
        
        screen.fill("black")
        screen.blit(game_over, game_rect)

        #Score text
        font = pygame.font.Font(None, 50)
        text_score = font.render(f"Score: {player.score}", True, (255, 255, 255))
        score_rect = text_score.get_rect(center=(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2 + 80))
        screen.blit(text_score, score_rect)
        
        pygame.display.flip()

        pygame.time.delay(1000)

        pygame.quit()
        sys.exit()
    
    dt = 0

    #Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #Update the sprite group
        updatable.update(dt)
        
        #game over text
        

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                game_over()

        for asteroid in asteroids:
            for bullet in shots:
                if bullet.check_collision(asteroid):
                    asteroid.split()
                    bullet.kill()
                    player.add_to_score(1)

        screen.fill("black")

        #display score
        score_text = font.render(f"Score: {player.score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        #draw the sprite group
        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()

        #limits fps to 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()