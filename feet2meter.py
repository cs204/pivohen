def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

def feet2meter(v):
    feet = float(v.replace('ft', ''))
    meters = feet * 0.3048

    return meters


main()