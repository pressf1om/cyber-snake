# imports
import pygame
import random
import sys
import os
import time
import requests
import pyautogui
from pathlib import Path

# create default
obj_point = None
color = None
best_result = None
best_result_status = None
last_result = None
dirlist = None
count = None
path = None
dist = None
number_song = None
on_music_bool = None
info_in_file_music = None
x = None
y = None
x_ = None
y_ = None
total_number_of_points = None
info_in_file_total_point = None
purchased_skins = []
non_purchased_skins = []


# my_skin.txt
def write_s():
    # read
    path_skin = 'skins/my_skin.txt'
    f_read_my_skin = open(path_skin, 'w')
    f_read_my_skin.write(str(purchased_skins))
    f_read_my_skin.write(str('\n'))
    f_read_my_skin.write(str(non_purchased_skins))


# init
pygame.init()
pygame.font.init()

# settings
screen_size_mode = width, height = 1000, 800
screen_size = 800
cell = 40
is_received_score = 0
clock = pygame.time.Clock()
fps = 12  # 15 is normal but not slow
score = pygame.font.Font(None, 30)
lose_game = pygame.font.Font(None, 70)
pause_game = pygame.font.Font(None, 100)

# snake pos
obj_x = random.randrange(0, screen_size, cell)
obj_y = random.randrange(0, screen_size, cell)

# point
obj_point = random.randrange(0, screen_size, cell), random.randrange(0, screen_size, cell)

# default snake
len_snake = 1
obj_snake = [(obj_x, obj_y)]
eaten_points = 0

# direction of movement snake (default)
obj_navigator_x = 0
obj_navigator_y = 0

# set screen
pygame.display.set_caption('CyberSnake 3088')
screen = pygame.display.set_mode(screen_size_mode)

# graphics
# heads
image_head_snake_cyber = pygame.image.load('made_graphics/heads/head.png')
image_head_snake_rage = pygame.image.load('made_graphics/heads/custom_rage_theme.png')
image_head_snake_SSSR = pygame.image.load('made_graphics/heads/sssr_them.png')
image_head_snake_classic = pygame.image.load('made_graphics/heads/standart.png')

# other
image_choose_skins = pygame.image.load('made_graphics/other/choose_head_snake_v2.png')
fon_ = pygame.image.load('made_graphics/other/fon.png')
settings_music = pygame.image.load('made_graphics/other/settings.png')
image_rules = pygame.image.load('made_graphics/other/rules.png')

# points
image_point_cyber = pygame.image.load('made_graphics/points/point.png')
image_point_apple = pygame.image.load('made_graphics/points/point_apple.png')
image_point_for_rage = pygame.image.load('made_graphics/points/point_for_rage.png')
image_point_for_ussr = pygame.image.load('made_graphics/points/ussr_point.png')

# create flags for skins
cyber_snake = 1
rage = 2
classic = 3
ussr = 4


# check purchased skins
def check_purchased_skins():
    # init global
    global cyber_snake
    global rage
    global classic
    global ussr

    # read
    f_read_cyber_snake = open('skins/oll skins/cybersnake.txt')
    f_read_rage = open('skins/oll skins/rage.txt')
    f_read_classic = open('skins/oll skins/classic.txt')
    f_read_ussr = open('skins/oll skins/ussr.txt')
    info_in_file_cyber_snake = f_read_cyber_snake.read()
    info_in_file_rage = f_read_rage.read()
    info_in_file_classic = f_read_classic.read()
    info_in_file_ussr = f_read_ussr.read()

    # check cyber snake
    if info_in_file_cyber_snake == '1':
        purchased_skins.append(cyber_snake)
    elif info_in_file_cyber_snake == '0':
        non_purchased_skins.append(cyber_snake)

    # check rage
    if info_in_file_rage == '1':
        purchased_skins.append(rage)
    elif info_in_file_rage == '0':
        non_purchased_skins.append(rage)

    # check rage
    if info_in_file_classic == '1':
        purchased_skins.append(classic)
    elif info_in_file_classic == '0':
        non_purchased_skins.append(classic)

    # check rage
    if info_in_file_ussr == '1':
        purchased_skins.append(ussr)
    elif info_in_file_ussr == '0':
        non_purchased_skins.append(ussr)

    print(f'Purchased skins: {purchased_skins}')
    print(f'Non purchased skins: {non_purchased_skins}')

    # start func
    write_s()


