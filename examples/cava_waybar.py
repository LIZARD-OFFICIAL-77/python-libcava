import sys;sys.path.append(".")
"""
ASCII cava for waybar and polybar
"""

from libcava import CAVA
from time import sleep

def ascii_callback(sample: list[float]):
    # sample: (0.0,1.0,...)
    ascii = "▁▂▃▄▅▆▇█"
    print("".join([ascii[round((i*7))] for i in sample]),end="\r")

cava = CAVA(
    bars = 10, # The amount of bars ("pillars") per sample
    callback = ascii_callback # Callback function that will receive samples ranging 0-1 
)

cava.start()