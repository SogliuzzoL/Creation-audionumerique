from pythonosc.udp_client import SimpleUDPClient
import pygame


def fxChangeValue(trackId, fxId, fxParamId, value):
    client.send_message(f"/track/{trackId}/fx/{fxId}/fxparam/{fxParamId}/value", value)


def trackChangeVolume(trackId, volume):
    client.send_message(f"/track/{trackId}/volume", volume)


ip = "127.0.0.1"
port = 8000

defaultValue = 0.5
trackId = 1

client = SimpleUDPClient(ip, port)
trackChangeVolume(trackId, defaultValue)

pygame.init()
window_width = 720
window_height = 720
screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
running = True
n_colums = 4
n_row = 4
margin = 10
x_start = 0.05 * window_width
y_start = 0.05 * window_height
width = (window_width - 2 * x_start - n_colums * margin) / n_colums
height = (window_height - 2 * y_start - n_row * margin) / n_row
font = pygame.font.SysFont(pygame.font.get_fonts()[1], 24)
buttons = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, button in enumerate(buttons):
                if button.collidepoint(pygame.mouse.get_pos()):
                    print(f"Button {i + 1} clicked")
                    if i == 0:
                        fxChangeValue(1, 1, 1, 0.4)

    buttons = []
    screen.fill("white")
    for i in range(n_colums):
        for j in range(n_row):
            buttons.append(
                pygame.draw.rect(
                    screen,
                    "black",
                    (
                        x_start + i * (width + margin),
                        y_start + j * (height + margin),
                        width,
                        height,
                    ),
                )
            )
            text = font.render(str(i * n_colums + j + 1), True, "white")
            screen.blit(
                text,
                (
                    x_start + i * (width + margin) + margin,
                    y_start + j * (height + margin) + margin,
                ),
            )
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