# start func
check_purchased_skins()


# ---------------------------------------------------------------------------------------- (skins)


# background skin
def background_skin():
    # background colour
    screen.fill(pygame.Color('#2d2d2d'))


# custom head snake
def skin_head_player():
    # init global
    global cyber_snake
    global rage
    global classic
    global ussr

    # custom head snake
    f_read = open('skins/choose_skin.txt')

    # read
    info_in_file = f_read.read()

    # check
    if info_in_file == '1':
        if cyber_snake in purchased_skins:
            screen.blit(image_head_snake_cyber, (obj_x, obj_y))
            print('Have')
        elif cyber_snake not in purchased_skins:
            screen.blit(image_head_snake_cyber, (obj_x, obj_y))
            print('Have not')
    if info_in_file == '2':
        if rage in purchased_skins:
            screen.blit(image_head_snake_rage, (obj_x, obj_y))
            print('Have')
        elif rage not in purchased_skins:
            screen.blit(image_head_snake_cyber, (obj_x, obj_y))
            print('Have not')
    if info_in_file == '3':
        if classic in purchased_skins:
            screen.blit(image_head_snake_classic, (obj_x, obj_y))
            print('Have')
        elif classic not in purchased_skins:
            screen.blit(image_head_snake_cyber, (obj_x, obj_y))
            print('Have not')
    if info_in_file == '4':
        if ussr in purchased_skins:
            screen.blit(image_head_snake_SSSR, (obj_x, obj_y))
            print('Have')
        elif ussr not in purchased_skins:
            screen.blit(image_head_snake_cyber, (obj_x, obj_y))
            print('Have not')


# custom body snake
def custom_body_player():
    # init global
    global color

    # custom body snake
    f_read = open('skins/choose_skin.txt')

    # read
    info_in_file_ = f_read.read()

    # check
    if info_in_file_ == '1':
        if cyber_snake in purchased_skins:
            color = pygame.Color('#178592')
            print('Have')
        elif cyber_snake not in purchased_skins:
            color = pygame.Color('#178592')
            print('Have not')
    if info_in_file_ == '2':
        if rage in purchased_skins:
            color = pygame.Color('#c8385a')
            print('Have')
        elif rage not in purchased_skins:
            color = pygame.Color('#178592')
            print('Have not')
    if info_in_file_ == '3':
        if classic in purchased_skins:
            color = pygame.Color('#228b22')
            print('Have')
        elif classic not in purchased_skins:
            color = pygame.Color('#178592')
            print('Have not')
    if info_in_file_ == '4':
        if ussr in purchased_skins:
            color = pygame.Color('#fa0000')
            print('Have')
        elif ussr not in purchased_skins:
            color = pygame.Color('#178592')
            print('Have not')


# start func
custom_body_player()


# custom point
def custom_point():
    # custom point for classic
    f_read = open('skins/choose_skin.txt')

    # read
    info_in_file = f_read.read()

    # custom point check
    if info_in_file == '1':
        if cyber_snake in purchased_skins:
            screen.blit(image_point_cyber, (*obj_point, cell, cell))
            print('Have')
        elif cyber_snake not in purchased_skins:
            screen.blit(image_point_cyber, (*obj_point, cell, cell))
            print('Have not')
    if info_in_file == '2':
        if rage in purchased_skins:
            screen.blit(image_point_for_rage, (*obj_point, cell, cell))
            print('Have')
        elif rage not in purchased_skins:
            screen.blit(image_point_cyber, (*obj_point, cell, cell))
            print('Have not')
    if info_in_file == '3':
        if classic in purchased_skins:
            screen.blit(image_point_apple, (*obj_point, cell, cell))
            print('Have')
        elif classic not in purchased_skins:
            screen.blit(image_point_cyber, (*obj_point, cell, cell))
            print('Have not')
    if info_in_file == '4':
        if ussr in purchased_skins:
            screen.blit(image_point_for_ussr, (*obj_point, cell, cell))
            print('Have')
        elif ussr not in purchased_skins:
            screen.blit(image_point_cyber, (*obj_point, cell, cell))
            print('Have not')


