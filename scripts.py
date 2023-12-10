import matplotlib.pyplot as plt
from math import sqrt, sin, cos, pi, radians
import pandas as pd


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            raise TypeError
        return Vector(self.x + other.x, self.y + other.y)


def first_orbit():
    """
    Выход на первую орбиту, около 150км. Подготовка в Гомановскому переходу.
    Учитываем Силу гравитации, силу сопротивления воздуха, силу тяжести.
    Используем скорость и ускорение как основные изменяемые характеристики.
    """
    time_rise = []
    height = 0
    resistance_coefficient = 0.5
    thrust_of_the_first_stage = 9806.65 * 2600
    thrust_of_the_second_stage = 9806.65 * 800
    table = {'Высота': [], 'Скорость': []}
    acceleration = Vector()
    speed = Vector()
    alpha = 90
    gg = 3.5 * 10 ** 12
    m_0 = 240_000
    minus_topl = [sqrt(i) for i in range(10000)][::-1]

    pl = {0: 1.225, 2500: 0.898, 5000: 0.642, 7500: 0.446,
          10000: 0.288, 15000: 0.108, 20000: 0.040, 25000: 0.015,
          30_000: 0.006, 40_000: 0.001}
    t = 0
    spped_first_cosmo = sqrt(gg / (600_000 + 150_000))
    while height < 150_000:
        f_thrust = thrust_of_the_first_stage
        f_gravity = gg * m_0 / ((600_000 + height) ** 2)
        f_resistance = (resistance_coefficient * (pi * 9 * (18 + 10)) * (speed.y ** 2)
                        * (pl[int(height // 10_000 * 10_000)] if height <= 40000 else 0) / 2)
        acceleration.y = (f_thrust - f_resistance - f_gravity) * sin(radians(alpha)) / m_0
        #print(alpha, height, acceleration.y, speed.y, acceleration.x, acceleration.y, sep=" ------ ")
        height += speed.y + acceleration.y / 2
        speed.y = acceleration.y + speed.y
        table['Высота'].append(height)
        acceleration.x = (f_thrust - f_resistance - f_gravity) * cos(radians(alpha)) / m_0
        speed.x = acceleration.x + speed.x
        table['Скорость'].append(sqrt(speed.x ** 2 + speed.y ** 2))
        m_0 -= minus_topl[t]
        full_speed = sqrt(speed.x ** 2 + speed.y ** 2)
        t += 1
        if full_speed > spped_first_cosmo:
            thrust_of_the_first_stage = 0
        if height > 6000 and alpha >= 6:
            alpha -= 2
        time_rise.append(t)
    plt.plot(time_rise, table['Высота'])
    plt.title('Зависимость высоты от времени')
    plt.xlabel('Время в секундах')
    plt.ylabel('Высота в метрах')
    plt.show()
    plt.plot(time_rise, table['Скорость'])
    plt.title('Зависимость скорости от времени')
    plt.xlabel("Время в секундах")
    plt.ylabel("Скорость м/c")
    plt.show()
    table = pd.DataFrame(table)
    print(table)
    table.to_csv("report")
    second_orbit(speed, acceleration, height)


def second_orbit(speed, acceleration, height):
    """
    Гомановский переход.

    """
    second_height = 350_000
    first_speed = sqrt(speed.x ** 2 + speed.y ** 2)


def main():
    first_orbit()


if __name__ == '__main__':
    main()
