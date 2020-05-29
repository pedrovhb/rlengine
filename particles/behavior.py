from __future__ import annotations
import typing as T

if T.TYPE_CHECKING:
    from .particle import Particle

import math


class ParticleBehavior:
    __slots__ = set()

    def update(self, particle, dt):
        raise NotImplementedError


class BehaviorSpeed(ParticleBehavior):
    __slots__ = {"speed", "x_factor", "y_factor"}

    def __init__(self, speed: float, direction: float):
        self.speed = speed

        self.x_factor = math.cos(direction)
        self.y_factor = math.sin(direction)

    def update(self, particle: Particle, dt: float):
        particle.sprite.x += self.speed * self.x_factor * dt
        particle.sprite.y += self.speed * self.y_factor * dt
        return False


class BehaviorAcceleration(BehaviorSpeed):
    __slots__ = {"acceleration", "acc_x_factor", "acc_y_factor"}

    def __init__(
            self,
            initial_speed: float,
            initial_speed_direction: float,
            acceleration: float,
            acceleration_direction: float,
    ):
        super(BehaviorAcceleration, self).__init__(
            initial_speed, initial_speed_direction
        )
        self.acceleration = acceleration

        self.acc_x_factor = math.cos(acceleration_direction)
        self.acc_y_factor = math.sin(acceleration_direction)

    def update(self, particle: Particle, dt: float):
        super(BehaviorAcceleration, self).update(particle, dt)
        self.x_factor += self.acc_x_factor * self.acceleration * dt
        self.y_factor += self.acc_y_factor * self.acceleration * dt
        return False


class BehaviorFade(ParticleBehavior):
    __slots__ = {"decay_rate"}

    def __init__(self, decay_rate):
        self.decay_rate = decay_rate

    def update(self, particle: Particle, dt: float):
        particle.sprite.opacity -= self.decay_rate * dt * 255
        return particle.sprite.opacity <= 0
