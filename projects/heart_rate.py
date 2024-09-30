"""
    This program will ask user input for their heartrate at specific times
    and then average them and display the data to the terminal
"""

time_slots = ["Morning", "Midday", "Afternoon", "Evening"]
heart_rates = []
total = 0
average = 0

for time in time_slots:
    heart_rate_temp = input(f"Enter your heart rate for {time}: ")
    heart_rates.append([time, heart_rate_temp])
print(heart_rates)

for i in range(4):
    time = heart_rates[i][0]
    heart_rate = heart_rates[i][1]
    total += int(heart_rate)
    print(f"At {time}, your heart rate was: {heart_rate} BPM")

average = total / 4
print(f"Your average heart rate was {average} BPM.")