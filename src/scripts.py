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
    table = {'Высота': [], 'Скорость': [], 'Ускорение по x': [], 'Ускорение по y': []}
    acceleration = Vector()
    velocity = Vector()
    alpha = 90
    gg = 3.5 * 10 ** 12
    m_0 = 240_000
    minus_topl = [sqrt(i) for i in range(10000)]

    pl = {0: 1.225, 2500: 0.898, 5000: 0.642, 7500: 0.446,
          10000: 0.288, 15000: 0.108, 20000: 0.040, 25000: 0.015,
          30_000: 0.006, 40_000: 0.001}
    t = 0
    x = [0]
    y = [600_000]
    speed_first_cosmo = sqrt(gg / (600_000 + 150_000))
    while height < 150_000:
        f_thrust = thrust_of_the_first_stage
        f_gravity = gg * m_0 / ((600_000 + height) ** 2)
        f_resistance = (resistance_coefficient * (pi * 9 * (18 + 10)) * (velocity.y ** 2)
                        * (pl[int(height // 10_000 * 10_000)] if height <= 40000 else 0) / 2)
        acceleration.y = (f_thrust - f_resistance - f_gravity) * sin(radians(alpha)) / m_0
        height += velocity.y + acceleration.y / 2
        y.append(y[-1] + velocity.y + acceleration.y / 2)
        velocity.y = acceleration.y + velocity.y
        table['Высота'].append(height)
        acceleration.x = (f_thrust - f_resistance - f_gravity) * cos(radians(alpha)) / m_0
        velocity.x = acceleration.x + velocity.x
        table['Скорость'].append(sqrt(velocity.x ** 2 + velocity.y ** 2))
        table['Ускорение по x'].append(acceleration.x)
        table['Ускорение по y'].append(acceleration.y)
        m_0 -= minus_topl[t]
        full_speed = sqrt(velocity.x ** 2 + velocity.y ** 2)
        t += 1
        x.append(x[-1] + velocity.x + acceleration.x / 2)
        if full_speed > speed_first_cosmo:
            thrust_of_the_first_stage = 0
        if height > 60000 and alpha > 2:
            alpha -= 2
        time_rise.append(t)
    with open("../Буран-Энергия Remake_12111235.csv", "r") as file:
        ksp = pd.read_csv(file)
    plt.plot(ksp["Velocity"][:200], color='blue')
    plt.plot(time_rise, table['Скорость'], color='black')
    plt.legend(["KSP", "Мат.модель"])
    plt.title('Зависимость скорости от времени')
    plt.xlabel("Время в секундах")
    plt.ylabel("Скорость м/c")
    plt.show()
    plt.plot(x, y, color='black')
    plt.title("Координатная зависимость")
    plt.xlabel("Координаты по X")
    plt.ylabel("Координаты по Y")
    plt.show()
    plt.title("Зависимость плотности воздуха от высоты")
    plt.xlabel("Высота")
    plt.ylabel("Плотность")
    plt.plot(pl.keys(), pl.values())
    plt.show()
    plt.title("Зависимость скорости и высоты")
    plt.xlabel("Высота")
    plt.ylabel("скорость")
    plt.plot(table["Высота"], table["Скорость"])
    plt.show()
    second_orbit(acceleration, height, m_0, table)
    table = pd.DataFrame(table)
    table.to_csv("./report.csv")
    print(table)
    print("All good. Check out report.csv")


def second_orbit(acceleration, height, m_0, table):
    """
    Гомановский переход.

    """
    gg = 3.5 * 10 ** 12
    thrust_of_the_second_stage = 9806.65 * 800
    second_height = 350_000
    speed_orbit = sqrt(gg / (600_000 + 150_000))
    m_0 -= 1490000
    gamma_1 = pi - pi * sqrt(1/8 * (1 + 3/5) ** 3)
    gamma_2 = pi - gamma_1
    time = pi * sqrt((250_000 + 150_000) ** 3 / 8 / (3.5316000 * 10 ** 12))
    w = gamma_1 / time
    required_speed_0 = speed_orbit * (sqrt(2 * 7/3 / (7/3 + 1)) - 1)
    required_speed_1 = speed_orbit * (1 / sqrt(7/3)) * (1 - sqrt(2 / (7/3 + 1)))
    with open("../Буран-Энергия Remake_12111235.csv", "r") as file:
        ksp = pd.read_csv(file)
    plt.plot(ksp["AltitudeFromTerrain"], color='blue')
    plt.plot(range(len(table["Высота"])), table["Высота"], color='red')
    plt.legend(["KSP", "Мат.модель"])
    plt.title('Зависимость высоты от времени')
    plt.xlabel('Время в секундах')
    plt.ylabel('Высота в метрах')
    plt.show()
    print(required_speed_0, required_speed_1, speed_orbit)
    print((gamma_2 + gamma_1) / w)


def main():
    first_orbit()


if __name__ == '__main__':
    main()
