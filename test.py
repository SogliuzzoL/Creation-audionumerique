from pythonosc.udp_client import SimpleUDPClient
import time
import RPi.GPIO as GPIO


ip = "10.42.0.1"
port = 8000
client = SimpleUDPClient(ip, port)

BPpin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(BPpin, GPIO.IN)


def fxChangeValue(trackId, fxId, fxParamId, value):
    client.send_message(f"/track/{trackId}/fx/{fxId}/fxparam/{fxParamId}/value", value)


trackId = 3
fxId = 1

fxChangeValue(trackId, fxId, 1, 50 / 127)
fxChangeValue(trackId, fxId, 2, 40 / 127)
fxChangeValue(trackId, fxId, 3, 0.1 / 16)

while True:
    BPstate = GPIO.input(BPpin)
    if BPstate:
        fxChangeValue(trackId, fxId, 4, 0.9)
    else:
        fxChangeValue(trackId, fxId, 4, 0.1)
