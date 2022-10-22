import copy
import random
import pygame
import sys
from Button import Button
from Text import Text

blue = (8, 13, 43)
yellow = (255, 201, 51)
pink = (255, 51, 187)
sky = (101, 230, 255)

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.mixer.music.load('sound//NEON XO.mp3')
click = pygame.mixer.Sound('sound//click.wav')
pygame.mixer.music.play(-1)
vol = 0.05
pygame.mixer.music.set_volume(vol)
clock = pygame.time.Clock()
w, h = 600, 600
size_block = 200
indent = 5
pygame.display.set_caption('NEON XO')
pygame.display.set_icon(pygame.image.load('images//X.bmp'))
sc = pygame.display.set_mode((w, h))
font = 'font//Madsense.otf'
bg = pygame.image.load("images//Bg.png").convert_alpha()
O = pygame.image.load("images//O.png").convert_alpha()
X = pygame.image.load("images//X.png").convert_alpha()
cross = pygame.image.load("images//Cross.png").convert_alpha()
start_game = Button('START GAME', 380, 100, (110, 440), 10, font, 70, sky, pink, yellow, blue)
play = Button('PLAY VS FRIEND', 380, 100, (110, 200), 10, font, 60, sky, pink, yellow, blue)
play_ai = Button('PLAY VS NEON', 380, 100, (110, 80), 10, font, 60, sky, pink, yellow, blue)
options = Button('OPTIONS', 380, 100, (110, 320), 10, font, 60, sky, pink, yellow, blue)
quit = Button('QUIT', 380, 100, (110, 440), 10, font, 60, sky, pink, yellow, blue)
on = Button('ON', 100, 50, (420, 100), 10, font, 30, sky, pink, yellow, blue)
easy = Button('EASY', 380, 100, (110, 220), 10, font, 60, sky, pink, yellow, blue)
unbeatable = Button('UNBEATABLE', 380, 100, (110, 340), 10, font, 60, sky, pink, yellow, blue)

FPS = 60
field = [[0] * 3 for i in range(3)]
turn = 0
game_over = False
game_vs_ai = False
choose_x = False
first_move = 0
sound_on = True
change_on = True
easy_mode = False


def start():
    alfa = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if start_game.check_pressed():
                        click.play()
                        menu()
        sc.blit(bg, (0, 0))
        if alfa < 255:
            alfa += 2
            O.set_alpha(alfa)
            X.set_alpha(alfa)
        sc.blit(O, (200, 220))
        sc.blit(X, (200, 40))
        start_game.draw(sc, sky)
        pygame.display.flip()
        clock.tick(FPS)


def menu():
    global game_vs_ai
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if play_ai.check_pressed():
                        click.play()
                        game_vs_ai = True
                        difficulty()
                    if play.check_pressed():
                        click.play()
                        choose()
                    elif options.check_pressed():
                        click.play()
                        option()
                    elif quit.check_pressed():
                        click.play()
                        sys.exit()

        sc.blit(bg, (0, 0))
        play.draw(sc, sky)
        play_ai.draw(sc, sky)
        options.draw(sc, sky)
        quit.draw(sc, sky)
        pygame.display.flip()
        clock.tick(FPS)


def option():
    global sound_on, change_on
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    click.play()
                    menu()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if on.check_pressed():
                        click.play()
                        if change_on:
                            on.change_text('OFF')
                            change_on = False
                        else:
                            on.change_text('ON')
                            change_on = True
                        if sound_on:
                            sound_on = False
                            pygame.mixer.music.pause()
                        else:
                            sound_on = True
                            pygame.mixer.music.unpause()
        sc.blit(bg, (0, 0))
        Text('MUSIC', text_color=sky, rect_color=yellow, width=50, height=50,
             font_size=60, font=font, pos=(40, 70)).draw_t(sc)
        on.draw(sc, sky)
        pygame.display.flip()
        clock.tick(FPS)


def difficulty():
    global game_vs_ai, easy_mode
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_vs_ai = False
                    click.play()
                    menu()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if easy.check_pressed():
                        easy_mode = True
                        click.play()
                        choose()
                    elif unbeatable.check_pressed():
                        click.play()
                        choose()
        sc.blit(bg, (0, 0))
        Text('DIFFICULTY', text_color=sky, rect_color=yellow, width=50, height=50,
             font_size=60, font=font, pos=(140, 100)).draw_t(sc)
        unbeatable.draw(sc, sky)
        easy.draw(sc, sky)
        pygame.display.flip()
        clock.tick(FPS)


