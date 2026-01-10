# Задание 2: Функции, модульные тесты
import math


def input_float(prompt):
    return float(input(prompt))


def read_data():
    d1_yards = input_float(
        "Введите кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды) => "
    )
    d2_feet = input_float(
        "Введите кратчайшее расстояние от утопающего до берега, d2 (футы) => "
    )
    h_yards = input_float(
        "Введите боковое смещение между спасателем и утопающим, h (ярды) => "
    )
    v_sand_mph = input_float(
        "Введите скорость движения спасателя по песку, v_sand (мили в час) => "
    )
    n = input_float(
        "Введите коэффициент замедления спасателя при движении в воде, n => "
    )
    theta_deg = input_float(
        "Введите направление движения спасателя по песку, theta1 (градусы) => "
    )
    return d1_yards, d2_feet, h_yards, v_sand_mph, n, theta_deg


def yards_to_feet(yards):
    return yards * 3.0


def mph_to_fps(mph):
    return mph * 5280.0 / 3600.0


def deg_to_rad(deg):
    return deg * math.pi / 180.0


def calc_time_seconds(d1_yards, d2_feet, h_yards, v_sand_mph, n, theta_deg):
    d1 = yards_to_feet(d1_yards)
    h = yards_to_feet(h_yards)
    v_sand = mph_to_fps(v_sand_mph)
    theta = deg_to_rad(theta_deg)

    x = d1 * math.tan(theta)
    L1 = math.sqrt(x * x + d1 * d1)
    L2 = math.sqrt((h - x) * (h - x) + d2_feet * d2_feet)

    t = (L1 + n * L2) / v_sand
    return t


def print_result(theta_deg, t_seconds):
    theta_int = int(theta_deg)
    print(
        f"Если спасатель начнёт движение под углом theta1, равным {theta_int} градусам, он"
    )
    print(f"достигнет утопающего через {t_seconds:.1f} секунды")


# Тесты --------------------

assert yards_to_feet(1) == 3.0
assert abs(mph_to_fps(1) - (5280.0 / 3600.0)) < 1e-9

assert abs(deg_to_rad(180) - math.pi) < 1e-9

t_test = calc_time_seconds(8, 10, 50, 5, 2, 39.413)
assert t_test > 0

t1 = calc_time_seconds(8, 10, 50, 5, 2, 39.413)
t2 = calc_time_seconds(8, 10, 50, 10, 2, 39.413)
assert t2 < t1


d1_yards, d2_feet, h_yards, v_sand_mph, n, theta_deg = read_data()
t_seconds = calc_time_seconds(d1_yards, d2_feet, h_yards, v_sand_mph, n, theta_deg)
print_result(theta_deg, t_seconds)
