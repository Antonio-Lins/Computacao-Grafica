import pygame
import math

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Janela de primitivas")

font = pygame.font.SysFont("Arial", 14)

def para_tela(x, y):
    tela_x = WIDTH // 2 + x
    tela_y = HEIGHT // 2 - y
    return tela_x, tela_y

def desenhar_pixel(x, y, cor=(255,255,255)):
    tx, ty = para_tela(x, y)

    if 0 <= tx < WIDTH and 0 <= ty < HEIGHT:
        screen.set_at((tx, ty), cor)

def desenhar_grade():
    espacamento = 20

    for x in range(0, WIDTH, espacamento):
        pygame.draw.line(
            screen,
            (50, 50, 50),
            (x, 0),
            (x, HEIGHT)
        )

    for y in range(0, HEIGHT, espacamento):
        pygame.draw.line(
            screen,
            (50, 50, 50),
            (0, y),
            (WIDTH, y)
        )

def desenhar_eixos():
    pygame.draw.line(
        screen,
        (255, 0, 0),
        (WIDTH // 2, 0),
        (WIDTH // 2, HEIGHT),
        2
    )

    pygame.draw.line(
        screen,
        (255, 0, 0),
        (0, HEIGHT // 2),
        (WIDTH, HEIGHT // 2),
        2
    )

def desenhar_numeros():
    espacamento = 50

    for x in range(-WIDTH // 2, WIDTH // 2 + 1, espacamento):
        if x != 0:
            tx, ty = para_tela(x, 0)
            texto = font.render(str(x), True, (180,180,180))
            screen.blit(texto, (tx - 10, ty + 5))

    for y in range(-HEIGHT // 2, HEIGHT // 2 + 1, espacamento):
        if y != 0:
            tx, ty = para_tela(0, y)
            texto = font.render(str(y), True, (180,180,180))
            screen.blit(
                texto,
                (tx - texto.get_width() - 5, ty - 10)
            )

def desenhar_cenario():
    screen.fill((0,0,0))
    # desenhar_grade()
    desenhar_eixos()
    # desenhar_numeros()

def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    passos = max(abs(dx), abs(dy))

    if passos == 0:
        desenhar_pixel(x1, y1)
        return

    x_inc = dx / passos
    y_inc = dy / passos

    x = x1
    y = y1

    for i in range(passos + 1):
        desenhar_pixel(round(x), round(y))
        x += x_inc
        y += y_inc

def bresenham(x1, y1, x2, y2):
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dx = x2 - x1
    dy = y2 - y1

    p = 2 * dy - dx

    x = x1
    y = y1

    while x <= x2:
        desenhar_pixel(x, y)

        if p <= 0:
            p += 2 * dy
        else:
            y += 1
            p += 2 * dy - 2 * dx

        x += 1

def circunferencia_explicita(xc, yc, r):
    x = 0

    while x <= r:
        y = round(math.sqrt(r**2 - x**2))

        desenhar_pixel(xc + x, yc + y)
        desenhar_pixel(xc - x, yc + y)
        desenhar_pixel(xc + x, yc - y)
        desenhar_pixel(xc - x, yc - y)
        desenhar_pixel(xc + y, yc + x)
        desenhar_pixel(xc - y, yc + x)
        desenhar_pixel(xc + y, yc - x)
        desenhar_pixel(xc - y, yc - x)

        x += 1

def circunferencia_bresenham(xc, yc, r):
    x = 0
    y = r
    p = 1 - r

    while x <= y:
        desenhar_pixel(xc + x, yc + y)
        desenhar_pixel(xc - x, yc + y)
        desenhar_pixel(xc + x, yc - y)
        desenhar_pixel(xc - x, yc - y)
        desenhar_pixel(xc + y, yc + x)
        desenhar_pixel(xc - y, yc + x)
        desenhar_pixel(xc + y, yc - x)
        desenhar_pixel(xc - y, yc - x)

        if p < 0:
            p += 2 * x + 3
        else:
            y -= 1
            p += 2 * (x - y) + 5

        x += 1

def circunferencia_trigonometrica(xc, yc, r):
    angulo = 0

    while angulo <= 360:
        radiano = math.radians(angulo)

        x = round(r * math.cos(radiano))
        y = round(r * math.sin(radiano))

        desenhar_pixel(xc + x, yc + y)

        angulo += 1

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    desenhar_cenario()

    pygame.display.update()
    pygame.event.pump()

    print("\n=========================")
    print("1 - DDA")
    print("2 - Bresenham")
    print("3 - Circunferência Explícita")
    print("4 - Circunferência Trigonométrica")
    print("5 - Circunferência Bresenham")
    print("0 - Sair")
    print("=========================")

    opcao = input("Escolha o algoritmo: ")

    if opcao == "0":
        running = False
        break

    desenhar_cenario()

    if opcao == "1":
        pygame.event.pump()

        x1 = int(input("x1: "))
        y1 = int(input("y1: "))
        x2 = int(input("x2: "))
        y2 = int(input("y2: "))

        dda(x1, y1, x2, y2)

    elif opcao == "2":
        pygame.event.pump()

        x1 = int(input("x1: "))
        y1 = int(input("y1: "))
        x2 = int(input("x2: "))
        y2 = int(input("y2: "))

        dx = x2 - x1
        dy = y2 - y1

        if dx <= 0 or dy < 0 or dy > dx:
            print("\nA reta deve estar no primeiro oitante.")
            print("Condição: 0 < m < 1")

        else:
            bresenham(x1, y1, x2, y2)

    elif opcao == "3":
        pygame.event.pump()

        xc = int(input("Centro X: "))
        yc = int(input("Centro Y: "))
        r = int(input("Raio: "))

        circunferencia_explicita(xc, yc, r)

    elif opcao == "4":
        pygame.event.pump()

        xc = int(input("Centro X: "))
        yc = int(input("Centro Y: "))
        r = int(input("Raio: "))

        circunferencia_trigonometrica(xc, yc, r)

    elif opcao == "5":
        pygame.event.pump()

        xc = int(input("Centro X: "))
        yc = int(input("Centro Y: "))
        r = int(input("Raio: "))

        circunferencia_bresenham(xc, yc, r)

    else:
        print("\nOpção inválida.")

    pygame.display.update()

    print("\nPressione qualquer tecla na janela para continuar...")

    esperando = True

    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                esperando = False

            elif event.type == pygame.KEYDOWN:
                esperando = False

pygame.quit()