from __future__ import annotations

import pyglet
import typing as T

from pyglet.window import key

from particles.emitter import TestEmitter
from tile_map import TiledImageMap

window = pyglet.window.Window()
fps_display = pyglet.window.FPSDisplay(window=window)


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('The "A" key was pressed.')
    elif symbol == key.LEFT:
        print('The left arrow key was pressed.')
    elif symbol == key.ENTER:
        print('The enter key was pressed.')


tiles = TiledImageMap("monochrome_transparent.png")
pe = TestEmitter(1000)


@window.event
def on_draw():
    window.clear()
    for i in range(20):
        tiles[3, i].blit(i * 40, 400, 0, 32, 32)
    fps_display.draw()
    pe.draw()


def update(dt):
    pe.update(dt)


pyglet.clock.schedule_interval(update, 1 / 144.0)
pyglet.app.run()
