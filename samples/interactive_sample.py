from pytemplate1.calculator import Calculator

def main():
    calc = Calculator()
    print("Interactive Calculator. Type 'exit' or 'quit' to end.")
    while True:
        try:
            line = input(">>> ").strip()
            if line.lower() in ["exit", "quit"]:
                break

            parts = line.split()
            if len(parts) != 3:
                print("Invalid input. Usage: <command> <num1> <num2>")
                continue

            command = parts[0].lower()
            try:
                num1 = float(parts[1])
                num2 = float(parts[2])
            except ValueError:
                print("Invalid numbers. Please enter numeric values.")
                continue

            if command == "add":
                result = calc.add(num1, num2)
                print(f"Result: {result}")
            elif command == "sub":
                result = calc.sub(num1, num2)
                print(f"Result: {result}")
            elif command == "mul":
                result = calc.mul(num1, num2)
                print(f"Result: {result}")
            elif command == "div":
                try:
                    result = calc.div(num1, num2)
                    print(f"Result: {result}")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print(f"Unknown command: {command}")

        except EOFError:
            print("\nExiting interactive mode.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
