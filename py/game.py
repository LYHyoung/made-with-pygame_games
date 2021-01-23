import random
import pygame
###############################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() # 초기화

# 화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Quiz") # 게임 이름

# FPS
clock = pygame.time.Clock()
###############################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
#background = pygame.image.load("C:/Users/이예형/python/pygame_basic/background.png")
background = pygame.image.load("C:/Users/이예형/python/pygame_basic/quiz_background.jpg")

# 캐릭터 만들기
#character = pygame.image.load("C:/Users/이예형/python/pygame_basic/character.png")
character = pygame.image.load("C:/Users/이예형/python/pygame_basic/dog.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
charater_x_pos = (screen_width / 2) - (character_width / 2)
charater_y_pos = screen_height - character_height

# 똥 만들기
#ddong = pygame.image.load("C:/Users/이예형/python/pygame_basic/enemy.png")
ddong = pygame.image.load("C:/Users/이예형/python/pygame_basic/ddong.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0, screen_width - ddong_width)
ddong_y_pos = 0
ddong_speed = 10

# 이동 위치
to_x = 0

# Font 정의
game_font = pygame.font.Font(None, 40)

# Mission Complete (성공)
# # Game Over (캐릭터 똥에 맞음)
game_result = "Game Over"

running = True # 게임이 진행중인가?
character_speed = 10
while running:
    dt = clock.tick(30) # 게임화면의 초당 프레임 수를 설정
    
    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): # 이벤트 루프가 켜지고 GUI가 들어오는지 확인함
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0


    # 3. 게임 캐릭터 위치 정의
    charater_x_pos += to_x

    if charater_x_pos < 0:
        charater_x_pos = 0
    elif charater_x_pos > screen_width - character_width:
        charater_x_pos = screen_width - character_width
    
    ddong_y_pos += ddong_speed

    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width - ddong_width)

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = charater_x_pos
    character_rect.top = charater_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    if character_rect.colliderect(ddong_rect):
        print("충돌했어요")
        running = False

    # 5. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(character, (charater_x_pos, charater_y_pos))
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))

    pygame.display.update() # 게임화면을 다시 그리기! 반드시 계속 호출되어야 함

# 게임 오버 메시지
msg = game_font.render(game_result, True, (255, 255, 0)) # 노란색
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()

# 2초 대기
pygame.time.delay(2000)

# pygame 종료
pygame.quit()