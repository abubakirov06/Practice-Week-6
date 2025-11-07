def summarize_sensor_data(data):
    new_data = []
    copy_of_data = data[:]
    copy_of_data.sort()
    count = 0
    for i in range(1, len(copy_of_data)):
        if copy_of_data[i-1][0] != copy_of_data[i][0]:
            new_data.append(copy_of_data[i-1])
            if i == len(copy_of_data) - 1:
                new_data.append(copy_of_data[i])
                count += 1
        if i == len(copy_of_data) - 1 and count == 0:
            new_data.append(copy_of_data[i])
            # for j in range(len(new_data)):
            #     if copy_of_data[i][0] in new_data[j]:
            #        new_data[j] = copy_of_data[i]
            #        count = 0
            

    
    return new_data

readings = [
	('SensorB', 25.4),
	('SensorA', 22.1),
	('SensorB', 26.1), 
	('SensorC', 30.5),
	('SensorA', 21.9), 
	('SensorB', 25.9)
]
print()
print(readings)
new_readings = summarize_sensor_data(readings)
print(new_readings)
print()