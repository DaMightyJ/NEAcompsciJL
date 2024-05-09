import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import atexit

# Global variables to store weight and height
init_weight = None
init_height = None

# Global variables to store the canvases in order to show the graphs on the program
calorie_canvas = None
sleep_canvas = None
weight_canvas = None
fitness_canvas = None


#initialisation function
def initial_data_saving():
    try:
        global init_weight, init_height
        init_weight = float(init_weight_entry.get())
        init_height = float(init_height_entry.get())
        if init_weight > 40 and init_weight < 140 and init_height > 140 and init_height < 210:
            messagebox.showinfo("Success",
                                "Initial weight: " + str(init_weight) + "\nInitial height: " + str(init_height))
            program_start_button.config(state="normal")
        elif init_weight < 40 or init_weight > 140 or init_height < 40 or init_height > 210:
            messagebox.showinfo("Error",
                                "Invalid height and/or weight(Unrealistic)! Please re-enter valid height and weight.")
            program_start_button.config(state="disabled")
        else:
            messagebox.showinfo("Error", "Invalid height and/or weight type! Please re-enter valid height and weight.")
            program_start_button.config(state="disabled")
    except ValueError:
        messagebox.showinfo("Error", "Invalid height and/or weight type! Please re-enter valid height and weight.")
        program_start_button.config(state="disabled")

#frame navigation functions
def frame_tracker(frame_no):
    global live_frame
    live_frame.pack_forget()
    live_frame = frames[frame_no]
    live_frame.pack()


def show_main_frame():
    frame_tracker(1)

#Calorie functions
def calories_data():
    try:
        calories = int(cal_entry.get())
        if calories > 1000 and calories < 20000:
            with open("calories.txt", "a") as file:
                file.write(str(calories) + "\n")
                messagebox.showinfo("Cal-Data", "Calories saved")
        else:
            messagebox.showinfo("Error","Unreasonable input! Try again")
    except ValueError:
        messagebox.showinfo("Error","Invalid data input! Try again")


def calorie_graph():
    global calorie_canvas
    try:
        calorie_canvas.get_tk_widget().destroy()
    except AttributeError:
        pass
    with open("calories.txt", "r") as file:
        data = file.readlines()
    data = [int(d.strip()) for d in data]

    fig, ax = plt.subplots()
    ax.bar(range(len(data)), data)
    ax.axhline(y=init_weight/(init_height*init_height*0.0001)*90, color='black', linestyle='--')
    ax.set_title("Calorie Graph")
    ax.set_xlabel("Days")
    ax.set_ylabel("Calories")


    calorie_canvas = FigureCanvasTkAgg(fig, master=Calories)
    calorie_canvas.draw()
    calorie_canvas.get_tk_widget().pack()


def clear_calories_file():
    with open("calories.txt", "w") as file:
        file.write("")

#Sleep functions
def sleep_data():
    try:
        hours = int(sleep_entry.get())
        if hours > 0 and hours < 24:
            with open("sleep.txt", "a") as file:
                file.write(str(hours) + "\n")
                messagebox.showinfo("Sleep-data", "Sleep saved")
        else:
            messagebox.showinfo("Error","Unreasonable input! Try again")
    except ValueError:
        messagebox.showinfo("Error","Invalid data input! Try again")


def sleep_display():
    global sleep_canvas
    try:
        sleep_canvas.get_tk_widget().destroy()
    except AttributeError:
        pass
    with open("sleep.txt", "r") as file:
        data = file.readlines()
    data = [int(d.strip()) for d in data]

    fig, ax = plt.subplots()
    ax.bar(range(len(data)), data)
    ax.axhline(y=8, color='black', linestyle='--')
    ax.set_title("Sleep Graph")
    ax.set_xlabel("Days")
    ax.set_ylabel("Sleep Hours")


    sleep_canvas = FigureCanvasTkAgg(fig, master=Sleep)
    sleep_canvas.draw()
    sleep_canvas.get_tk_widget().pack()


def clear_sleep_file():
    with open("sleep.txt", "w") as file:
        file.write("")
#weight functions
def weight_data_entered():
    weight = float(weight_entry.get())
    return weight

def weight_data():
    try:
        weight = int(weight_entry.get())
        if weight > 40 and weight < 210:
            with open("weight.txt", "a") as file:
                file.write(str(weight) + "\n")
                messagebox.showinfo("Weight-data", "Weight saved")
        else:
            messagebox.showinfo("Error","Unreasonable input! Try again")
    except ValueError:
        messagebox.showinfo("Error","Invalid data input! Try again")


def weight_display():
    global weight_canvas
    try:
        weight_canvas.get_tk_widget().destroy()
    except AttributeError:
        pass
    with open("weight.txt", "r") as file:
        data = file.readlines()
    data = [int(d.strip()) for d in data]

    fig, ax = plt.subplots()
    ax.plot(range(len(data)), data, marker='o', linestyle='-')
    ax.axhline(y=0.9 * init_weight, color='black', linestyle='--')
    ax.set_xlabel("Days")
    ax.set_ylabel("Weight (kg)")
    ax.set_title("Weight Graph")

    weight_canvas = FigureCanvasTkAgg(fig, master=Weight)
    weight_canvas.draw()
    weight_canvas.get_tk_widget().pack()


