def weather_model(time, a, b, c):
    # Quadratic equation for temperature change over time
    temperature_change = a * time**2 + b * time + c
    return temperature_change

def main():
    # Read coefficients from file
    with open('coefficients.txt', 'r') as file:
        lines = file.readlines()
        a = float(lines[0].strip())
        b = float(lines[1].strip())
        c = float(lines[2].strip())

    # Get user input for time range
    start_time = int(input("Enter the start time: "))
    end_time = int(input("Enter the end time: "))

    # Display the weather model for each time value in the specified range
    print("\nWeather Model:")
    print("---------------")
    print("| Time | Temperature Change |")
    print("---------------")

    for time in range(start_time, end_time + 1):
        temperature_change = weather_model(time, a, b, c)
        print(f"| {time}   | {temperature_change:.2f}                 |")

if __name__ == "__main__":
    main()
