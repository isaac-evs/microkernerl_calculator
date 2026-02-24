from kernel import CalculatorKernel


def main():
    app = CalculatorKernel()
    app.load_plugins()

    print("--- Microkernel Calculator ---")
    try:
        val1 = float(input("First number: "))
        op = input("Operation (+, -, *, /): ")
        val2 = float(input("Second number: "))

        result = app.compute(op, val1, val2)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
