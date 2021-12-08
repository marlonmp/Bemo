from discord import Embed

GREEN = 0x70e000
RED = 0xf40000
BLUE = 0x0353a4
WHITE = 0xf1faee

def green(**kwargs) -> Embed:
    return Embed(**kwargs, color=GREEN)

def red(**kwargs) -> Embed:
    return Embed(**kwargs, color=RED)

def blue(**kwargs) -> Embed:
    return Embed(**kwargs, color=BLUE)

def white(**kwargs) -> Embed:
    return Embed(**kwargs, color=WHITE)