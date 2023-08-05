import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определение размеров окна
WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 6
BOARD_SIZE = 3

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Создание игровой доски
board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крестики-нолики")


def draw_board():
    # Очистка экрана
    screen.fill(WHITE)

    # Рисование вертикальных линий
    for x in range(1, BOARD_SIZE):
        pygame.draw.line(screen, BLACK, (x * WIDTH // BOARD_SIZE, 0),
                         (x * WIDTH // BOARD_SIZE, HEIGHT), LINE_WIDTH)

    # Рисование горизонтальных линий
    for y in range(1, BOARD_SIZE):
        pygame.draw.line(screen, BLACK, (0, y * HEIGHT // BOARD_SIZE),
                         (WIDTH, y * HEIGHT // BOARD_SIZE), LINE_WIDTH)

    # Рисование крестиков и ноликов
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if board[x][y] == 'X':
                pygame.draw.line(screen, BLACK, (x * WIDTH // BOARD_SIZE, y * HEIGHT // BOARD_SIZE),
                                 ((x + 1) * WIDTH // BOARD_SIZE, (y + 1) * HEIGHT // BOARD_SIZE), 2)
                pygame.draw.line(screen, BLACK, ((x + 1) * WIDTH // BOARD_SIZE, y * HEIGHT // BOARD_SIZE),
                                 (x * WIDTH // BOARD_SIZE, (y + 1) * HEIGHT // BOARD_SIZE), 2)
            elif board[x][y] == 'O':
                pygame.draw.circle(screen, BLACK,
                                   (x * WIDTH // BOARD_SIZE + WIDTH // (2 * BOARD_SIZE),
                                    y * HEIGHT // BOARD_SIZE + HEIGHT // (2 * BOARD_SIZE)),
                                   WIDTH // (2 * BOARD_SIZE) - 2, 2)

    # Обновление экрана
    pygame.display.flip()


def check_draw():
    # Проверка на ничью
    for row in board:
        if '' in row:
            return False
    return True


def check_win(player):
    # Проверка на победу в строках
    for row in board:
        if set(row) == {player}:
            return True

    # Проверка на победу в столбцах
    for col in range(BOARD_SIZE):
        if set([board[row][col] for row in range(BOARD_SIZE)]) == {player}:
            return True

    # Проверка на победу по диагоналям
    if set([board[i][i] for i in range(BOARD_SIZE)]) == {player} or \
            set([board[i][BOARD_SIZE - 1 - i] for i in range(BOARD_SIZE)]) == {player}:
        return True

    return False


player_turn = 'X'
game_over = False

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            x = mouse_x // (WIDTH // BOARD_SIZE)
            y = mouse_y // (HEIGHT // BOARD_SIZE)

            if board[x][y] == '':
                board[x][y] = player_turn

                if check_win(player_turn):  # Проверка на победу
                    print(f'Игрок {player_turn} победил!')
                    game_over = True
                elif check_draw():  # Проверка на ничью
                    print("Ничья!")
                    game_over = True
                else:
                    player_turn = 'O' if player_turn == 'X' else 'X'
            
                draw_board()

    draw_board()