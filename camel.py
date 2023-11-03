def camel_to_snake(camel_case):
    snake_case = 'Верблюжий стиль: '
    for char in camel_case:
        if char.isupper():
            snake_case += '_' + char.lower()
        else:
            snake_case += char
    if snake_case.startswith('_'):
        snake_case = snake_case[1:]
    return snake_case

def main():
    camel_case_name = input()
    snake_case_name = camel_to_snake(camel_case_name)
    print(snake_case_name)

main()