import matplotlib.pyplot as plt

def weather_model(time, a, b, c):
    # Quadratic equation for temperature change over time
    temperature_change = a * time**2 + b * time + c
    return temperature_change

def plot_weather_model(coefficients, start_time, end_time, graph_type):
    # Plotting the weather model based on user input
    time_values = list(range(start_time, end_time + 1))

    plt.figure(figsize=(10, 6))
    plt.title("Weather Model")
    plt.xlabel("Time")
    plt.ylabel("Temperature Change")

    for a, b, c in coefficients:
        temperature_changes = [weather_model(time, a, b, c) for time in time_values]
        
        if graph_type == 'line':
            plt.plot(time_values, temperature_changes, label=f"a={a}, b={b}, c={c}")
        elif graph_type == 'scatter':
            plt.scatter(time_values, temperature_changes, label=f"a={a}, b={b}, c={c}")
    
    plt.legend()
    plt.show()

def main():
    # Fixed variables
    fixed_a = 0.1
    fixed_b = 2.0
    fixed_c = 10.0

    # Get user input for additional coefficients
    user_a = float(input("Enter the coefficient for the quadratic term (a): "))
    user_b = float(input("Enter the coefficient for the linear term (b): "))
    user_c = float(input("Enter the constant term (c): "))

    # Combine fixed and user-input coefficients
    coefficients = [
        (fixed_a, fixed_b, fixed_c),
        (user_a, user_b, user_c)
    ]

    # Get user input for time range
    start_time = int(input("Enter the start time: "))
    end_time = int(input("Enter the end time: "))

    # Get user input for graph type
    graph_type = input("Enter the graph type (line/scatter): ").lower()

    # Plot weather models based on user input
    plot_weather_model(coefficients, start_time, end_time, graph_type)

if __name__ == "__main__":
    main()
