while True:
    try:
        start_degree = float(input('Enter a temperature: '))
        break
    except ValueError:
        print('ERROR. Not a number.')
        continue

start_unit_list = ['C', 'F', 'K']
start_unit = input('What unit is this? (C, F, K): ').upper()
while start_unit not in start_unit_list:
    print('ERROR. Not a valid unit. Please use "C", "F", or "K".')
    start_unit = input('What unit is this? (C, F, K): ').upper()

new_unit_list = ['C', 'F', 'K']
new_unit = input('What unit do you want? (C, F, K): ').upper()
while new_unit not in new_unit_list or start_unit == new_unit:
    print('ERROR. Not a valid input. Value either same as starting unit or not "C", "F", or "K". ')
    new_unit = input('What unit do you want? (C, F, K): ').upper()

new_degree = 'ERROR'


def c_f(start_degree, new_degree):
    new_degree = (9.0 / 5.0) * start_degree + 32
    print(start_degree, start_unit, 'is', new_degree, new_unit)


def c_k(start_degree, new_degree):
    new_degree = start_degree + 273.15
    print(start_degree, start_unit, 'is', new_degree, new_unit)


def f_c(start_degree, new_degree):
    new_degree = (start_degree - 32) * (5.0 / 9.0)
    print(start_degree, start_unit, 'is', new_degree, new_unit)


def f_k(start_degree, new_degree):
    new_degree = ((start_degree - 32) * 5) / 9 + 273.15
    print(start_degree, start_unit, 'is', new_degree, new_unit)


def k_c(start_degree, new_degree):
    new_degree = start_degree - 273.15
    print(start_degree, start_unit, 'is', new_degree, new_unit)


def k_f(start_degree, new_degree):
    new_degree = ((start_degree - 273.15) * 1.8) + 32
    print(start_degree, start_unit, 'is', new_degree, new_unit)


if start_unit == 'C' and new_unit == 'F': c_f(start_degree, new_degree)

if start_unit == 'C' and new_unit == 'K': c_k(start_degree, new_degree)

if start_unit == 'F' and new_unit == 'C': f_c(start_degree, new_degree)

if start_unit == 'F' and new_unit == 'K': f_k(start_degree, new_degree)

if start_unit == 'K' and new_unit == 'C': k_c(start_degree, new_degree)

if start_unit == 'K' and new_unit == 'F': k_f(start_degree, new_degree)
