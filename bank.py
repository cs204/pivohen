def main():
    greeting = input("Приветствие: ")

    if greeting.lower().startswith("здравствуйте") :
        print("$0")
    elif greeting.lower().startswith("здрасте"):
        print("$20")
    else:
        print("$100")

    if greeting.lower().startswith("здравствуйте, человек"):
        print("$0")



main()