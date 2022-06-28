temp = input('Temperature: ')
unc_unit = input('Unit: ')
c_unit = input('Unit of resault: ')
unc_unit = unc_unit[0].lower()
c_unit = c_unit[0].lower()
if unc_unit == 'c' and c_unit == 'f':
    con_temp = 32 + 1.8 * float(temp)
    print('The temperature in farenheit is ' + str(con_temp))
elif unc_unit == 'f' and c_unit == 'c':
    con_temp = (float(temp) - 32) * 0.5556
    print('The temperature in celcious is ' + str(con_temp))
elif unc_unit == 'c' and c_unit == 'k':
    con_temp = float(temp) + 273
    print('The temperature in kelvin is ' + str(con_temp))
elif unc_unit == 'k' and c_unit == 'c':
    con_temp = float(temp) - 273
    print('The temperature in celcious is ' + str(con_temp))
elif unc_unit == 'f' and c_unit == 'k':
    con_temp = (float(temp) + 459.67) * 0.556
    print('The temperature in kelvin is ' + str(con_temp))
elif unc_unit == 'k' and c_unit == 'f':
    con_temp = 32 + 1.8 * (float(temp) - 273)
    print('The temperature in farenheit is ' + str(con_temp))
else:
    print('Invalid')
