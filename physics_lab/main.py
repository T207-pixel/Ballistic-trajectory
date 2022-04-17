# Movement of a body thrown with angle to the horizontal, taking in account resistance of air.
# Input parameters: speed, angle, resistance, mass
from formulas_resistance import *
from frontend import *


def main():
    speed = 0
    angle = 0
    resistance = 0
    mass = 0
    coef = 0
    g = 9.80665
    arr_x = []
    arr_y = []
    arr_t = []
    print("Enter speed: ")
    speed = float(input())
    print("Enter angle: ")
    angle = float(input())
    print("Enter resistance")
    coef = float(input())
    option = 0
    if coef == 0:
        option = 2
    elif coef > 0:
        option = 1

    if option == 1:
        print("Enter mass of body")
        mass = float(input())
        time = time_f_resistance(speed, mass, coef, g, angle)
        print("Time:\t", time)
        length = x_t_resistance(speed, mass, coef, time, angle)
        print("Select graphic:\n1) x(t), y(t)\n2) y(x) ")
        choice = int(input())
        if choice == 1:
            data_x_t_resistance(x_t_resistance, speed, mass, coef, time, angle, arr_t, arr_x)
            data_y_t_resistance(y_t_resistance, speed, mass, coef, g, time, angle, arr_t, arr_y)
            draw_func_1(arr_t, arr_x, arr_y, '$$x(t)=(\\frac{v_{0x}m}{k})(1-e^{\\frac{-kt}{m}})$$',
                        '$$y(t)=(\\frac{m}{k})[(v_{0y}+\\frac{mg}{k})(1-e^{\\frac{-kt}{m}})-gt]$$',
                        "Ballistic trajectory with resistance", "Time", "Displacement of X and Y")
        elif choice == 2:
            data_y_x_t_resis(speed, mass, coef, time, angle, g, arr_x, arr_y)
            draw_func_2(arr_x, arr_y, '$$y=f(x)$$', "Ballistic trajectory with resistance", "Length of flight X",
                        "Height of flight Y")
    else:
        time = time_f(speed, angle, g)
        length = length_f(speed, angle, g)
        print("Select graphic:\n1) x(t), y(t)\n2) y(x) ")
        choice = int(input())
        if choice == 1:
            data_x_t(x_t, speed, angle, time, arr_t, arr_x)
            data_y_t(y_t, speed, angle, time, g, arr_t, arr_y)
            draw_func_1(arr_t, arr_x, arr_y, '$$x(t)=v*cos(a)*t$$', '$$y(t)=v*sin(a)*t-(\\frac{g*t^2}{2})$$',
                        "Ballistic trajectory", "Time", "Displacement of X and Y")
        elif choice == 2:
            data_y_x(y_point, length, angle, g, speed,  arr_x, arr_y)
            draw_func_2(arr_x, arr_y, '$$y(x)=x*tg(a)-\\frac{g*x^2}{2*v^2*cos(a)^2*t}$$', "Ballistic trajectory",
                        "Length of flight X", "Height of flight Y")


if __name__ == "__main__":
    main()
