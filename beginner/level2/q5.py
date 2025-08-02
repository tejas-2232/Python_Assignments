def analyze_weather_data(temp):
    if not temp:
        return None, None, None
    
    avg_temp = sum(temp)/len(temp)
    high_temp = max(temp)
    low_temp = min(temp)
    
    return avg_temp, high_temp, low_temp

def main():
    temp_input = input("Enter temperature: ")
    temp = list(map(float, temp_input.split()))
    
    # Check if input is valid
    if not temp:
        print("No temperature readings provided!")
        return
    
    average, highest, lowest = analyze_weather_data(temp)
    
    # Display results
    print(f"Average Temperature: {average}")
    print(f"Highest Temperature: {int(highest)}")
    print(f"Lowest Temperature: {int(lowest)}")

if __name__ == "__main__":
    main()