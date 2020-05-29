from __future__ import annotations
import typing as T
if T.TYPE_CHECKING:
    from .particle import Particle

import math


class ParticleBehavior:

    def __init__(self):
        self.crt_life = 0

    def update(self, particle, dt):
        raise NotImplementedError


class BehaviorSpeed(ParticleBehavior):

    def __init__(self, speed: float, direction: float):
        super().__init__()
        self.speed = speed
        self.direction = direction

    def update(self, particle: Particle, dt: float):
        particle.sprite.x += self.speed * math.cos(self.direction) * dt
        particle.sprite.y += self.speed * math.sin(self.direction) * dt