# ---------------------------------------------------------------------------------------- (skins)


# terminate
def terminate():
    pygame.quit()
    sys.exit()


# start
def start_screen():
    intro_text = ["Cyber shake"]
    intro_text1 = [
        "The classic game (easy) (press 1)",
        "Match making (for experienced players) (press 2)",
        "Settings (press U)",
        "Skins (press I)",
        "Rules (press O)"
    ]

    # background
    fon = pygame.transform.scale(fon_, (width, height))
    screen.blit(fon, (0, 0))
    font1 = pygame.font.Font(None, 45)
    font2 = pygame.font.Font(None, 120)
    text_coord1 = 50

    # text
    for line in intro_text:
        string_rendered2 = font2.render(line, 1, pygame.Color('#50c878'))
        intro_rect = string_rendered2.get_rect()
        text_coord1 += 5
        intro_rect.top = text_coord1
        intro_rect.x = 60
        text_coord1 += intro_rect.height
        screen.blit(string_rendered2, intro_rect)

    # text
    for line1 in intro_text1:
        string_rendered1 = font1.render(line1, 1, pygame.Color('#50c878'))
        intro_rect1 = string_rendered1.get_rect()
        text_coord1 += 5
        intro_rect1.top = text_coord1
        intro_rect1.x = 60
        text_coord1 += intro_rect1.height
        screen.blit(string_rendered1, intro_rect1)

    # wait move from user
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(fps)


# screen for best result
def get_screenshot(path_):
    pyautogui.screenshot(path_ + '.png')
    print(f'screenshot in {path_}')


# save result
def write_point():
    # init global
    global last_result

    # read
    path_mmr = 'mm/mmr.txt'
    f___ = open(path_mmr)
    last_result = f___.read()

    # if
    if int(last_result) < is_received_score:
        f___ = open(path_mmr, 'w')
        f___.write(str(is_received_score))
        print('record')
    elif int(last_result) == is_received_score:
        print('==============')
    elif int(last_result) > is_received_score:
        print('NOT WRITED')


# best result
def best():
    # init global
    global best_result
    global best_result_status
    global last_result

    print(is_received_score)
    print(last_result)

    # if
    if int(last_result) < is_received_score:
        best_result = is_received_score
        print('screenshot is will made')
        best_result_status = True
    else:
        best_result = last_result
        best_result_status = False

    return best_result_status


# now result
def now():
    return is_received_score


# total number of points
def get_total_points():
    # init global
    global info_in_file_total_point

    # read
    f_read_total = open('mm/total_point.txt')
    info_in_file_total_point = (f_read_total.read())

    # ###
    print(info_in_file_total_point)

    # ###
    return info_in_file_total_point


# on music
def music_is_on():
    # init global
    global info_in_file_music

    # read
    f_read_music = open('music/info.txt')
    info_in_file_music = f_read_music.read()

    # check
    if info_in_file_music == '0':
        # ###
        print('Music off')
    if info_in_file_music == '1':
        # init
        pygame.mixer.init()

        # load music
        pygame.mixer.music.load('D:\\pythonProject\\main\\music\\music sorse\\Alan Walker Faded.mp3')

        # play
        pygame.mixer.music.play()

        # ###
        print('Music on')


# end for easy game
def end_for_ez():
    # init globals
    global best_result_status
    global info_in_file_music

    # now func
    now()

    # check
    if info_in_file_music == '1':
        # load music
        pygame.mixer.music.load('D:\\pythonProject\\main\\music\\music sorse\\retro end.mp3')

        # play
        pygame.mixer.music.play()
    else:
        print('Off')

    # main loop
    while True:
        # set display
        background_skin()
        lose_message = lose_game.render('You lose (((', 1, pygame.Color(color))
        lose_message_about_try_again = lose_game.render('Try again!', 1, pygame.Color(color))
        screen.blit(lose_message, (350, 300))
        screen.blit(lose_message_about_try_again, (350, 350))
        pygame.draw.rect(screen, color, (300, 280, 345, 140), 5)

        # update
        pygame.display.flip()

        # check event
        for event in pygame.event.get():
            # check event type
            if event.type == pygame.QUIT:
                sys.exit()


