import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

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
    
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #Update the sprite group
        updatable.update(dt)

        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game Over!")
                sys.exit()

        screen.fill("black")

        #draw the sprite group
        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()

        #limits fps to 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()