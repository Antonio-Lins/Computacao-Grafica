import pygame

pygame.init()

WIDTH = int(input("Largura da janela: "))
HEIGHT = int(input("Altura da janela: "))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Transformacoes de Coordenadas")

xmin = float(input("xmin: "))
xmax = float(input("xmax: "))

ymin = float(input("ymin: "))
ymax = float(input("ymax: "))

x_world = float(input("Coordenada x do ponto: "))
y_world = float(input("Coordenada y do ponto: "))

# mundo - NDC (0 a 1)
def user_to_ndc_01(x, y):
    ndcx = (x - xmin) / (xmax - xmin)
    ndcy = (y - ymin) / (ymax - ymin)
    return ndcx, ndcy

# mundo - NDC (-1 a 1)
def user_to_ndc_11(x, y):
    ndcx = 2 * ((x - xmin) / (xmax - xmin)) - 1
    ndcy = 2 * ((y - ymin) / (ymax - ymin)) - 1
    return ndcx, ndcy


# NDC (0 a 1) - dispositivo
def ndc01_to_dc(ndcx, ndcy):
    dcx = round(ndcx * (WIDTH - 1))
    dcy = round((1 - ndcy) * (HEIGHT - 1))
    return dcx, dcy

# NDC (-1 a 1) - dispositivo
def ndc11_to_dc(ndcx, ndcy):
    dcx = round(((ndcx + 1) / 2) * (WIDTH - 1))
    dcy = round(((1 - ndcy) / 2) * (HEIGHT - 1))
    return dcx, dcy

# Desenha o pixel na janela
def draw_pixel(x, y, color):
    screen.set_at((x, y), color)

ndcx_01, ndcy_01 = user_to_ndc_01(x_world, y_world)
dcx_01, dcy_01 = ndc01_to_dc(ndcx_01, ndcy_01)

ndcx_11, ndcy_11 = user_to_ndc_11(x_world, y_world)
dcx_11, dcy_11 = ndc11_to_dc(ndcx_11, ndcy_11)

print("\n========== NDC 0 A 1 ==========")
print("Coordenadas NDC:")
print(ndcx_01, ndcy_01)
print("Coordenadas do Dispositivo:")
print(dcx_01, dcy_01)

print("\n========== NDC -1 A 1 ==========")
print("Coordenadas NDC:")
print(ndcx_11, ndcy_11)
print("Coordenadas do Dispositivo:")
print(dcx_11, dcy_11)

# loop principa do código/py.games
running = True

while running:
    screen.fill((0, 0, 0))
    
    draw_pixel(dcx_01, dcy_01, (255, 255, 255))
    draw_pixel(dcx_11, dcy_11, (255, 0, 0))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()