def choose():
    global choose_x
    pygame.display.flip()
    clock.tick(FPS)
    global turn
    alfa_X = 60
    alfa_O = 60
    reverse = False
    while True:
        X_rect = X.get_rect(topleft=(100, 250))
        O_rect = O.get_rect(topleft=(300, 250))
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    click.play()
                    menu()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if X_rect.collidepoint(pos):
                        click.play()
                        if game_vs_ai:
                            if easy_mode:
                                choose_x = True
                                game_ai()
                            else:
                                choose_x = True
                                game_hard_ai()
                        else:
                            game()
                    elif O_rect.collidepoint(pos):
                        click.play()
                        if game_vs_ai:
                            if easy_mode:
                                game_ai()
                            else:
                                game_hard_ai()
                        else:
                            turn += 1
                            game()
        sc.blit(bg, (0, 0))
        Text('CHOOSE YOUR SIDE', text_color=sky, rect_color=yellow, width=50, height=50,
             font_size=60, font=font, pos=(40, 100)).draw_t(sc)
        sc.blit(X, X_rect)
        sc.blit(O, O_rect)
        X.set_alpha(alfa_X)
        O.set_alpha(alfa_O)
        if X_rect.collidepoint(pos):
            if alfa_X < 255 and not reverse:
                alfa_X += 10
            if alfa_X >= 255:
                reverse = True
            if reverse:
                alfa_X -= 10
            if alfa_X == 60:
                reverse = False
        elif O_rect.collidepoint(pos):
            if alfa_O < 255 and not reverse:
                alfa_O += 10
            if alfa_O >= 255:
                reverse = True
            if reverse:
                alfa_O -= 10
            if alfa_O == 60:
                reverse = False
        else:
            alfa_O = 70
            alfa_X = 70
        pygame.display.flip()
        clock.tick(FPS)


def check_win(field, sign):
    zeroes = 0
    for row in field:
        zeroes += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if field[0][0] == sign and field[1][0] == sign and field[2][0] == sign:
            return sign
        if field[0][1] == sign and field[1][1] == sign and field[2][1] == sign:
            return sign
        if field[0][2] == sign and field[1][2] == sign and field[2][2] == sign:
            return sign
        if field[0][0] == sign and field[1][1] == sign and field[2][2] == sign:
            return sign
        if field[0][2] != sign or field[1][1] != sign or field[2][0] != sign:
            if zeroes == 0:
                return 'PIECE'
            return False
        return sign


def screen_result(text, text_size, x, pos_x):
    s = pygame.Surface((600, 600))
    s.set_alpha(200)
    s.fill(blue)
    sc.blit(s, (0, 0))
    Text(text, text_color=sky, width=50, height=50,
         font_size=text_size, font=font, pos=(x, 100)).draw_t(sc)
    Text('SPACE TO CONTINUE', text_color=pink, width=50, height=50,
         font_size=40, font=font, pos=(pos_x, 200)).draw_t(sc)
    Text('ESC TO MENU', text_color=yellow, width=50, height=50,
         font_size=40, font=font, pos=(pos_x, 230)).draw_t(sc)
    pygame.display.flip()
    clock.tick(FPS)


def hard_ai():
    if choose_x:
        try:
            field[ai_move()[0]][ai_move()[1]] = 'o'
        except IndexError:
            result_ai()
    else:
        try:
            field[ai_move()[0]][ai_move()[1]] = 'x'
        except IndexError:
            result_ai()


def easy_ai():
    if choose_x:
        try:
            x, y = random.randint(0, 2), random.randint(0, 2)
            if field[x][y] != 0:
                x, y = random.randint(0, 2), random.randint(0, 2)
                easy_ai()
            else:
                field[x][y] = 'o'
        except RecursionError:
            result_ai()
    else:
        try:
            x, y = random.randint(0, 2), random.randint(0, 2)
            if field[x][y] != 0:
                x, y = random.randint(0, 2), random.randint(0, 2)
                easy_ai()
            else:
                field[x][y] = 'x'
        except RecursionError:
            result_ai()


def ai_move():
    if choose_x:
        move = []
        best_score = -100
        board = copy.deepcopy(field)
        for x in range(3):
            for y in range(3):
                if board[x][y] == 0:
                    board[x][y] = 'o'
                    score = minimax(board, False)
                    board[x][y] = 0
                    if score > best_score:
                        best_score = score
                        move = (x, y)
        return move
    else:
        move = []
        best_score = -100
        board = copy.deepcopy(field)
        for x in range(3):
            for y in range(3):
                if board[x][y] == 0:
                    board[x][y] = 'x'
                    score = minimax(board, False)
                    board[x][y] = 0
                    if score > best_score:
                        best_score = score
                        move = (x, y)
        return move


