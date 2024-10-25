import datetime

# List to store patient data
patients = []

# Function to add a patient
def add_patient(name, arrival_time):
    # Convert arrival_time to a datetime object
    arrival_time = datetime.datetime.strptime(arrival_time, "%H:%M")
    # Assume consultation starts immediately for simplicity
    start_time = datetime.datetime.now()
    waiting_time = (start_time - arrival_time).total_seconds() / 60  # Waiting time in minutes
    
    # Create a patient record
    patient_record = {
        'name': name,
        'arrival_time': arrival_time.strftime("%H:%M"),
        'start_time': start_time.strftime("%H:%M"),
        'waiting_time': waiting_time
    }
    
    # Add patient record to the list
    patients.append(patient_record)

# Function to convert minutes to hours and days
def convert_time(minutes):
    hours = minutes // 60
    days = hours // 24
    remaining_hours = hours % 24
    remaining_minutes = minutes % 60
    return days, remaining_hours, remaining_minutes

# Function to display waiting statistics
def display_statistics():
    total_waiting_time = sum(patient['waiting_time'] for patient in patients)
    
    average_waiting_time = total_waiting_time / len(patients) if patients else 0
    max_waiting_time = max(patient['waiting_time'] for patient in patients) if patients else 0
    min_waiting_time = min(patient['waiting_time'] for patient in patients) if patients else 0
    
    # Convert times to days, hours, and minutes
    total_days, total_hours, total_minutes = convert_time(total_waiting_time)
    avg_days, avg_hours, avg_minutes = convert_time(average_waiting_time)
    max_days, max_hours, max_minutes = convert_time(max_waiting_time)
    min_days, min_hours, min_minutes = convert_time(min_waiting_time)

    print("\n--- Patient Waiting Time Statistics ---")
    print(f"Total Patients: {len(patients)}")
    print(f"Total Waiting Time: {total_days} days, {total_hours} hours, {total_minutes:.2f} minutes")
    print(f"Average Waiting Time: {avg_days} days, {avg_hours} hours, {avg_minutes:.2f} minutes")
    print(f"Maximum Waiting Time: {max_days} days, {max_hours} hours, {max_minutes:.2f} minutes")
    print(f"Minimum Waiting Time: {min_days} days, {min_hours} hours, {min_minutes:.2f} minutes")

# Main loop to take user input
def main():
    while True:
        name = input("Enter patient name (or type 'exit' to finish): ")
        if name.lower() == 'exit':
            break
        
        arrival_time = input("Enter arrival time (HH:MM format): ")
        try:
            add_patient(name, arrival_time)
        except ValueError:
            print("Invalid time format. Please enter time in HH:MM format.")
    
    # Display statistics after input is finished
    display_statistics()

# Run the program
if __name__ == "__main__":
    main()
