import matplotlib.pyplot as plt
import numpy as np
from math import sqrt, sin, cos, pi
import pandas as pd


def main():
    plt.title('Зависимость изменения угла')
    plt.xlabel('Ось x')
    plt.ylabel('Ось y')
    plt.plot([i for i in range(10000)], [sqrt(i) for i in range(10000)])
    #plt.show()
    height = 0
    resistance_coefficient = 0.5
    thrust_of_the_first_stage = 9806.65 * 3000
    thrust_of_the_second_stage = 9806.65 * 650
    table = {'Высота': []}
    a_y = 0
    v_y = 0
    alpha = 90
    gg = 6.67 * 10 ** -11
    m_0 = 240_000
    pl = list(map(lambda x: x / 1000, [3.08, 2.35, 1.75, 1.75, 1.40, 1.09,
                                       0.842, 0.627, 0.550, 0.402, 0.316,
                                       0.245, 0.181, 0.144, 0.102, 0.0769,
                                       0.594, 0.449, 0.0327, 0.0239, 0.0163]))

    a_x = 0
    v_x = 0
    t = 0
    while height < 350_000:
        f_thrust = thrust_of_the_first_stage
        f_gravity = gg * m_0 * 5.9726 ** 24 / ((6378_000 + height) ** 2)
        f_resistance = 0.5 * (pi * 18 * (18 + 40)) * (v_y ** 2) * (pl[int(height // 2000)] if height < 40000 else 0) / 2
        a_y = (f_thrust - f_resistance - f_gravity) * sin(alpha) / m_0
        v_y = a_y + v_y
        height = height + v_y + a_y / 2
        table['Высота'].append(height)
        a_x = (f_thrust - f_resistance - f_gravity) * cos(alpha) / m_0
        v_x = a_x + v_x
        if height > 50000:
            thrust_of_the_first_stage = thrust_of_the_second_stage

    print(pd.DataFrame(table))


if __name__ == '__main__':
    main()
