import pygame
import sys

# 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pygame Window")

# 색상 정의
WHITE = (255, 255, 255)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 화면 채우기
    screen.fill(WHITE)
    
    # 화면 업데이트
    pygame.display.flip()

# 종료
pygame.quit()
sys.exit()

import pygame
import sys

# 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Keyboard Input Example")

# 색상 정의
WHITE = (255, 255, 255)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                print("Left key pressed")
            elif event.key == pygame.K_RIGHT:
                print("Right key pressed")

    # 화면 채우기
    screen.fill(WHITE)
    
    # 화면 업데이트
    pygame.display.flip()

# 종료
pygame.quit()
sys.exit()

import pygame
import sys

# 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Image Load Example")

# 색상 정의
WHITE = (255, 255, 255)

# 이미지 로드
image = pygame.image.load('path_to_your_image.png')
image_rect = image.get_rect()
image_rect.center = (screen_width // 2, screen_height // 2)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 화면 채우기
    screen.fill(WHITE)
    
    # 이미지 그리기
    screen.blit(image, image_rect)
    
    # 화면 업데이트
    pygame.display.flip()

# 종료
pygame.quit()
sys.exit()

import pygame
import sys

# 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Collision Detection Example")

# 색상 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 사각형 정의
rect1 = pygame.Rect(100, 100, 50, 50)
rect2 = pygame.Rect(300, 300, 50, 50)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 이동
    rect1.x += 1
    rect2.x -= 1
    
    # 충돌 검사
    if rect1.colliderect(rect2):
        print("Collision detected!")
    
    # 화면 채우기
    screen.fill(WHITE)
    
    # 사각형 그리기
    pygame.draw.rect(screen, RED, rect1)
    pygame.draw.rect(screen, BLUE, rect2)
    
    # 화면 업데이트
    pygame.display.flip()

# 종료
pygame.quit()
sys.exit()