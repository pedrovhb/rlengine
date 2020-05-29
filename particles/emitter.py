from __future__ import annotations

import math
import random
import typing as T

from .behavior import BehaviorAcceleration, BehaviorFade, BehaviorRotate

if T.TYPE_CHECKING:
    pass

from pyglet.graphics import Batch
from pyglet.image import Texture
from pyglet.sprite import Sprite

from . import Particle, particle_texture, BehaviorSpeed, ParticleBehavior


class ParticleEmitter:
    def __init__(self, lifetime: float):
        self.crt_time = 0
        self.lifetime = lifetime
        self.particles = set()
        self.batch = Batch()

    def create_particle(
        self,
        x: float,
        y: float,
        scale: float,
        initial_texture: Texture,
        behaviors: T.List[ParticleBehavior],
    ):
        sprite = Sprite(initial_texture, x, y, batch=self.batch)
        sprite.scale = scale
        self.particles.add(Particle(sprite, behaviors))

    def update(self, dt):
        self.crt_time += dt
        to_remove = set()
        for particle in self.particles:
            pop = particle.update(dt)
            if pop:
                to_remove.add(particle)
        [self.particles.remove(tr) for tr in to_remove]

    def draw(self):
        self.batch.draw()


class TestEmitter(ParticleEmitter):
    def __init__(self, lifetime: float):
        initial_texture = particle_texture
        super().__init__(lifetime)

        for _ in range(100):
            self.create_particle(
                100,
                100,
                1 / 20,
                initial_texture,
                [BehaviorSpeed(100, random.randint(0, 360)), BehaviorFade(1)],
            )

    def update(self, dt):
        super(TestEmitter, self).update(dt)
        self.create_particle(
            100,
            100,
            1 / 10,
            particle_texture,
            [
                BehaviorAcceleration(
                    100,
                    math.fmod(self.crt_time * 5, math.pi * 2),
                    1,
                    math.pi / 4,
                ),
                BehaviorFade(0.3),
                BehaviorRotate(math.pi * 100),
            ],
        )
        self.create_particle(
            100,
            100,
            1 / 10,
            particle_texture,
            [
                BehaviorAcceleration(
                    100,
                    math.fmod(-self.crt_time * 5, math.pi * 2),
                    1,
                    math.pi / 4,
                ),
                BehaviorFade(0.3),
                BehaviorRotate(math.pi * 100),
            ],
        )
