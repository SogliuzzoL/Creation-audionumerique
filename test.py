from pythonosc.udp_client import SimpleUDPClient
import time

ip = "127.0.0.1"
port = 8000
client = SimpleUDPClient(ip, port)


def fxChangeValue(trackId, fxId, fxParamId, value):
    client.send_message(f"/track/{trackId}/fx/{fxId}/fxparam/{fxParamId}/value", value)


trackId = 3
fxId = 1

fxChangeValue(trackId, fxId, 1, 50 / 127)
fxChangeValue(trackId, fxId, 2, 40 / 127)
fxChangeValue(trackId, fxId, 3, 0.1 / 16)
fxChangeValue(trackId, fxId, 4, 0.9)
time.sleep(2)
fxChangeValue(trackId, fxId, 4, 0.1)
