import matplotlib.pyplot as plt
import numpy as np
from math import sqrt, sin, cos, pi
import pandas as pd


class Vector:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        if __name__ == '__main__':
            return Vector(self.x + other.x, self.y + other.y)


def main():
    height = 0
    resistance_coefficient = 0.5
    thrust_of_the_first_stage = 9806.65 * 800
    thrust_of_the_second_stage = 9806.65 * 650
    table = {'Высота': [], 'Скорость': []}
    acceleration = Vector()
    speed = Vector()
    alpha = 90
    gg = 6.67 * 10 ** -11
    m_0 = 240_000
    minus_topl = [sqrt(i) for i in range(10000)]
    pl = list(map(lambda x: x / 1000, [3.08, 2.35, 1.75, 1.75, 1.40, 1.09,
                                       0.842, 0.627, 0.550, 0.402, 0.316,
                                       0.245, 0.181, 0.144, 0.102, 0.0769,
                                       0.594, 0.449, 0.0327, 0.0239, 0.0163]))

    t = 0
    while height < 350_000:
        f_thrust = thrust_of_the_first_stage
        f_gravity = gg * m_0 * 5.9726 ** 24 / ((6378_000 + height) ** 2)
        f_resistance = (resistance_coefficient * (pi * 18 * (18 + 40)) * (speed.y ** 2)
                        * (pl[int(height // 2000)] if height < 40000 else 0) / 2)
        acceleration.y = (f_thrust - f_resistance - f_gravity) * sin(alpha) / m_0
        speed.y = acceleration.y + speed.y
        height = height + speed.y + acceleration.y / 2
        table['Высота'].append(height)
        acceleration.x = (f_thrust - f_resistance - f_gravity) * cos(alpha) / m_0
        speed.x = acceleration.x + speed.x
        table['Скорость'].append(sqrt(speed.x ** 2 + speed.y ** 2))
        m_0 -= minus_topl[t]
        t += 1
        alpha -= 0.05
        if height > 50000:
            thrust_of_the_first_stage = thrust_of_the_second_stage

    print(pd.DataFrame(table))


if __name__ == '__main__':
    main()
