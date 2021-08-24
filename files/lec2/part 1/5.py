#correct

vehicle_type = int(input())
hour = int(input())

if vehicle_type == 1:
    fee_1, time, fee_2 = [0.7, 3, 2.5]
elif vehicle_type == 2:
    fee_1, time, fee_2 = [1.5, 3, 2.0]
else:
    fee_1, time, fee_2 = [2.5, 2, 3.25]

if hour <= time:
    fee = fee_1 * hour
else:
    fee = fee_1 * time + fee_2 * (hour-time)
print('{:.2f}'.format(fee))