def calculate_fuel_percentage(fraction_str):
    while True:
        try:
            x, y = map(int, fraction_str.split('/'))
            if y == 0 or x > y:
                raise ValueError

            percentage = (x / y) * 100
            if percentage <= 1:
                return 'E'
            elif percentage >= 99:
                return 'F'
            else:
                return str(round(percentage)) + '%'
        except ValueError:
            fraction_str = input("Ошибка. X или Y не целые, X больше чем Y. Введите снова: ")
        except ZeroDivisionError:
            fraction_str = input("Ошибка. Y не может быть равен 0. Введите снова: ")

if __name__ == '__main__':
    fraction = input("Дробь: ")
    result = calculate_fuel_percentage(fraction)
    print(result)