# python-libcava
CAVA audio visualizer bindings for python using FIFO

# Usage

```python
# Print the pillars for 5 seconds
from libcava import CAVA
from time import sleep

def simple_callback(sample: list[float]):
    # sample: (0.0,1.0,...)
    print(sample)

cava = CAVA(
    bars = 10, # The amount of bars ("pillars") per sample
    callback = simple_callback # Callback function that will receive samples ranging 0-1 
)

cava.start()
sleep
```