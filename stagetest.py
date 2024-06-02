import pygame
import sys
import random

pygame.init()

# 화면 크기 설정
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("점프 점프")

# 색깔 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
FLOOR_COLOR = (144, 228, 144)
SPIKE_COLOR = (255, 0, 0)  # 가시 블록 색상

# 캐릭터 속성 설정
character_width, character_height = 50, 50
character_speed = 10
jump_speed = 20
gravity = 1

# 바닥 속성 설정
floor_height = 22
floor_y = SCREEN_HEIGHT - floor_height

# 발판 속성 설정
platform_width, platform_height = 100, 20
platform_color = BLUE

# 가시 블록 클래스 정의
class Spike:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 블록 클래스 정의
class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 스테이지 클래스 정의
class Stage:
    def __init__(self, num_blocks, num_spikes):
        self.blocks = self.generate_random_positions(num_blocks)
        self.spikes = self.generate_random_positions(num_spikes, is_spike=True)

    def generate_random_positions(self, num, is_spike=False):
        positions = []
        for _ in range(num):
            x = random.randint(0, SCREEN_WIDTH - platform_width)
            y = random.randint(0, SCREEN_HEIGHT - floor_height - platform_height)
            if is_spike:
                positions.append(Spike(x, y))
            else:
                positions.append(Block(x, y))
        return positions

    def draw(self, screen):
        for block in self.blocks:
            pygame.draw.rect(screen, platform_color, (block.x, block.y, platform_width, platform_height))
        for spike in self.spikes:
            pygame.draw.rect(screen, SPIKE_COLOR, (spike.x, spike.y, platform_width, platform_height))

    def check_collision(self, character_rect):
        for block in self.blocks:
            if character_rect.colliderect(pygame.Rect(block.x, block.y, platform_width, platform_height)):
                return block
        return None

    def check_spike_collision(self, character_rect):
        for spike in self.spikes:
            if character_rect.colliderect(pygame.Rect(spike.x, spike.y, platform_width, platform_height)):
                return spike
        return None

def reset_game():
    global character_x, character_y, vertical_momentum, is_on_ground, new_stage
    character_x, character_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT - character_height * 2
    vertical_momentum = 0
    is_on_ground = True
    new_stage = Stage(num_blocks=5, num_spikes=4)

# 게임 초기화
clock = pygame.time.Clock()
reset_game()

# 게임 루프
running = True
space_pressed = False

while running:
    screen.fill(WHITE)
    character_rect = pygame.Rect(character_x, character_y, character_width, character_height)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                space_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                space_pressed = False

    if space_pressed and is_on_ground:
        vertical_momentum = -jump_speed
        is_on_ground = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x -= character_speed
    if keys[pygame.K_RIGHT]:
        character_x += character_speed

    # 화면 범위 제한 및 바닥 충돌 처리
    character_x = max(0, min(SCREEN_WIDTH - character_width, character_x))
    vertical_momentum += gravity
    character_y += vertical_momentum
    character_y = min(character_y, floor_y - character_height)

    # 바닥 그리기
    pygame.draw.rect(screen, FLOOR_COLOR, (0, floor_y, SCREEN_WIDTH, floor_height))

    # 충돌 검사 및 처리
    block_collided = new_stage.check_collision(character_rect)
    if block_collided:
        if vertical_momentum > 0:
            character_y = block_collided.y - character_height
            vertical_momentum = 0
            is_on_ground = True
    elif character_y >= floor_y - character_height:
        character_y = floor_y - character_height
        vertical_momentum = 0
        is_on_ground = True
    else:
        is_on_ground = False

    # 가시 블록 충돌 검사
    spike_collided = new_stage.check_spike_collision(character_rect)
    if spike_collided:
        reset_game()  # 가시 블록에 닿으면 게임 초기화

    # 스테이지 그리기
    new_stage.draw(screen)

    # 캐릭터 생성
    pygame.draw.rect(screen, RED, character_rect)

    pygame.display.update()
    clock.tick(60)

