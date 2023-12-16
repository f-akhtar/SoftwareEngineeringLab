import matplotlib.pyplot as plt

def weather_model(time, a, b, c):
    # Quadratic equation for temperature change over time
    temperature_change = a * time**2 + b * time + c
    return temperature_change

def plot_weather_model(coefficients, start_time, end_time):
    # Plotting the weather model for each set of coefficients
    time_values = list(range(start_time, end_time + 1))

    plt.figure(figsize=(10, 6))
    plt.title("Weather Models for Multiple Sets of Coefficients")
    plt.xlabel("Time")
    plt.ylabel("Temperature Change")

    for i, (a, b, c) in enumerate(coefficients):
        temperature_changes = [weather_model(time, a, b, c) for time in time_values]
        label = f"Set {i + 1} - a={a}, b={b}, c={c}"
        plt.plot(time_values, temperature_changes, label=label)

    plt.legend()
    plt.show()

def main():
    # Read multiple sets of coefficients from file
    with open('multiple_coefficients.txt', 'r') as file:
        lines = file.readlines()
        coefficients = [tuple(map(float, line.strip().split())) for line in lines]

    # Get user input for time range
    start_time = int(input("Enter the start time: "))
    end_time = int(input("Enter the end time: "))

    # Plot weather models for multiple sets of coefficients
    plot_weather_model(coefficients, start_time, end_time)

if __name__ == "__main__":
    main()
