import pygame

pygame.init()

WIDTH = int(input("Largura da janela: "))
HEIGHT = int(input("Altura da janela: "))

# WIDTH = 800
# HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Transformacoes de Coordenadas")

xmin = float(input("xmin: "))
xmax = float(input("xmax: "))

ymin = float(input("ymin: "))
ymax = float(input("ymax: "))

# xmin = -100
# xmax = 100
#
# ymin = -100
# ymax = 100

x_world = float(input("Coordenada x do ponto: "))
y_world = float(input("Coordenada y do ponto: "))

# x_world = 0
# y_world = 0

def user_to_ndc(x, y):
    ndcx = (x - xmin) / (xmax - xmin)
    ndcy = (y - ymin) / (ymax - ymin)
    return ndcx, ndcy


def ndc_to_dc(ndcx, ndcy):
    dcx = round(ndcx * (WIDTH - 1))
    dcy = round((1 - ndcy) * (HEIGHT - 1))
    return dcx, dcy

def draw_pixel(x, y, color=(255, 255, 255)):

    screen.set_at((x, y), color)

ndcx, ndcy = user_to_ndc(x_world, y_world)
dcx, dcy = ndc_to_dc(ndcx, ndcy)

print("\nCoordenadas do Mundo:")
print(x_world, y_world)

print("\nCoordenadas NDC:")
print(ndcx, ndcy)

print("\nCoordenadas do Dispositivo:")
print(dcx, dcy)


running = True

while running:
    screen.fill((0, 0, 0))
    draw_pixel(dcx, dcy)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()