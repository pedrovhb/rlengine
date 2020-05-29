from __future__ import annotations
import typing as T

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
        self.particles = []
        self.batch = Batch()

    def create_particle(
        self,
        x: float,
        y: float,
        initial_texture: Texture,
        behaviors: T.List[ParticleBehavior],
    ):
        sprite = Sprite(initial_texture, x, y, batch=self.batch)
        self.particles.append(Particle(sprite, behaviors))

    def update(self, dt):
        for particle in self.particles:
            particle.update(dt)

    def draw(self):
        self.batch.draw()


class TestEmitter(ParticleEmitter):
    def __init__(self, lifetime: float):
        initial_texture = particle_texture
        super().__init__(lifetime)
        self.create_particle(100, 100, initial_texture, [BehaviorSpeed(100, 0)])
