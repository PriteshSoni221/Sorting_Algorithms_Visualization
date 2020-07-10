import tkinter as tk
from tkinter import ttk
import random
from PIL import Image, ImageTk
from BubbleSort import bubble_sort  # importing bubble_sort function

# variables
min_height, min_width = 1200, 700
data = []


# functions
def resize_image(event):
    # This function is to resize the background wallpaper
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo


def draw_data(data, color_list):
    canvas.delete("all")
    canvas_height = 380
    canvas_width = 600
    x_width = canvas_width / (len(data) + 1)
    offset = 30  # some space from the border
    padding = 10  # space between bars
    # using list comprehension below to get a list of all the normalised data
    normalise_data = [i / max(data) for i in data]

    for i, height in enumerate(normalise_data):  # enumerate keeps track of count
        # top left
        x0 = i * x_width + offset + padding
        y0 = canvas_height - height * 340
        # bottom right
        x1 = (i+1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_list[i])  # "#E76F51"
        canvas.create_text(x0+2, y0, anchor="sw", text=(data[i]))
    root.update_idletasks()
    root.update()


def generate_arrays():
    global data
    min_num = int(min_num_scale.get())
    max_num = int(max_num_scale.get())
    num_of_elements = int(num_of_elements_scale.get())
    data = []
    for _ in range(num_of_elements):
        data.append(random.randrange(min_num, max_num+1))  # (max_num +1) because it is exclusive
    draw_data(data, ["#FF8A5B" for _ in range(len(data))])


def start_algorithm():
    global data
    selectedAlgo = algo_list.get("anchor")
    print("Selected Algorithm "+selectedAlgo)
    print(data)
    bubble_sort(data, draw_data, speed_scale.get())


# initializing root
root = tk.Tk()
root.title("Sorting Algorithm Visualization")
root.configure(background='#A7A2A9')
root.minsize(min_height, min_width)
root.geometry('900x700')
selectedAlgo = tk.StringVar()

# setting background wallpaper
image = Image.open(
    '/Users/priteshsoni/Documents/GitHub/sorting_algorithm_visualization/triangles.png')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image=photo)
label.bind('<Configure>', resize_image)
label.pack(fill="both", expand="yes")

# for element control - upper frame
upper_frame = tk.Frame(root, bg="#EDAFB8", highlightthickness=2)
upper_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.15)


# for algo choice - right frame
right_frame = tk.Frame(root, bg="#F7E1D7", highlightthickness=2)
right_frame.place(relx=0.7, rely=0.37, relwidth=0.2, relheight=0.45)

# for graphs - canvas
canvas = tk.Canvas(root, bg="#F7E1D7", bd=0, highlightthickness=2)
canvas.place(relx=0.1, rely=0.3, relwidth=0.55, relheight=0.6)

# widgets on the upper frame
num_of_elements_scale = tk.Scale(upper_frame, from_=3, to=30,
                                 orient="horizontal", label="Total Elements", troughcolor="#4A5759", bg="#E76F51",
                                 font=("Plantagenet Cherokee", 16))
num_of_elements_scale.place(relx=0.05, rely=0.2, width=150, height=60)

min_num_scale = tk.Scale(upper_frame, from_=0, to=10,
                         orient="horizontal", label="Minimum Number", troughcolor="#4A5759", bg="#F7E1D7",
                         font=("Plantagenet Cherokee", 16))
min_num_scale.place(relx=0.34, rely=0.2, width=150, height=60)

max_num_scale = tk.Scale(upper_frame, from_=10, to=100,
                         orient="horizontal", label="Maximum Number", troughcolor="#4A5759", bg="#AFC97E",
                         font=("Plantagenet Cherokee", 16))
max_num_scale.place(relx=0.63, rely=0.2, width=150, height=60)

# to generate an array
generate_button = tk.Button(upper_frame, text="Generate\nArray",
                            command=generate_arrays, bg="#036D19",
                            font=("Plantagenet Cherokee", 16))
generate_button.place(relx=0.88, rely=0.2, width=64, height=64)


# widgets on the right frame
algo_label = tk.Label(right_frame, text="Select Algorithm", bg="#EDAFB8",
                      font=("Plantagenet Cherokee", 18))
algo_label.place(relx=0.1, rely=0.05, relwidth=0.8)

# First idea was to use a combobox for algo but i might not use it
# algo_list = ttk.Combobox(right_frame, textvariable=selectedAlgo,
#                          values=['Bubble Sort', 'Merge Sort'])
# algo_list.place(relx=0.1, rely=0.12, relwidth=0.8)
# algo_list.current(0)

# Instead I am using a list box which is better in this case
algo_list = tk.Listbox(right_frame, bg="#F3DE2C",
                       font=("Plantagenet Cherokee", 18))
algo_list.insert(1, "Merge Sort")
algo_list.insert(2, "Bubble Sort")
algo_list.insert(3, "Quick Sort")
algo_list.insert(4, "Insertion Sort")
algo_list.insert(5, "Heap Sort")
algo_list.place(relx=0.1, rely=0.20, height=120, width=100)

speed_scale = tk.Scale(right_frame, from_=0.1, to=2.0,
                       orient="horizontal", label="Animation Speed(s)", troughcolor="#4A5759", bg="#EDAFB8",
                       font=("Plantagenet Cherokee", 16), resolution=0.2)
speed_scale.place(relx=0.1, rely=0.65, width=150, height=60)

start_button = tk.Button(right_frame, text="Start Sorting",
                         command=start_algorithm,
                         font=("Plantagenet Cherokee", 16), bg="#EDAFB8")
start_button.place(relx=0.1, rely=0.9, relwidth=0.8)

root.mainloop()
