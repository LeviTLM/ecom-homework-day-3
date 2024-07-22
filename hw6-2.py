import statistics

temperatures = []

while True:
    temp = float(input("Enter a temperature (enter -999 to stop): "))
    if temp == -999:
        break
    if -50 <= temp <= 50:
        temperatures.append(temp)
    else:
        print("Temperature must be between -50 and 50.")

additional_temps = [18.5, 39.1, -20.0]
temperatures.extend(additional_temps)

print("Highest temperature:", max(temperatures))
print("Lowest temperature:", min(temperatures))

average = sum(temperatures) / len(temperatures)
print("Average temperature (sum+len):", average)

average_using_mean = statistics.mean(temperatures)
print("Average temperature (statistics):", average_using_mean)

del temperatures[0]
temperatures.remove(18.5)
last_temp = temperatures.pop()

sorted_temperatures = sorted(temperatures.copy())
sorted_reverse_temperatures = sorted(temperatures.copy(), reverse=True)

print("Updated temperatures list:", temperatures)
print("Last temperature inserted:", last_temp)
print("Sorted temperatures:", sorted_temperatures)
print("Sorted temperatures in reverse:", sorted_reverse_temperatures)