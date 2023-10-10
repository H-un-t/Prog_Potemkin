def calculate_distance(vi, v2, t):
    initial_distance = 5
    total_distance = initial_distance+(vi+v2)*t
    return total_distance
speed1 =60
speed2 =80
time =2
distance = calculate_distance(speed1, speed2, time)
print('Расстояние между автомобилями через', time, 'часа:',distance, 'км')