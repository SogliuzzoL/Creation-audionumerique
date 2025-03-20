from pythonosc.udp_client import SimpleUDPClient
import pygame

ip = "127.0.0.1"
port = 8000

track_id = 1
fx_id = 1
fxparam_id = 2
volume = 0.5
value = 1.5

client = SimpleUDPClient(ip, port)
client.send_message(f"/track/{track_id}/volume", volume)
for fxparam_id in range(1, 12):
    client.send_message(
        f"/track/{track_id}/fx/{fx_id}/fxparam/{fxparam_id}/value", value
    )

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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    for i in range(n_colums):
        for j in range(n_row):
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
            text = font.render(str(i + j * n_row + 1), True, "white")
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
