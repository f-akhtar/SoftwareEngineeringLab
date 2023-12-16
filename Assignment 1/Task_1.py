def weather_model(time):
    # Fixed variables
    a = 0.1  # Coefficient for the quadratic term
    b = 2.0  # Coefficient for the linear term
    c = 10.0  # Constant term

    # Quadratic equation for temperature change over time
    temperature_change = a * time**2 + b * time + c

    return temperature_change

def main():
    # Time values from 0 to 10 (you can adjust this range)
    time_values = range(11)

    # Display the weather model for each time value
    for time in time_values:
        temperature_change = weather_model(time)
        print(f"Time: {time} hours, Temperature Change: {temperature_change} degrees")

if __name__ == "__main__":
    main()