def clear_weight_file():
    with open("weight.txt", "w") as file:
        file.write("")

#fitness functions
def cal_loss_data():
    try:
        calorie_loss = int(cal_loss_entry.get())
        if calorie_loss > 50 and calorie_loss  < 600:
            with open("cal_loss.txt", "a") as file:
                file.write(str(calorie_loss) + "\n")
            messagebox.showinfo("Cal-loss-data", "Cal-loss data saved")
        else:
            messagebox.showinfo("Error","Unreasonable input! Try again")
    except ValueError:
        messagebox.showinfo("Error","Invalid data input! Try again")


def cal_loss_display():
    global fitness_canvas
    try:
        fitness_canvas.get_tk_widget().destroy()
    except AttributeError:
        pass
    with open("cal_loss.txt", "r") as file:
        data = file.readlines()
    data = [int(d.strip()) for d in data]

    fig, ax = plt.subplots()
    ax.bar(range(len(data)), data)
    ax.axhline(y=init_weight/(init_height*init_height*0.0001)*9, color='black', linestyle='--')
    ax.set_xlabel("Days")
    ax.set_ylabel("Calories Burned")
    ax.set_title("Calories Burned Graph")

    fitness_canvas = FigureCanvasTkAgg(fig, master=Fitness)
    fitness_canvas.draw()
    fitness_canvas.get_tk_widget().pack()


def clear_calorie_loss_file():
    with open("cal_loss.txt", "w") as file:
        file.write("")

def colour_changer(colour_no):
    if colour_no == 0:
        root.config(bg="white")
    elif colour_no == 1:
        root.config(bg="dark blue")
    else:
        root.config(bg="light pink")

#Clearing out files when project closes
atexit.register(clear_calories_file)
atexit.register(clear_sleep_file)
atexit.register(clear_weight_file)
atexit.register(clear_calorie_loss_file)

root = tk.Tk()
root.geometry("800x800")
root.resizable(False, False)
root.title("Macro-fitness Tracker")

# Initialisation frame
init_frame = tk.Frame(root)
init_label = tk.Label(init_frame, text="Enter Initial Weight and Height", font=("Sans-serif", 20))
init_label.pack(pady=20)

init_weight_label = tk.Label(init_frame, text="Weight (kg): ", font=("Sans-serif", 15))
init_weight_label.pack(pady=5)
init_weight_entry = ttk.Entry(init_frame, width=10, font=("Sans-serif", 15))
init_weight_entry.pack(pady=5)
init_weight_entry.bind('<Return>', lambda event=None: init_height_entry.focus())

init_height_label = tk.Label(init_frame, text="Height (cm): ", font=("Sans-serif", 15))
init_height_label.pack(pady=5)
init_height_entry = ttk.Entry(init_frame, width=10, font=("Sans-serif", 15))
init_height_entry.pack(pady=5)
init_height_entry.bind('<Return>', lambda event=None: initial_data_saving())

program_start_button = tk.Button(init_frame, text="Continue", command=show_main_frame, state="disabled")
program_start_button.pack(pady=10)

# Main frame
main_frame = tk.Frame(root)
main_title = tk.Label(main_frame, text="Main Page", font=("Sans-serif", 40))
main_title.pack(pady=10)



# Buttons section
def main_button(button_name, button_no, button_colour):
    button = tk.Button(main_frame, text=button_name, command=lambda: frame_tracker(button_no + 1), bg=button_colour, fg="white")
    button.pack(side = tk.TOP, padx=5, pady=24,ipadx = 20, ipady = 30,expand=tk.FALSE)

main_button("Calories", 1,"green")
main_button("Weight", 2,"yellow")
main_button("Sleep", 3,"blue")
main_button("Fitness", 4,"orange")
main_button("Colour", 5, "pink")

check_init = tk.Button(main_frame, text="Check initial values", command=lambda:messagebox.showinfo("Initial values",f"Initial weight is {init_weight}kg and initial height is {init_height}cm"))
check_init.pack(pady=10, side=tk.TOP, expand = tk.TRUE)

# Frames section

#Calories Buttons

Calories = tk.Frame(root)
start1 = tk.Label(Calories, text="Calories", font=("Sans-serif", 40))
start1.pack(pady=10)

cal_label = tk.Label(Calories, text="Enter Calories:", font=("Sans-serif", 15))
cal_label.pack(pady=5)
cal_entry = ttk.Entry(Calories, width=10, font=("Sans-serif", 15))
cal_entry.pack(pady=5)

cal_submit_button = ttk.Button(Calories, text="Submit", command=calories_data)
cal_submit_button.pack(pady=10)

