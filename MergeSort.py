import time


def merge_sort(data, draw_data, animation_time):
    merge_sort_algorithm(data, 0, len(data)-1, draw_data, animation_time)
    # len(data)-1 because index starts at 0.


def merge_sort_algorithm(data, left, right, draw_data, animation_time):
    if left < right:
        middle = (left+right)//2
        # recursion: first left part then right part
        merge_sort_algorithm(data, left, middle, draw_data, animation_time)
        merge_sort_algorithm(data, middle+1, right, draw_data, animation_time)
        merge(data, left, middle, right, draw_data, animation_time)


def merge(data, left, middle, right, draw_data, animation_time):

    draw_data(data, get_color_list(len(data), left, middle, right))
    time.sleep(animation_time)

    left_part = data[left:middle+1]  # middle+1 because we want to include it
    right_part = data[middle+1:right+1]

    left_index = right_index = 0

    for data_index in range(left, right+1):
        if left_index < len(left_part) and right_index < len(right_part):
            # if first element of left part is greater than right one then add first
            # element of left part else right part
            if left_part[left_index] <= right_part[right_index]:
                data[data_index] = left_part[left_index]
                left_index += 1
            else:
                data[data_index] = right_part[right_index]
                right_index += 1
        elif left_index < len(left_part):
            # If there is still some elements in the left part then we want to
            # simply add them into our sorted data
            data[data_index] = left_part[left_index]
            left_index += 1
        else:
            # Or if there is still some elements in the right part then we want to
            # add them into our sorted data
            data[data_index] = right_part[right_index]
            right_index += 1

    draw_data(data, ["green" if x >= left and x <=
                     right else "white" for x in range(len(data))])
    time.sleep(animation_time)


def get_color_list(length, left, middle, right):
    color_list = []

    for i in range(length):
        if i >= left and i <= middle:
            if i >= left and i <= middle:
                color_list.append("yellow")
            else:
                color_list.append("pink")
        else:
            color_list.append("white")

    return color_list


# data = [1, 5, 2, 5, 3, 2, 4]
# merge_sort(data, 0, 0)
# print(data)
