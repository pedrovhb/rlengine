from __future__ import annotations
import typing as T

if T.TYPE_CHECKING:
    from particles import ParticleBehavior

from pyglet.sprite import Sprite


class Particle:

    def __init__(self,
                 sprite: Sprite,
                 behaviors: T.List[ParticleBehavior],
                 max_life: float = 5
                 ):
        self.sprite = sprite
        self.behaviors = behaviors
        self.crt_time = 0
        self.max_life = max_life

    def update(self, dt):
        self.crt_time += dt
        destroy = False
        for beh in self.behaviors:
            destroy = destroy or beh.update(self, dt)
        return destroy or self.crt_time > self.max_life