# end for hard game
def end():
    # init globals
    global best_result_status
    global info_in_file_music
    global x
    global y
    global x_
    global y_

    # check best func
    best()

    # now func
    now()

    # check
    if info_in_file_music == '1':
        # load music
        pygame.mixer.music.load('D:\\pythonProject\\main\\music\\music sorse\\retro end.mp3')

        # play
        pygame.mixer.music.play()
    else:
        print('Off')

    # main loop
    while True:
        # set display
        background_skin()
        lose_message = lose_game.render('You lose (((', 1, pygame.Color(color))
        lose_message_about_record = lose_game.render(f'Best result: {best_result}', 1, pygame.Color(color))
        lose_message_about_today_result = lose_game.render(f'Now result: {is_received_score}', 1, pygame.Color(color))
        lose_message_about_try_again = lose_game.render('Try again!', 1, pygame.Color(color))
        screen.blit(lose_message, (350, 250))
        screen.blit(lose_message_about_record, (350, 300))
        screen.blit(lose_message_about_today_result, (350, 350))
        screen.blit(lose_message_about_try_again, (350, 400))
        if int(best_result) < 10:
            x, y = 337, 230
            x_, y_ = 337, 235
        else:
            x, y = 340, 230
            x_, y_ = 357, 235
        pygame.draw.rect(screen, color, (x, y, x_, y_), 5)

        # update
        pygame.display.flip()

        # get screen or not
        if best_result_status:
            get_screenshot('/best_moments\\record')
            print('screenshot is done')
        else:
            print('Error')

        # check event
        for event in pygame.event.get():
            # check event type
            if event.type == pygame.QUIT:
                sys.exit()


# start func
start_screen()


# Main management
key = pygame.key.get_pressed()

# rules
if key[pygame.K_o]:
    def rules():
        # init
        pygame.init()

        # settings
        size_window_ = width_image_skin_, height_image_skin_ = 1000, 800
        screen_window_ = pygame.display.set_mode(size_window_)

        # stay running true
        running = True

        # main loop
        while running:
            # background
            screen_window_.blit(image_rules, (0, 0))

            # check event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # update
            pygame.display.flip()

    # start func
    rules()

# custom snake
if key[pygame.K_i]:
    # choose skin
    def choose_skin():
        # init
        pygame.init()

        # settings
        size_window = width_image_skin, height_image_skin = 1000, 800
        screen_window = pygame.display.set_mode(size_window)

        # open path
        path_ = "skins/choose_skin.txt"
        f__ = open(path_, 'w')

        # stay running true
        running = True

        # main loop
        while running:
            # background
            screen_window.blit(image_choose_skins, (0, 0))

            # choose
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        # write
                        f__.write('1')
                        print('Selected 1')

                        # del
                        terminate()

                    if event.key == pygame.K_2:
                        # write
                        f__.write('2')
                        print('Selected 2')

                        # del
                        terminate()

                    if event.key == pygame.K_3:
                        # write
                        f__.write('3')
                        print('Selected 3')

                        # del
                        terminate()

                    if event.key == pygame.K_4:
                        # write
                        f__.write('4')
                        print('Selected 4')

                        # del
                        terminate()

            # update
            pygame.display.flip()


    # start func
    choose_skin()

# settings
if key[pygame.K_u]:
    # choose play
    def choose_music():
        # init
        pygame.init()

        # settings
        size_window_ = width_image_music, height_image_music = 1000, 800
        screen_window_ = pygame.display.set_mode(size_window_)

        # open path
        path_info = 'music/info.txt'
        f_ = open(path_info, 'w')

        # main loop
        while True:
            # background
            screen_window_.blit(settings_music, (0, 0))

            # choose
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        # write
                        f_.write('0')
                        print('Selected 0')

                        # del
                        terminate()

                    if event.key == pygame.K_1:
                        # write
                        f_.write('1')
                        print('Selected 1')

                        # del
                        terminate()

            # update
            pygame.display.flip()


    # start func
    choose_music()

