def process_temperature_readings():
    total = 0
    count = 0
     
    while True:
        raw_value = input("Enter temperature (or 'done' to stop): ")
        
        if raw_value == "done":
            break
            
        number = float(raw_value)
        total = total + number
        count = count + 1
     
    if count > 0:
        average = total / count
        print(f"Average temperature: {average}")
    else:
        print("No temperatures were entered")

# Call the function to run it
process_temperature_readings()