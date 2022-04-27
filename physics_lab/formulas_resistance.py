from formulas import *


# power for y(x)
def power_f(speed, angle, mass, coef, x):
    res = (speed*cos(angle*pi/180)*mass - x*coef)/(speed*cos(angle*pi/180)*mass)
    res = typo(res)
    return res


# x(t) function with resistance
def x_t_resistance(speed, mass, coef, time, angle):
    res = (speed*cos(angle*pi/180)*mass/coef)*(1 - exp(-coef*time/mass))
    res = typo(res)
    return res


# y(t) function with resistance
def y_t_resistance(speed, mass, coef, g, time, angle):
    res = (mass/coef)*((speed*sin(angle*pi/180) + mass*g/coef)*(1 - exp(-coef*time/mass)) - g*time)
    res = typo(res)
    return res


# y(x) function with resistance
def y_x_resistance(speed, mass, coef, g, angle, x):
    power = power_f(speed, angle, mass, coef, x)
    res = (mass/coef)*((speed*sin(angle*pi/180) + mass*g/coef)*(1 - exp(log(power, e))) + g*mass*exp(log(power, e))/coef)
    res = typo(res)
    print(res)
    return res


# Time of flight with resistance
def time_f_resistance(speed, mass, coef, g, angle):
    i = 0
    time = 0
    while i < 100000:  # limit
        y = y_t_resistance(speed, mass, coef, g, time, angle)
        time += 0.001
        i += 1
        if y < 0:
            return time


# function of filling arrays with coordinates (x, t) (RESISTANCE != 0)
def data_x_t_resistance(func, speed, mass, coef, time, angle, arr_t, arr_x):
    i = 0
    t = 0
    while i < 100000:  # limit
        arr_t.extend([t])  # array of time
        x = func(speed, mass, coef, t, angle)
        arr_x.extend([x])
        t += 0.01
        if t > time:
            break
        i += 1


# function of filling arrays with coordinates (y, t) (RESISTANCE != 0)
def data_y_t_resistance(func, speed, mass, coef, g, time, angle, arr_t, arr_y):
    i = 0
    t = 0
    while i < 100000:  # limit
        arr_t.extend([t])  # array of time
        y = func(speed, mass, coef, g, t, angle)
        arr_y.extend([y])
        t += 0.01
        if t > time:
            break
        i += 1


# function of filling arrays with coordinates parametrically (y,x) (RESISTANCE != 0)
def data_y_x_t_resis(speed, mass, coef, time, angle, g, arr_x, arr_y):
    i = 0
    t = 0
    while i < 100000:  # limit
        x = x_t_resistance(speed, mass, coef, t, angle)
        arr_x.extend([x])
        y = y_t_resistance(speed, mass, coef, g, t, angle)
        arr_y.extend([y])
        t += 0.01
        if t > time:
            break
        i += 1