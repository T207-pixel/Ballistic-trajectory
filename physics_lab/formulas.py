from math import sin, tan, cos, pi, pow, exp, log, e


# Makes correct type of returning value
def typo(arg):
    res = '%0.10f' % arg
    res = float(res)
    return res


# Checking input for float
def is_float(num):
    try:
        float(num)
        return num
    except ValueError:
        return print("Entered wrong type of data, gets integer or float\nRepeat input:")
    except float(num) < 0:
        print("Enter positive number: ")


# Checking input for float && int
def get_number():
    while True:
        number = input()
        if number.isdigit():
            if int(number) >= 0:
                return number
            else:
                print("Enter positive number: ")
        elif number == is_float(number):
            if float(number) >= 0:
                return number
            else:
                print("Enter positive number: ")


# Checking input for int
def get_digit():
    while True:
        number = input()
        if number.isdigit():
            return number
        else:
            print("Enter integer")


# Time of flight without resistance
def time_f(speed, angle, g):
    res = (2*speed*sin((angle*pi)/180))/g
    res = typo(res)
    return res


# Distance of flight without resistance
def length_f(speed, angle, g):
    res = pow(speed, 2)*(sin(2*angle*pi/180))/g
    res = typo(res)
    return res


# y(x) function without resistance
def y_point(x, angle, g, speed):
    res = x*tan(angle*pi/180) - (g*x*x)/(2*pow(speed, 2)*pow(cos(angle*pi/180), 2))  # x*tg(a)-\frac{g*x^2}{2*v^2*cos(a)^2}
    res = typo(res)
    return res


# x(t) function without resistance
def x_t(speed, angle, time):
    res = speed*cos(angle*pi/180)*time  # v*cos(a)*t
    res = typo(res)
    return res


# y(t) function without resistance
def y_t(speed, angle, time, g):
    res = (speed*sin(angle*pi/180)*time) - (g*pow(time, 2)/2)  # v*sin(a)*t-(g*time^2)/2
    res = typo(res)
    return res


# function of filling arrays with coordinates (y,x) (RESISTANCE = 0)
def data_y_x(func, length, angle, g, speed,  arr_x, arr_y):
    i = 0
    x = 0
    while i < 100000:  # limit
        arr_x.extend([x])
        y = func(x, angle, g, speed)
        arr_y.extend([y])
        x += 0.1
        if x > length:
            break
        i += 1


# function of filling arrays with coordinates (x, t) (RESISTANCE = 0)
def data_x_t(func, speed, angle, time, arr_t, arr_x):
    i = 0
    t = 0
    while i < 100000:  # limit
        arr_t.extend([t])  # array of time
        x = func(speed, angle, t)
        arr_x.extend([x])
        t += 0.01
        if t > time:
            break
        i += 1


# function of filling arrays with coordinates (y, t) (RESISTANCE = 0)
def data_y_t(func, speed, angle, time, g, arr_t, arr_y):
    i = 0
    t = 0
    while i < 100000:  # limit
        arr_t.extend([t])  # array of time
        y = func(speed, angle, t, g)
        arr_y.extend([y])
        t += 0.01
        if t > time:
            break
        i += 1

