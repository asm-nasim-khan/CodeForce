size = int(input())
passengers = 0
max_seat = 0
for station_no in range(size):
    passengers_count = input()
    values = passengers_count.split()
    people_out = int(values[0])
    people_in = int(values[1])
    passengers -= people_out
    passengers += people_in
    if passengers > max_seat:
        max_seat = passengers
print(max_seat)