def minimax(board, ismax):
    if choose_x:
        if check_win(board, 'x') == 'x':
            return -1
        elif check_win(board, 'o') == 'o':
            return 1
        elif check_win(board, 'o') == 'PIECE':
            return 0
        if ismax:
            best_score = -100
            for x in range(3):
                for y in range(3):
                    if board[x][y] == 0:
                        board[x][y] = 'o'
                        score = minimax(board, False)
                        board[x][y] = 0
                        if score > best_score:
                            best_score = score
        else:
            best_score = 100
            for x in range(3):
                for y in range(3):
                    if board[x][y] == 0:
                        board[x][y] = 'x'
                        score = minimax(board, True)
                        board[x][y] = 0
                        if score < best_score:
                            best_score = score
        return best_score
    else:
        if check_win(board, 'x') == 'x':
            return 1
        elif check_win(board, 'o') == 'o':
            return -1
        elif check_win(board, 'o') == 'PIECE':
            return 0
        if ismax:
            best_score = -100
            for x in range(3):
                for y in range(3):
                    if board[x][y] == 0:
                        board[x][y] = 'x'
                        score = minimax(board, False)
                        board[x][y] = 0
                        if score > best_score:
                            best_score = score
        else:
            best_score = 100
            for x in range(3):
                for y in range(3):
                    if board[x][y] == 0:
                        board[x][y] = 'o'
                        score = minimax(board, True)
                        board[x][y] = 0
                        if score < best_score:
                            best_score = score
        return best_score


def result_ai():
    global game_over
    if choose_x:
        player = check_win(field, 'x')
        neon = check_win(field, 'o')
        if player == 'x':
            game_over = True
            screen_result('X WIN', 130, 110, 110)
        elif neon == 'o':
            screen_result('O WIN', 130, 100, 100)
            game_over = True
        elif player == 'PIECE':
            screen_result('PIECE', 130, 130, 130)
            game_over = True
    else:
        player = check_win(field, 'o')
        neon = check_win(field, 'x')
        if player == 'o':
            screen_result('O WIN', 130, 100, 100)
            game_over = True
        elif neon == 'x':
            game_over = True
            screen_result('X WIN', 130, 110, 110)
        elif player == 'PIECE':
            screen_result('PIECE', 130, 130, 130)
            game_over = True


def game():
    global game_over
    global turn
    global field
    alfa = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    click.play()
                    game_over = False
                    turn = 0
                    field = [[0] * 3 for i in range(3)]
                    menu()
                elif event.key == pygame.K_SPACE:
                    click.play()
                    game_over = False
                    turn = 0
                    field = [[0] * 3 for i in range(3)]
                    choose()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click.play()
                    if not game_over:
                        pos = pygame.mouse.get_pos()
                        col = pos[0] // (size_block + indent)
                        row = pos[1] // (size_block + indent)
                        if field[row][col] == 0:
                            if turn % 2 == 0:
                                field[row][col] = 'x'
                            else:
                                field[row][col] = 'o'
                            turn += 1
        sc.blit(bg, (0, 0))
        if alfa < 255:
            alfa += 5
            cross.set_alpha(alfa)
        sc.blit(cross, (0, 0))
        for row in range(3):
            for col in range(3):
                x = col * size_block + (col + 0) * indent
                y = row * size_block + (row + 0) * indent
                O.set_alpha(0)
                sc.blit(O, (x, y))
                spot = O.get_rect(topleft=(x, y))
                mouse_pos = pygame.mouse.get_pos()
                if spot.collidepoint(mouse_pos) and not game_over:
                    if turn % 2 == 0 and field[row][col] != 'o' and field[row][col] != 'x':
                        X.set_alpha(100)
                        sc.blit(X, spot)
                    elif turn % 2 != 0 and field[row][col] != 'o' and field[row][col] != 'x':
                        O.set_alpha(100)
                        sc.blit(O, spot)
                if field[row][col] == 'x':
                    X.set_alpha(255)
                    sc.blit(X, spot)
                elif field[row][col] == 'o':
                    O.set_alpha(255)
                    sc.blit(O, spot)
        if (turn - 1) % 2 == 0:
            game_over = check_win(field, 'x')
        else:
            game_over = check_win(field, 'o')
        if game_over == 'x':
            screen_result('X WIN', 130, 110, 110)
        if game_over == 'o':
            screen_result('O WIN', 130, 100, 100)
        if game_over == 'PIECE':
            screen_result('PIECE', 130, 130, 130)
        pygame.display.flip()
        clock.tick(FPS)


