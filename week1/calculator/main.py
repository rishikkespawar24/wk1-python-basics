# main.py — Interactive Calculator (v1, robust)

def read_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def read_op(prompt: str) -> str:
    ops = {"+", "-", "*", "/"}
    while True:
        op = input(prompt).strip()
        if op in ops:
            return op
        print("Choose one of: +  -  *  /")

def calc(a: float, b: float, op: str) -> float:
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b
    raise ValueError("Unsupported operation")

def main():
    print("=== Calculator ===")
    while True:
        a = read_number("Enter first number: ")
        b = read_number("Enter second number: ")
        op = read_op("Enter operation (+, -, *, /): ")
        try:
            result = calc(a, b, op)
            print("Result:", result)
        except ZeroDivisionError as e:
            print("Error:", e)

        again = input("Another calculation? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()


