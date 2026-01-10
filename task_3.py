import math


def yards_to_feet(y):
    return y * 3.0


def mph_to_fps(mph):
    return mph * 5280.0 / 3600.0


def deg_to_rad(deg):
    return deg * math.pi / 180.0


def rad_to_deg(rad):
    return rad * 180.0 / math.pi


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


def find_best_theta(d1_yards, d2_feet, h_yards, v_sand_mph, n):
    best_theta = 0.0
    best_time = None

    # перебор угла 0..89 с шагом 1 градус
    for theta in range(0, 90):
        t = calc_time_seconds(d1_yards, d2_feet, h_yards, v_sand_mph, n, theta)
        if best_time is None or t < best_time:
            best_time = t
            best_theta = theta

    return best_theta, best_time


def approx_theta_straight(d1_yards, h_yards):
    d1 = yards_to_feet(d1_yards)
    h = yards_to_feet(h_yards)
    theta = math.atan(h / d1)
    return rad_to_deg(theta)


d1_yards = float(
    input(
        "Введите кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды) => "
    )
)
d2_feet = float(
    input("Введите кратчайшее расстояние от утопающего до берега, d2 (футы) => ")
)
h_yards = float(
    input("Введите боковое смещение между спасателем и утопающим, h (ярды) => ")
)
v_sand_mph = float(
    input("Введите скорость движения спасателя по песку, v_sand (мили в час) => ")
)
n = float(input("Введите коэффициент замедления спасателя при движении в воде, n => "))

theta_num, t_num = find_best_theta(d1_yards, d2_feet, h_yards, v_sand_mph, n)

theta_approx = approx_theta_straight(d1_yards, h_yards)
t_approx = calc_time_seconds(d1_yards, d2_feet, h_yards, v_sand_mph, n, theta_approx)

print("\n=== Сравнение ===")
print(f"Численно (перебор): лучший угол = {theta_num}°, время = {t_num:.1f} сек")
print(
    f"Аналитически (приближение по прямой): угол = {theta_approx:.1f}°, время = {t_approx:.1f} сек"
)