def game_ai():
    global game_over, game_vs_ai, first_move, choose_x, turn, field, easy_mode
    alfa = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    click.play()
                    game_over = False
                    turn = 0
                    field = [[0] * 3 for i in range(3)]
                    first_move = 0
                    choose_x = False
                    game_vs_ai = False
                    easy_mode = False
                    menu()
                elif event.key == pygame.K_SPACE:
                    click.play()
                    game_over = False
                    turn = 0
                    field = [[0] * 3 for i in range(3)]
                    first_move = 0
                    game_ai()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click.play()
                    if not game_over:
                        if choose_x:
                            pos = pygame.mouse.get_pos()
                            col = pos[0] // (size_block + indent)
                            row = pos[1] // (size_block + indent)
                            if field[row][col] == 0:
                                field[row][col] = 'x'
                                easy_ai()
                        else:
                            pos = pygame.mouse.get_pos()
                            col = pos[0] // (size_block + indent)
                            row = pos[1] // (size_block + indent)
                            if field[row][col] == 0:
                                field[row][col] = 'o'
                            easy_ai()
        if not choose_x and first_move != 1:
            easy_ai()
            first_move += 1
        sc.blit(bg, (0, 0))
        if alfa < 255:
            alfa += 5
            cross.set_alpha(alfa)
        sc.blit(cross, (0, 0))
        for row in range(3):
            for col in range(3):
                x = col * size_block + (col + 0) * indent
                y = row * size_block + (row + 0) * indent
                O.set_alpha(0)
                sc.blit(O, (x, y))
                spot = O.get_rect(topleft=(x, y))
                mouse_pos = pygame.mouse.get_pos()
                if not choose_x:
                    if spot.collidepoint(mouse_pos) and not game_over:
                        if field[row][col] != 'o' and field[row][col] != 'x':
                            O.set_alpha(100)
                            sc.blit(O, spot)
                else:
                    if spot.collidepoint(mouse_pos) and not game_over:
                        if field[row][col] != 'o' and field[row][col] != 'x':
                            X.set_alpha(100)
                            sc.blit(X, spot)
                if field[row][col] == 'x':
                    X.set_alpha(255)
                    sc.blit(X, spot)
                elif field[row][col] == 'o':
                    O.set_alpha(255)
                    sc.blit(O, spot)
        result_ai()
        pygame.display.flip()
        clock.tick(FPS)


def game_hard_ai():
    global game_over, game_vs_ai, first_move, choose_x, turn, field
    alfa = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    click.play()
                    game_over = False
                    turn = 0
                    field = [[0] * 3 for i in range(3)]
                    first_move = 0
                    choose_x = False
                    game_vs_ai = False
                    menu()
                elif event.key == pygame.K_SPACE:
                    click.play()
                    game_over = False
                    turn = 0
                    field = [[0] * 3 for i in range(3)]
                    first_move = 0
                    game_hard_ai()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click.play()
                    if not game_over:
                        if choose_x:
                            pos = pygame.mouse.get_pos()
                            col = pos[0] // (size_block + indent)
                            row = pos[1] // (size_block + indent)
                            if field[row][col] == 0:
                                field[row][col] = 'x'
                            hard_ai()
                        else:
                            pos = pygame.mouse.get_pos()
                            col = pos[0] // (size_block + indent)
                            row = pos[1] // (size_block + indent)
                            if field[row][col] == 0:
                                field[row][col] = 'o'
                            hard_ai()
        if choose_x == False and first_move != 1:
            hard_ai()
            first_move += 1
        sc.blit(bg, (0, 0))
        if alfa < 255:
            alfa += 5
            cross.set_alpha(alfa)
        sc.blit(cross, (0, 0))
        for row in range(3):
            for col in range(3):
                x = col * size_block + (col + 0) * indent
                y = row * size_block + (row + 0) * indent
                O.set_alpha(0)
                sc.blit(O, (x, y))
                spot = O.get_rect(topleft=(x, y))
                mouse_pos = pygame.mouse.get_pos()
                if not choose_x:
                    if spot.collidepoint(mouse_pos) and not game_over:
                        if field[row][col] != 'o' and field[row][col] != 'x':
                            O.set_alpha(100)
                            sc.blit(O, spot)
                else:
                    if spot.collidepoint(mouse_pos) and not game_over:
                        if field[row][col] != 'o' and field[row][col] != 'x':
                            X.set_alpha(100)
                            sc.blit(X, spot)
                if field[row][col] == 'x':
                    X.set_alpha(255)
                    sc.blit(X, spot)
                elif field[row][col] == 'o':
                    O.set_alpha(255)
                    sc.blit(O, spot)
        result_ai()
        pygame.display.flip()
        clock.tick(FPS)


start()
