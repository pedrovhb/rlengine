from __future__ import annotations

import pyglet

particle_texture = pyglet.image.load("particles/imgs/magic_03.png")
particle_texture.anchor_x = particle_texture.width // 2
particle_texture.anchor_y = particle_texture.height // 2
