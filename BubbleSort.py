import time


def bubble_sort(data, draw_data, animation_time):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                draw_data(data, ["#9BC1BC" if x == j or x == j +
                                 1 else "#FF8A5B" for x in range(len(data))])
                time.sleep(animation_time)
    draw_data(data, ["#E76F51" for _ in range(len(data))])
