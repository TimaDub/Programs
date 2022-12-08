import pygame, time, datetime
from random import randint

# base
need_to_update_screen = True
WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500
pygame.mixer.init()
pygame.font.init()
NAME = "w.12835"
ICON = pygame.image.load("img/os/icon.png")
Image1 = pygame.image.load("img/Bg/back1.webp")
Image2 = pygame.image.load("img/Bg/img.jpg")
Audio1 = pygame.mixer.Sound("audio/Audio1.mp3")
Audio2 = pygame.mixer.Sound("audio/Audio2.mp3")
Audio3 = pygame.mixer.Sound("audio/Audio3_Full.mp3")
Audio4 = pygame.mixer.Sound("audio/Audio4.mp3")
Audio4_Sec = pygame.mixer.Sound("audio/Audio4_Sec.mp3")
Audio_Back = pygame.mixer.Sound("audio/Back_Play_N_Go.mp3")
Audio_6_Win_1 = pygame.mixer.Sound("audio/voxworker-voice-file (7).mp3")
Audio_6_Win_2 = pygame.mixer.Sound("audio/voxworker-voice-file (6).mp3")
Audio_6_Win_3 = pygame.mixer.Sound("audio/voxworker-voice-file (8).mp3")
menu_picture = pygame.image.load("img/Bg/bg.jpg")
img_One = pygame.image.load("img/Bg/bg_One.jpg")
img_Field = pygame.image.load("img/Bg/Field_1.png")
img_Player = pygame.image.load("img/Player/Player_Yellow.png")
img_Enemy = pygame.image.load("img/Player/Player_Red.png")
B_Bucks_img = pygame.image.load("img/os/B_bucks.png")
B_Ultra_img = pygame.image.load("img/os/Ultra_B_Bucks.png")
icon_B_bucks_img = pygame.image.load("img/os/B_bucks_icon.png")
icon_Ultra_B_bucks_img = pygame.image.load("img/os/Ultra_B_Bucks_icon.png")
FPS = 60
# base
# colors
BLACK = 0, 0, 0 # 1
RED = 255, 0, 0 # 2
BLUE = 0, 0, 255 # 3
GREEN = 0, 255, 0 # 4
YELLOW = 255, 255, 0 # 5
WHITE = 255, 255, 255 # 6
PINK = 242, 140, 242 # 7
LIGHT_BLUE = 0, 255, 255 # 8
LIGHT_PINK = 255, 0, 150 # 9
PURPLE = 150, 0, 250 # 10
LIGHT_GREEN = 0, 255, 50 # 11
ORANGE = 255, 150, 0 # 12
LIGHT_LIGHT_PINK = 255, 150, 150 # 13
DARK = 125, 115, 100 # 14
# colors
R_Y = randint(0, 2)
if R_Y == 0:
    You = pygame.image.load("img/Player/Block_Player_Yellow.png")
else:
    You = pygame.image.load("img/Player/Block_Player_Red.png")
Run = True
clock = pygame.time.Clock()
ConncretTime = 1
pygame.init()
Page1 = False
Page2 = False
Page3 = False
Page4 = False
Page5_Reg = False
Page6_Log = False
Page7_menu = False
Page8_Play = False
Page9_Reset = False
Tr_Fl = False
q_Next = False
T_N = 0
x = 0
y = 0
x_Player, y_Player = 243, 701
activ_Btt = 0
Col_Active = RED
Col_Font = RED
# Settings
step = 0
need_input = False
Name_Click = False
Password_Click = False
enemy_turn = False
B_Bucks_x = 1100
Ultra_B_Bucks_x = 1100
P_N = False
N_N = False
Start = True
First_Time = False
your_turn = True
input_text = ''
button_font = pygame.font.Font('font/font.ttf', 72)
label_font = pygame.font.Font('font/font1.otf', 400)
ConncretMin = 99
ConncretSec = 99
l = open('logins/Log_S.dll', 'r')
L_Password = l.readline()
l.close()
print(L_Password)
y_T = 0
x_T = 0
Level_1 = 0
Audio_Back.play(-1)
Audio_Back.set_volume(0.1)
Was_Reset = False
Pass = True
Audio4_One = True
Seven_one = True
pass_2 = True
pass_3 = True
player_win = False