cal_graph_button = ttk.Button(Calories, text="Show Chart", command=calorie_graph)
cal_graph_button.pack(pady=10)

check_1 = tk.Button(Calories, text="Check Calorie Goal", command=lambda:messagebox.showinfo("Calorie Goal",f"Calorie Goal is {init_weight/(init_height*init_height*0.0001)*90}"))
check_1.pack(pady=10)

back_button1 = tk.Button(Calories, text="Back to Main", command=show_main_frame)
back_button1.pack(side=tk.BOTTOM, expand=True)

#Weight Buttons

Weight = tk.Frame(root)
start2 = tk.Label(Weight, text="Weight", font=("Sans-serif", 40))
start2.pack(pady=10)

weight_label = tk.Label(Weight, text="Enter Weight:", font=("Sans-serif", 15))
weight_label.pack(pady=5)
weight_entry = ttk.Entry(Weight, width=10, font=("Sans-serif", 15))
weight_entry.pack(pady=5)

weight_submit_button = ttk.Button(Weight, text="Submit", command=weight_data)
weight_submit_button.pack(pady=10)

weight_graph_button = ttk.Button(Weight, text="Show Chart", command=weight_display)
weight_graph_button.pack(pady=10)

check_2 = tk.Button(Weight, text="Check Weight Goal", command=lambda:messagebox.showinfo("Weight Goal",f"Weight Goal is {init_weight*0.9}"))
check_2.pack(pady=10)

back_button2 = tk.Button(Weight, text="Back to Main", command=show_main_frame)
back_button2.pack(side=tk.BOTTOM, expand=True)


#Sleep Buttons

Sleep = tk.Frame(root)
start3 = tk.Label(Sleep, text="Sleep", font=("Sans-serif", 40))
start3.pack(pady=10)

sleep_label = tk.Label(Sleep, text="Input hours of sleep here", font=("Sans-serif", 25))
sleep_label.pack(pady=15)
sleep_entry = ttk.Entry(Sleep, width=10, font=("Sans-serif", 15))
sleep_entry.pack(pady=5)

sleep_submit_button = ttk.Button(Sleep, text="Submit", command=sleep_data)
sleep_submit_button.pack(pady=10)

sleep_graph_button = ttk.Button(Sleep, text="Show Chart", command=sleep_display)
sleep_graph_button.pack(pady=10)

check_3 = tk.Button(Sleep, text="Check Sleep Goal", command=lambda:messagebox.showinfo("Sleep Goal",f"Sleep Goal is 8 hours"))
check_3.pack(pady=10)

back_button3 = tk.Button(Sleep, text="Back to Main", command=show_main_frame)
back_button3.pack(side=tk.BOTTOM, expand=True)

#Fitness Buttons

Fitness = tk.Frame(root)
start4 = tk.Label(Fitness, text="Fitness", font=("Sans-serif", 40))
start4.pack(pady=10)

cal_loss_label = tk.Label(Fitness, text="Enter Calorie Loss:", font=("Sans-serif", 15))
cal_loss_label.pack(pady=5)
cal_loss_entry = ttk.Entry(Fitness, width=10, font=("Sans-serif", 15))
cal_loss_entry.pack(pady=5)

cal_loss_submit_button = ttk.Button(Fitness, text="Submit", command=cal_loss_data)
cal_loss_submit_button.pack(pady=10)

cal_loss_graph_button = ttk.Button(Fitness, text="Show Chart", command=cal_loss_display)
cal_loss_graph_button.pack(pady=10)

check_4 = tk.Button(Fitness, text="Check Calorie Loss Goal", command=lambda:messagebox.showinfo("Cal-Loss Goal",f"Calorie Loss Goal is {init_weight/(init_height*init_height*0.0001)*9}"))
check_4.pack(pady=10)

back_button4 = tk.Button(Fitness, text="Back to Main", command=show_main_frame)
back_button4.pack(side=tk.BOTTOM, expand=True)

#Colour Button
Colour = tk.Frame(root)

colour_label = tk.Label(Colour, text="Press if you want dark theme or light theme, or special pink theme", font=("Sans-serif", 20))
colour_label.pack(pady=5)

light_button = tk.Button(Colour, text="Light theme", font = ("Sans-serif",30), command = lambda: colour_changer(0))
light_button.pack()
dark_button = tk.Button(Colour, text="Dark theme", font = ("Sans-serif",30), command = lambda: colour_changer(1),bg = "dark blue", fg= "white")
dark_button.pack()
pink_button = tk.Button(Colour, text="Pink theme", font = ("Sans-serif",30), command = lambda: colour_changer(2),bg = "light pink", fg= "white")
pink_button.pack()

back_button5 = tk.Button(Colour, text="Back to Main", command=show_main_frame)
back_button5.pack(side=tk.BOTTOM, expand=True)

# Current frame
frames = [init_frame, main_frame, Calories, Weight, Sleep, Fitness, Colour]
live_frame = init_frame
live_frame.pack()

root.mainloop()
