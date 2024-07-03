import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 설정
screen_size = (300, 300)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Tic Tac Toe")

# 색상 설정
bg_color = (255, 255, 255)
line_color = (0, 0, 0)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 배경색으로 화면을 채움
    screen.fill(bg_color)

    # 틱택토 그리드 그리기
    pygame.draw.line(screen, line_color, (100, 0), (100, 300), 2)
    pygame.draw.line(screen, line_color, (200, 0), (200, 300), 2)
    pygame.draw.line(screen, line_color, (0, 100), (300, 100), 2)
    pygame.draw.line(screen, line_color, (0, 200), (300, 200), 2)

    # 화면 업데이트
    pygame.display.flip()

# Pygame 종료
pygame.quit()
sys.exit()