def find(s, info):
    otkr = None
    for i in range(len(s)):
        if s[i] == "<":
            otkr = i
        if s[i] == ">" and otkr != None:
            zakr = i
            res = s[otkr + 1:zakr]
            res = res.split(',')
            return res[info]
    return ''

Player_name_Find = find(L_Password, 0)
Password_Find = find(L_Password, 1)
Save_Find = find(L_Password, 2)
Level_Find = int(find(L_Password, 3))
Status_Find = find(L_Password, 6)
Your_status = Status_Find
B_Bucks_Find = find(L_Password, 4)
Ultera_B_Bucks_Find = find(L_Password, 5)
#
Player_name = Player_name_Find
Password = Password_Find
B_Bucks = B_Bucks_Find
Ultra_B_Bucks = Ultera_B_Bucks_Find
B_Bucks = int(B_Bucks)
Ultra_B_Bucks = int(Ultra_B_Bucks)

x_Test = 0
this_level = Level_Find

while Run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False
        if need_input == True and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if Page4 == True:
                    need_input = False
                    Page4 = False
                    Page5_Reg = True
                    Player_name = input_text
                    input_text = ''
                    Audio2.play()
                if Page5_Reg == True:
                    Password = input_text
                    if Password != '':
                        need_input = False
                        Page5_Reg = False
                        Page6_Log = True
                        input_text = ''
                        Last_Page = 'Page6_Log'
                        if Was_Reset == False:
                            Audio3.play()
                        else:
                            Audio4.play()
                if Page6_Log == True:
                    if Name_Click == True:
                        if input_text == Player_name:
                            Name_Click = False
                            N_N = True
                            input_text = ''
                    if Password_Click == True:
                        if input_text == Password:
                            P_N = True
                            Password_Click = False
                            input_text = ''

            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                if len(input_text) < 10:
                    input_text += event.unicode


    HALF_WIDTH = WINDOW_WIDTH // 2
    HALF_HEIGHT = WINDOW_HEIGHT // 2

    if Save_Find == 'Page1' and Start == True:
        Page1 = True
        Start = False
        First_Time = True

    if Save_Find == 'Page6_Log' and Pass == True:
        Page6_Log = True
        Pass = False

    if need_to_update_screen == True and pass_2 == True or pass_3 == True and need_to_update_screen == True:
        WINDOW_WIDTH = 1200
        WINDOW_HEIGHT = 800
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pass_2 = False
        pass_3 = False
    pygame.display.set_icon(ICON)
    pygame.display.set_caption(NAME)

    def width_Money(num, letter_width=20,window_width=1200, icon_width=20):
        len_Num = len(num)
        money_pos = window_width - icon_width - len_Num * letter_width
        return money_pos

    def print_text(message, x, y, font_color=(0, 0, 0), font_type="font/font.ttf", font_size=30):
        font_type = pygame.font.Font(font_type, font_size)
        text = font_type.render(message, True, font_color)
        screen.blit(text, (x, y))

    B_Bucks_x = width_Money(str(B_Bucks))
    Ultra_B_Bucks_x = width_Money(str(Ultra_B_Bucks))
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()
    sec_now = datetime.datetime.today().second
    min_now = datetime.datetime.today().minute

    if Tr_Fl == True:
        sec_Con = datetime.datetime.today().second
        ConncretTime = sec_Con + 14
        if ConncretTime > 60:
            ConncretTime = ConncretTime - 60
        Tr_Fl = False


    if T_N == 1:
        need_input = True

    if Ultra_B_Bucks == 10000000 and Ultra_B_Bucks == 1000000000:
        Your_status = 'Богач'
    elif Ultra_B_Bucks == 100000 and Ultra_B_Bucks == 10000000:
        Your_status = 'На хлеб хватит'
    elif B_Bucks == 1000000 and B_Bucks == 10000000:
        Your_status = 'Бедный Богач'
    elif B_Bucks == 10000 and Ultra_B_Bucks == 100:
        Your_status = 'Бомжык'
    elif Ultra_B_Bucks == 1000 and Ultra_B_Bucks == 10000:
        Your_status = 'Нищий'
    elif Ultra_B_Bucks == 100:
        Your_status = 'Нищий'
    elif B_Bucks or Ultra_B_Bucks == 100000000:
        Your_status = 'МИЛИОРДЕР'
    else:
        Your_status = 'Зарабатывай'

    if Page1 == True:
        Seven_one = True
        Last_Page_File = open('logins/Log_S.dll', 'w')
        Last_Page_File.write(f"fv6tyb6gt252rrh8jmiok9em,9ftr9fdhytr<{Player_name},{Password},Page1,{this_level},{B_Bucks},{Ultra_B_Bucks},{Your_status}>hijmnudtbf7ctgt7n6gm7f6r,sy8r,sy9gh8,sy8slyhgy7hk,0w8syl0,.,f.t,f.t,.,.,.se,.r,f.,t.f,t.,f.t,.")
        Last_Page_File.close()
        Last_Page = 'Page1'
        WINDOW_WIDTH = 500
        WINDOW_HEIGHT = 500
        active = button_font.render('Active', True, pygame.Color(Col_Font))
        next = button_font.render('NEXT', True, pygame.Color(RED))
        button_next = pygame.Rect(0, 0, 400, 150)
        button_active = pygame.Rect(0, 0, 400, 150)
        button_next.center = HALF_WIDTH, HALF_HEIGHT
        button_active.center = HALF_WIDTH, HALF_HEIGHT - 170

        pygame.draw.rect(screen, BLACK, button_next, border_radius=25, width=10)
        screen.blit(next, (button_next.centerx - 85, button_next.centery - 70))
        pygame.draw.rect(screen, Col_Active, button_active, border_radius=25, width=10)
        screen.blit(active, (button_active.centerx - 130, button_active.centery - 70))

        if button_active.collidepoint(mouse_pos):
            screen.blit(active, (button_active.centerx - 130, button_active.centery - 70))
            if mouse_click[0]:
                time.sleep(0.1)
                Col_Active = LIGHT_GREEN
                Col_Font = LIGHT_GREEN
                activ_Btt = activ_Btt + 1

        if activ_Btt == 2:
            Col_Active = RED
            Col_Font = RED
            activ_Btt = 0


        if activ_Btt == 1:
            if button_next.collidepoint(mouse_pos):
                screen.blit(next, (button_next.centerx - 85, button_next.centery - 70))
                if mouse_click[0]:
                    Page1 = False
                    Page2 = True
    elif Page2 == True:
        Tr_Fl = True
        Audio1.play()
        Page2 = False
        Page3 = True
    elif Page3 == True:
        screen.blit(img_One, (0, 0), (x % WINDOW_HEIGHT, WINDOW_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT))
        x += 1
        if sec_now == ConncretTime:
            Page3 = False
            Page4 = True
    elif Page4 == True:
        screen.fill(BLACK)
        T_N += 1
        print_text("Напиши свое Имя", 45,50, font_size=40, font_color=RED)
    elif Page5_Reg == True:
        WINDOW_WIDTH = 1200
        WINDOW_HEIGHT = 800
        need_to_update_screen = True
        screen.blit(menu_picture, (0, 0), (x % WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT))
        NAME = f'Привет {Player_name}'
        x += 1
        print_text(f'Привет {Player_name}', 400,100, font_size=60,font_color=WHITE)
        print_text("Пароль", 250 - 50, 500, font_color=ORANGE)
        need_input = True
    elif Page6_Log == True and Was_Reset == False:
        need_to_update_screen = True
        NAME = f'Привет {Player_name}'
        ICON = pygame.image.load("img/os/ICON_Main.png")
        Last_Page_File = open('logins/Log_S.dll', 'w')
        Last_Page_File.write(f"fv6tyb6gt252rrh8jmiok9em,9ftr9fdhytr<{Player_name},{Password},Page6_Log,{this_level},{B_Bucks},{Ultra_B_Bucks},{Your_status}>hijmnudtbf7ctgt7n6gm7f6r,sy8r,sy9gh8,sy8slyhgy7hk,0w8syl0,.,f.t,f.t,.,.,.se,.r,f.,t.f,t.,f.t,.")
        Last_Page_File.close()
        screen.blit(menu_picture, (0, 0), (x % WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT))
        x += 1
        Password_Enter = button_font.render('Password', True, pygame.Color(WHITE))
        Name_Enter = button_font.render('Name', True, pygame.Color(WHITE))
        button_Enter_Name = pygame.Rect(0, 0, 500, 150)
        button_Enter_Password = pygame.Rect(0, 0, 500, 150)
        button_Enter_Name.center = 250, 250
        button_Enter_Password.center = 250, 250 - 170
        screen.blit(Name_Enter, (button_Enter_Name.centerx - 130, button_Enter_Name.centery - 70))
        if button_Enter_Name.collidepoint(mouse_pos):
            if mouse_click[0]:
                need_input = True
                Name_Click = True
                Password_Click = False
        screen.blit(Password_Enter, (button_Enter_Password.centerx - 130, button_Enter_Password.centery - 70))
        if button_Enter_Password.collidepoint(mouse_pos):
            if mouse_click[0]:
                need_input = True
                Name_Click = False
                Password_Click = True
        if N_N and P_N == True and Page6_Log == True:
            Page6_Log = False
            Page7_menu = True
            if First_Time == True:
                Audio4.play()
    elif Was_Reset == True and Seven_one == True:
        Page7_menu = True
        Seven_one = False
    if Page7_menu == True:
        ICON = pygame.image.load("img/os/ICON_Main.png")
        Last_Page_File = open('logins/Log_S.dll', 'w')
        Last_Page_File.write(f"fv6tyb6gt252rrh8jmiok9em,9ftr9fdhytr<{Player_name},{Password},Page6_Log,{this_level},{B_Bucks},{Ultra_B_Bucks},{Your_status}>hijmnudtbf7ctgt7n6gm7f6r,sy8r,sy9gh8,sy8slyhgy7hk,0w8syl0,.,f.t,f.t,.,.,.se,.r,f.,t.f,t.,f.t,.")
        Last_Page_File.close()

        if Audio4_One == True and First_Time == False:
            Audio4_Sec.play(0)
            Audio4_One = False
        NAME = f'Привет {Player_name}'
        screen.blit(menu_picture, (0, 0), (x % WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT))
        x += 1
        screen.blit(icon_B_bucks_img, (1180, 0))
        screen.blit(icon_Ultra_B_bucks_img, (1180, 32))
        print_text(str(B_Bucks), B_Bucks_x, 30 ,font_color= WHITE)
        print_text(str(Ultra_B_Bucks), Ultra_B_Bucks_x, -3, font_color=WHITE)
        print_text(Your_status,500, 0, font_color=WHITE)
        Play = button_font.render('Play', True, pygame.Color(WHITE))
        Settings = button_font.render('Settings', True, pygame.Color(WHITE))
        Reset = button_font.render('Reset', True, pygame.Color(WHITE))
        #
        button_Play = pygame.Rect(0, 0, 400, 150)
        button_Settings = pygame.Rect(0, 0, 500, 150)
        button_Reset = pygame.Rect(0, 0, 450, 150)
        #
        button_Play.center = HALF_WIDTH, HALF_HEIGHT - 150
        button_Settings.center = HALF_WIDTH, HALF_HEIGHT
        button_Reset.center = HALF_WIDTH, HALF_HEIGHT + 250

        screen.blit(Play, (button_Play.centerx - 85, button_Play.centery - 70))
        screen.blit(Settings, (button_Settings.centerx - 150, button_Settings.centery - 70))
        screen.blit(Reset, (button_Reset.centerx - 110, button_Reset.centery - 70))


        if button_Play.collidepoint(mouse_pos):
            pygame.draw.rect(screen, WHITE, button_Play, border_radius=25, width=10)
            if mouse_click[0]:
                Page8_Play = True
        if button_Settings.collidepoint(mouse_pos):
            pygame.draw.rect(screen, WHITE, button_Settings, border_radius=25, width=10)
            if mouse_click[0]:
                pass
        if button_Reset.collidepoint(mouse_pos):
            pygame.draw.rect(screen, WHITE, button_Reset, border_radius=25, width=10)
            if mouse_click[0]:
                Page7_menu = False
                Page9_Reset = True

    if Page8_Play == True:
        Last_Page_File = open('logins/Log_S.dll', 'w')
        Last_Page_File.write(f"fv6tyb6gt252rrh8jmiok9em,9ftr9fdhytr<{Player_name},{Password},Page6_Log,{this_level},{B_Bucks},{Ultra_B_Bucks},{Your_status}>hijmnudtbf7ctgt7n6gm7f6r,sy8r,sy9gh8,sy8slyhgy7hk,0w8syl0,.,f.t,f.t,.,.,.se,.r,f.,t.f,t.,f.t,.")
        Last_Page_File.close()
        screen.blit(img_Field, (0, 0))
        if this_level == 1:
            if Page8_Play == True and your_turn == True and x_T == 0 and x_T == 4:
                screen.blit(You, (x_Player, y_Player))
                ICON = pygame.image.load("img/os/ICON_Main.png")
                if keys[pygame.K_LEFT]:
                    x_T -= 1
                    time.sleep(0.1)
                if keys[pygame.K_RIGHT]:
                    x_T += 1
                    time.sleep(0.1)
                if keys[pygame.K_DOWN]:
                    y_T -= 1
                    time.sleep(0.1)
                if keys[pygame.K_UP]:
                    y_T += 1
                    time.sleep(0.1)

            if x_T == 0:
                x_Player = 243
            elif x_T == 1:
                x_Player = 243 + 137
            elif x_T == 2:
                x_Player = 243 + 137 + 137
            elif x_T == 3:
                x_Player = 654
            elif x_T == 4:
                x_Player = 243 + 137 + 137 + 137 + 137
            if x_T >= 4:
                x_T = 4
            if x_T <= 0:
                x_T = 0
            if y_T == 0:
                y_Player = 800 - 99
            if y_T == 1:
                y_Player = 800 - (86 + 99)
            if y_T == 2:
                y_Player = 800 - (86 + 86 + 99)
            if y_T == 3:
                y_Player = 800 - (86 + 86 + 86 + 99)
            if y_T > 3:
                player_win = True
                Audio_6_Win_2.play()
                y_T = 0
            if y_T <= 0:
                y_T = 0
            if q_Next == True and player_win == True:
                ICON = pygame.image.load("img/os/ICON_Main.png")
                screen.blit(menu_picture, (0, 0), (x % WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT))
                x += 1
                Next = button_font.render('NEXT ', True, pygame.Color(GREEN))
                Back2 = button_font.render('Back', True, pygame.Color(RED))
                #
                Next_Button = pygame.Rect(0, 0, 450, 150)
                button_Back2 = pygame.Rect(0, 0, 400, 150)
                #
                Next_Button.center = HALF_WIDTH, HALF_HEIGHT
                button_Back2.center = HALF_WIDTH, HALF_HEIGHT - 300
                #
                screen.blit(Next, (Next_Button.centerx - 110, Next_Button.centery - 70))
                screen.blit(Back2, (button_Back2.centerx - 100, button_Back2.centery - 70))
                #
                if Next_Button.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, RED, Next_Button, border_radius=25, width=10)
                    if mouse_click[0]:
                        this_level = 2
                        Audio_6_Win_3.play()
                        player_win = False
                if button_Back2.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, RED, button_Back2, border_radius=25, width=10)
                    if mouse_click[0]:
                        q_Next = False
                        player_win = False
                        Page6_Log = True
        if this_level == 2:
            screen.fill(BLACK)
            screen.blit(img_Field, (0, 0))
            screen.blit(You, (x_Player, y_Player))
            if keys[pygame.K_LEFT]:
                x_T -= 1
                time.sleep(0.1)
                your_turn = False
                enemy_turn = True
            if keys[pygame.K_RIGHT]:
                x_T += 1
                time.sleep(0.1)
                your_turn = False
                enemy_turn = True
            if keys[pygame.K_DOWN]:
                y_T -= 1
                time.sleep(0.1)
                your_turn = False
                enemy_turn = True
            if keys[pygame.K_UP]:
                y_T += 1
                time.sleep(0.1)
                your_turn = False
                enemy_turn = True
            if x_T == 0:
                x_Player = 243
            elif x_T == 1:
                x_Player = 243 + 137
            elif x_T == 2:
                x_Player = 243 + 137 + 137
            elif x_T == 3:
                x_Player = 654
            elif x_T == 4:
                x_Player = 243 + 137 + 137 + 137 + 137
            if x_T >= 4:
                x_T = 4
            if x_T <= 0:
                x_T = 0
            if y_T == 0:
                y_Player = 800 - 99
            if y_T == 1:
                y_Player = 800 - (86 + 99)
            if y_T == 2:
                y_Player = 800 - (86 + 86 + 99)
            if y_T == 3:
                y_Player = 800 - (86 + 86 + 86 + 99)
            if y_T > 3:
                player_win = True
                Audio_6_Win_3.play()
                y_T = 0
            if y_T <= 0:
                y_T = 0
            if enemy_turn == True and step == 1:
                pass
            if q_Next == True and player_win == True:
                ICON = pygame.image.load("img/os/ICON_Main.png")
                screen.blit(menu_picture, (0, 0), (x % WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT))
                x += 1
                Next = button_font.render('NEXT ', True, pygame.Color(GREEN))
                Back2 = button_font.render('Back', True, pygame.Color(RED))
                #
                Next_Button = pygame.Rect(0, 0, 450, 150)
                button_Back2 = pygame.Rect(0, 0, 400, 150)
                #
                Next_Button.center = HALF_WIDTH, HALF_HEIGHT
                button_Back2.center = HALF_WIDTH, HALF_HEIGHT - 300
                #
                screen.blit(Next, (Next_Button.centerx - 110, Next_Button.centery - 70))
                screen.blit(Back2, (button_Back2.centerx - 100, button_Back2.centery - 70))
                #
                if Next_Button.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, RED, Next_Button, border_radius=25, width=10)
                    if mouse_click[0]:
                        this_level = 3
                        player_win = False
                if button_Back2.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, RED, button_Back2, border_radius=25, width=10)
                    if mouse_click[0]:
                        q_Next = False
                        player_win = False
                        Page7_menu = True

    if player_win == True:
        q_Next = True
    else:
        q_Next = False
    if Page9_Reset == True:
        ICON = pygame.image.load("img/os/ICON_Main.png")
        screen.blit(menu_picture, (0, 0), (x % WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT))
        x += 1
        Reset_B = button_font.render('Reset', True, pygame.Color(WHITE))
        Back = button_font.render('Back', True, pygame.Color(RED))
        #
        button_Reset_B = pygame.Rect(0, 0, 450, 150)
        button_Back = pygame.Rect(0, 0, 400, 150)
        #
        button_Reset_B.center = HALF_WIDTH, HALF_HEIGHT
        button_Back.center = HALF_WIDTH, HALF_HEIGHT - 300
        #
        screen.blit(Reset_B, (button_Reset_B.centerx - 110, button_Reset_B.centery - 70))
        screen.blit(Back, (button_Back.centerx - 100, button_Back.centery - 70))
        #
        print_text("Нажимая Эту Кнопку", HALF_WIDTH - 300, HALF_HEIGHT - 180, font_color=WHITE, font_size=50)
        print_text("Ты начнешь с начала", HALF_WIDTH - 120, HALF_HEIGHT + 100, font_color=WHITE)
        print_text("Весь прогрес будет уничтожен тогда", HALF_WIDTH - 200, HALF_HEIGHT + 200, font_color=WHITE)
        print_text("ты сможешь ввести новый Пароль и имя", HALF_WIDTH - 300, HALF_HEIGHT + 300, font_color=WHITE)
        #
        if button_Reset_B.collidepoint(mouse_pos):
            pygame.draw.rect(screen, WHITE, button_Reset_B, border_radius=25, width=10)
            if mouse_click[0]:
                Last_Page_File = open('logins/Log_S.dll', 'w')
                Last_Page_File.write(f"fv6tyb6gt252rrh8jmiok9em,9ftr9fdhytr<{Player_name},{Password},Page1,{this_level},{B_Bucks},{Ultra_B_Bucks},{Your_status}>hijmnudtbf7ctgt7n6gm7f6r,sy8r,sy9gh8,sy8slyhgy7hk,0w8syl0,.,f.t,f.t,.,.,.se,.r,f.,t.f,t.,f.t,.")
                Last_Page_File.close()
                Page9_Reset = False
                Page1 = True
                Start = True
                First_Time = True
                Was_Reset = True
        if button_Back.collidepoint(mouse_pos):
            pygame.draw.rect(screen, RED, button_Back, border_radius=25, width=10)
            if mouse_click[0]:
                Page9_Reset = False
                Page7_menu = True

    if Page4 == False:
        T_N = 0
    if need_input == True and Page6_Log == True and Name_Click == True:
        print_text(input_text, 250 + 200, 250 - 40, font_size=50, font_color=WHITE)
    if need_input == True and Page6_Log == True and Password_Click == True:
        print_text(input_text, 250 + 350, 250 - 210, font_size=50, font_color=WHITE)


    if need_input == True and Page4 == True:
        print_text(input_text, 225,250, font_color=WHITE)
    if need_input == True and Page5_Reg == True:
        print_text(input_text, 250 + 200, 500, font_color=WHITE)

    pygame.display.flip()
    clock.tick(FPS)
