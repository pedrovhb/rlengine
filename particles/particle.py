from __future__ import annotations
import typing as T

if T.TYPE_CHECKING:
    from particles import ParticleBehavior

from pyglet.sprite import Sprite


class Particle:

    def __init__(self,
                 sprite: Sprite,
                 behaviors: T.List[ParticleBehavior]
                 ):
        self.sprite = sprite
        self.behaviors = behaviors
        self.crt_time = 0

    def update(self, dt):
        self.crt_time += dt
        for beh in self.behaviors:
            beh.update(self, dt)
