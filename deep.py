def main():
    user_input = input("Какой ответ на главный вопрос жизни, вселенной и всего такого? ")
    user_input_lower = user_input.lower()

    if user_input_lower == "42" or user_input_lower == "сорок два":
        print("Да")
    else:
        print("Нет")

main()