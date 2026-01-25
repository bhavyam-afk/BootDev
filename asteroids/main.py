import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    bhavyam = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        dt = clock.tick(60) / 1000

        # 1. Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # 2. Update game state
        bhavyam.update(dt)   # movement, physics, etc.

        # 3. Draw
        screen.fill("black")
        bhavyam.draw(screen)
        pygame.display.flip()



if __name__ == "__main__":
    main()
