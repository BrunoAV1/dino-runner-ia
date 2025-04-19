import pygame
import random
from ai.agent import DinoAgent

WIDTH, HEIGHT = 800, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GROUND = 350
GRAVITY = 1

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = GROUND
        self.vel_y = 0
        self.jumping = False

    def update(self):
        if self.jumping:
            self.vel_y += GRAVITY
            self.rect.y += self.vel_y
            if self.rect.y >= GROUND:
                self.rect.y = GROUND
                self.jumping = False
                self.vel_y = 0

    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.vel_y = -16  # Pulo mais alto

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, height=40):
        super().__init__()
        self.image = pygame.Surface((20, height))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = GROUND - height + 40
        self.passed = False

    def update(self, speed):
        self.rect.x -= speed
        if self.rect.right < 0:
            self.kill()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Aprendizado de IA com Dino Runner. Por - Bruno Vasconcellos")
        self.clock = pygame.time.Clock()
        self.dino = Dino()
        self.obstacles = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group(self.dino)
        self.agent = DinoAgent()
        self.font = pygame.font.SysFont(None, 30)
        self.score = 0
        self.deaths = 0
        self.speed = 5
        self.last_obstacle_time = 0
        self.obstacle_delay = 1000
        self.fast_mode = False

    def run(self):
        running = True

        while running:
            self.screen.fill(WHITE)
            current_time = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.agent.reset_q_table()
                        print("Q-table resetada!")
                        self.score = 0
                        self.deaths = 0
                    if event.key == pygame.K_t:
                        self.fast_mode = not self.fast_mode
                        print("Modo turbo:", "Ativado" if self.fast_mode else "Desativado")

            # ESCALONA DIFICULDADE COM SCORE
            if self.score < 10:
                self.obstacle_delay = 1200
            elif self.score < 20:
                self.obstacle_delay = 1000
            elif self.score < 30:
                self.obstacle_delay = 800
            elif self.score < 50:
                self.obstacle_delay = 700
            elif self.score < 80:
                self.obstacle_delay = 600
            else:
                self.obstacle_delay = 500

            # GERA OBSTÁCULOS COM ESPAÇAMENTO VIÁVEL
            if current_time - self.last_obstacle_time > self.obstacle_delay:
                if not self.obstacles or self.obstacles.sprites()[-1].rect.x < WIDTH - 200:
                    height = random.choice([30, 40])
                    obstacle = Obstacle(height)
                    self.obstacles.add(obstacle)
                    self.all_sprites.add(obstacle)
                    self.last_obstacle_time = current_time

            state = self.get_state()
            action = self.agent.choose_action(state)
            if action == 1:
                self.dino.jump()

            for obs in self.obstacles:
                obs.update(self.speed)
            self.dino.update()

            if pygame.sprite.spritecollideany(self.dino, self.obstacles):
                self.agent.learn(-100, self.get_state())
                self.deaths += 1
                self.reset()
                self.last_obstacle_time = pygame.time.get_ticks()
                continue
            else:
                self.agent.learn(1, self.get_state())

            for obs in self.obstacles:
                if not obs.passed and obs.rect.right < self.dino.rect.left:
                    obs.passed = True
                    self.score += 1

            self.all_sprites.draw(self.screen)
            self.show_stats()
            pygame.display.flip()

            self.clock.tick(300 if self.fast_mode else 30)
            self.speed = 5 + self.score // 10

    def get_state(self):
        obs = sorted([o for o in self.obstacles if o.rect.x > self.dino.rect.x], key=lambda x: x.rect.x)
        if len(obs) >= 2:
            dist1 = obs[0].rect.x - self.dino.rect.x
            h1 = obs[0].rect.height
            dist2 = obs[1].rect.x - self.dino.rect.x
            h2 = obs[1].rect.height
        elif len(obs) == 1:
            dist1 = obs[0].rect.x - self.dino.rect.x
            h1 = obs[0].rect.height
            dist2 = 800
            h2 = 0
        else:
            dist1, h1, dist2, h2 = 800, 0, 800, 0
        return (dist1, h1, dist2, h2, self.dino.rect.y)

    def show_stats(self):
        death_text = self.font.render(f"Mortes: {self.deaths}", True, BLACK)
        score_text = self.font.render(f"Score: {self.score}", True, BLACK)
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(death_text, (10, 40))

    def reset(self):
        self.obstacles.empty()
        self.all_sprites = pygame.sprite.Group(self.dino)
        self.dino.rect.y = GROUND
        self.dino.jumping = False
        self.dino.vel_y = 0
        self.score = 0
        self.speed = 5
