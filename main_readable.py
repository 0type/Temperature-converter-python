temp = input('Temperature: ')
unc_unit = input('Unit: ')
c_unit = input('Unit of result: ')
temp = float(temp)
unc_unit = unc_unit[0].lower()
c_unit = c_unit[0].lower()


def output(x, y):
    print(f'The temperature in {x} is {y}')


if unc_unit == 'c' and c_unit == 'f':
    c_unit = 'Fahrenheit'
    con_temp = 32 + 1.8 * temp
    output(c_unit, con_temp)
elif unc_unit == 'f' and c_unit == 'c':
    c_unit = 'Celsius'
    con_temp = (temp - 32) * 0.5556
    output(c_unit, con_temp)
elif unc_unit == 'c' and c_unit == 'k':
    c_unit = 'Kelvin'
    con_temp = temp + 273
    output(c_unit, con_temp)
elif unc_unit == 'k' and c_unit == 'c':
    c_unit = 'Celsius'
    con_temp = temp - 273
    output(c_unit, con_temp)
elif unc_unit == 'f' and c_unit == 'k':
    c_unit = 'Kelvin'
    con_temp = (temp + 459.67) * 0.556
    output(c_unit, con_temp)
elif unc_unit == 'k' and c_unit == 'f':
    c_unit = 'Fahrenheit'
    con_temp = 32 + 1.8 * (temp - 273)
    output(c_unit, con_temp)
else:
    print('Invalid')