# default snake (easy)
if key[pygame.K_1]:
    # start music func
    music_is_on()

    # main loop
    while True:
        # background colour
        background_skin()

        # print received score
        settings_print = score.render(f'Received score: {is_received_score}', 1, pygame.Color('#178592'))
        screen.blit(settings_print, (400, 0))

        # spawn: snake head
        for i, j in obj_snake:
            pygame.draw.rect(screen, color, (i, j, cell, cell))

        # custom head snake
        skin_head_player()

        # spawn: point
        pygame.draw.rect(screen, pygame.Color('#2d2d2d'), (*obj_point, cell, cell))

        # custom point
        custom_point()

        # move
        obj_x += obj_navigator_x * cell
        obj_y += obj_navigator_y * cell

        # add
        obj_snake.append((obj_x, obj_y))
        obj_snake = obj_snake[-len_snake:]

        # check received score
        if obj_snake[-1] == obj_point:
            obj_point = random.randrange(0, screen_size, cell), random.randrange(0, screen_size, cell)
            len_snake += 1
            is_received_score += 1

        # living conditions
        if obj_x > 1000 or obj_y > 800 or obj_x < -40 or obj_y < -40:
            # get i
            i = obj_snake

            # ###
            print(i)

            # start func
            end_for_ez()

        # check event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # FPS
        pygame.display.flip()
        clock.tick(fps)

        # management
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            obj_navigator_x = 0
            obj_navigator_y = -1
        if key[pygame.K_DOWN]:
            obj_navigator_x = 0
            obj_navigator_y = 1
        if key[pygame.K_RIGHT]:
            obj_navigator_x = 1
            obj_navigator_y = 0
        if key[pygame.K_LEFT]:
            obj_navigator_x = -1
            obj_navigator_y = 0

# match making (hard)
if key[pygame.K_2]:
    # start music func
    music_is_on()

    # main loop
    while True:
        # background colour
        background_skin()

        # print received score
        settings_print = score.render(f'Received score: {is_received_score}', 1, pygame.Color('#178592'))
        screen.blit(settings_print, (400, 0))

        # spawn: snake head
        for i, j in obj_snake:
            pygame.draw.rect(screen, color, (i, j, cell, cell))

        # custom head snake
        skin_head_player()

        # spawn: point
        pygame.draw.rect(screen, pygame.Color('#2d2d2d'), (*obj_point, cell, cell))

        # custom point
        custom_point()

        # move
        obj_x += obj_navigator_x * cell
        obj_y += obj_navigator_y * cell

        # add
        obj_snake.append((obj_x, obj_y))
        obj_snake = obj_snake[-len_snake:]

        # check received score
        if obj_snake[-1] == obj_point:
            obj_point = random.randrange(0, screen_size, cell), random.randrange(0, screen_size, cell)
            len_snake += 1
            fps += 1
            is_received_score += 1

        # living conditions
        if obj_x > 1000 or obj_y > 800 or obj_x < -40 or obj_y < -40:
            i = obj_snake
            print(i)
            # start func write
            write_point()

            # check total points
            get_total_points()

            # get total_number_of_points
            total_number_of_points = ((float(int(is_received_score)) / 10) + float(info_in_file_total_point))

            # ###
            print(total_number_of_points)

            # write
            # read
            path_mmr_total = 'mm/total_point.txt'

            # if
            if 1 == 1:
                f = open(path_mmr_total, 'w')
                f.write(str(total_number_of_points))

            # end func
            end()

        # check event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # FPS
        pygame.display.flip()
        clock.tick(fps)

        # management
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            obj_navigator_x = 0
            obj_navigator_y = -1
        if key[pygame.K_DOWN]:
            obj_navigator_x = 0
            obj_navigator_y = 1
        if key[pygame.K_RIGHT]:
            obj_navigator_x = 1
            obj_navigator_y = 0
        if key[pygame.K_LEFT]:
            obj_navigator_x = -1
            obj_navigator_y = 0
