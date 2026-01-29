from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS
from shot import Shot
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rot = 0
        self.cooldown = 0

    def rotate(self, dt):
        self.rot += PLAYER_TURN_SPEED * dt 
    
    def update(self, dt):
        if self.cooldown > 0:
            self.cooldown -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.position += self.move(dt)
        
        if keys[pygame.K_s]:
            self.position -= self.move(dt)
        
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rot)
        return rotated_vector * PLAYER_SPEED * dt 

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rot)
        right = pygame.Vector2(0, 1).rotate(self.rot + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def shoot(self):
        if self.cooldown > 0:
            return
        shot = Shot(self.position.x, self.position.y)
        direction = pygame.Vector2(0, 1).rotate(self.rot)
        shot.velocity = direction * PLAYER_SHOOT_SPEED
        self.cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS 