from pythonosc.udp_client import SimpleUDPClient
import pygame


def fxChangeValue(trackId, fxId, fxParamId, value):
    client.send_message(f"/track/{trackId}/fx/{fxId}/fxparam/{fxParamId}/value", value)


def trackChangeVolume(trackId, volume):
    client.send_message(f"/track/{trackId}/volume", volume)


def masterChangeVolume(volume):
    client.send_message(f"/master/volume", volume)


def trackMute(trackId, value):
    client.send_message(f"/track/{trackId}/mute", int(value))


ip = "127.0.0.1"
port = 8000

defaultValue = 0.5
pasValue = 0.05
roundValue = 3
volumeValue = 0.5
trackId = 1
fxId = 1
fxParam = 1
fxValues = {(trackId, fxId, fxParam): defaultValue}
trackVolumeValues = {trackId: defaultValue}
mutedTrack = {trackId: False}

client = SimpleUDPClient(ip, port)

buttonsName = [
    "Master +",
    "Master -",
    "Volume +",
    "Volume -",
    "Track +",
    "Track -",
    "FX +",
    "FX -",
    "FX Param +",
    "FX Param -",
    "FX Value +",
    "FX Value -",
    "FX Reset",
    "Mute Track",
]

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
fontInfo = pygame.font.SysFont(pygame.font.get_fonts()[1], 18)
buttons = []
infoTxt = f"Volume: {volumeValue} \nTrack: {trackId} \nFX: {fxId} \nFX Param: {fxParam}"

while running:
    screen.fill("white")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, button in enumerate(buttons):
                if button.collidepoint(pygame.mouse.get_pos()):
                    if i == 0:
                        volumeValue += pasValue
                        volumeValue = round(volumeValue, roundValue)
                        volumeValue = min(1, volumeValue)
                        masterChangeVolume(volumeValue)
                    elif i == 1:
                        volumeValue -= pasValue
                        volumeValue = round(volumeValue, roundValue)
                        volumeValue = max(0, volumeValue)
                        masterChangeVolume(volumeValue)
                    elif i == 2:
                        if trackId not in trackVolumeValues.keys():
                            trackVolumeValues[trackId] = defaultValue
                        trackVolumeValues[trackId] += pasValue
                        trackVolumeValues[trackId] = min(1, trackVolumeValues[trackId])
                        trackChangeVolume(trackId, trackVolumeValues[trackId])
                    elif i == 3:
                        if trackId not in trackVolumeValues.keys():
                            trackVolumeValues[trackId] = defaultValue
                        trackVolumeValues[trackId] -= pasValue
                        trackVolumeValues[trackId] = max(0, trackVolumeValues[trackId])
                        trackChangeVolume(trackId, trackVolumeValues[trackId])
                    elif i == 4:
                        trackId += 1
                    elif i == 5:
                        trackId -= 1
                        trackId = max(1, trackId)
                    elif i == 6:
                        fxId += 1
                    elif i == 7:
                        fxId -= 1
                        fxId = max(1, fxId)
                    elif i == 8:
                        fxParam += 1
                    elif i == 9:
                        fxParam -= 1
                        fxParam = max(1, fxParam)
                    elif i == 10:
                        if (trackId, fxId, fxParam) not in fxValues.keys():
                            fxValues[(trackId, fxId, fxParam)] = defaultValue
                        fxValues[(trackId, fxId, fxParam)] += pasValue
                        fxValues[(trackId, fxId, fxParam)] = round(
                            fxValues[(trackId, fxId, fxParam)], roundValue
                        )
                        fxChangeValue(
                            trackId, fxId, fxParam, fxValues[(trackId, fxId, fxParam)]
                        )
                    elif i == 11:
                        if (trackId, fxId, fxParam) not in fxValues.keys():
                            fxValues[(trackId, fxId, fxParam)] = defaultValue
                        fxValues[(trackId, fxId, fxParam)] -= pasValue
                        fxValues[(trackId, fxId, fxParam)] = round(
                            fxValues[(trackId, fxId, fxParam)], roundValue
                        )
                        fxValues[(trackId, fxId, fxParam)] = max(
                            0, fxValues[(trackId, fxId, fxParam)]
                        )
                        fxChangeValue(
                            trackId, fxId, fxParam, fxValues[(trackId, fxId, fxParam)]
                        )
                    elif i == 12:
                        fxValues[(trackId, fxId, fxParam)] = defaultValue
                        fxChangeValue(
                            trackId, fxId, fxParam, fxValues[(trackId, fxId, fxParam)]
                        )
                    elif i == 13:
                        if trackId not in mutedTrack.keys():
                            mutedTrack[trackId] = False
                        mutedTrack[trackId] = not mutedTrack[trackId]
                        trackMute(trackId, mutedTrack[trackId])

                infoTxt = f"Volume: {volumeValue} \nTrack: {trackId} \nFX: {fxId} \nFX Param: {fxParam} \n"
    textInfo = fontInfo.render(infoTxt, True, "blue")
    screen.blit(textInfo, (x_start, margin))

    buttons = []
    for j in range(n_row):
        for i in range(n_colums):
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
            textStr = f"{i + j * n_row + 1}"
            if i + j * n_row < len(buttonsName):
                textStr = f"{buttonsName[i + j * n_row]}"
            text = font.render(textStr, True, "white")
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
