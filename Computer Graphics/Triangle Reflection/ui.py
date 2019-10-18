from tkinter import *
from tkinter import messagebox


# Check if triangle is not degenerate
def is_triangle_check(x_a, y_a, x_b, y_b, x_c, y_c):
    is_triangle = False

    side_a = ((x_b - x_a) * (x_b - x_a) + (y_b - y_a) * (y_b - y_a)) ** (1 / 2)
    side_b = ((x_c - x_b) * (x_c - x_b) + (y_c - y_b) * (y_c - y_b)) ** (1 / 2)
    side_c = ((x_c - x_a) * (x_c - x_a) + (y_c - y_a) * (y_c - y_a)) ** (1 / 2)

    if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
        is_triangle = True

    return is_triangle


# Check and return parameters
def return_parameters(x_a, y_a, x_b, y_b, x_c, y_c,
                      k, b, triangle, line, root):
    try:
        # Check entered values
        x_a_num = float(x_a.get())
        y_a_num = float(y_a.get())
        x_b_num = float(x_b.get())
        y_b_num = float(y_b.get())
        x_c_num = float(x_c.get())
        y_c_num = float(y_c.get())

        k_num = float(k.get())
        b_num = float(b.get())

        # Check if triangle is not degenerate
        is_triangle = is_triangle_check(x_a_num, y_a_num, x_b_num, y_b_num, x_c_num, y_c_num)
        if not is_triangle:
            raise Warning

        # Write parameters to objects if it's possible
        triangle.x_a = x_a_num
        triangle.y_a = y_a_num
        triangle.x_b = x_b_num
        triangle.y_b = y_b_num
        triangle.x_c = x_c_num
        triangle.y_c = y_c_num

        line.k = k_num
        line.b = b_num

        line.print_value()
        root.destroy()

    except ValueError:
        messagebox.showinfo("Parameters Error", "Not all parameters are numbers")
    except Warning:
        messagebox.showinfo("Parameters Error", "A triangle with such coordinates is degenerate")


# Create UI
def ui_window(triangle, line):
    # Create root window
    root = Tk()
    root.title("Triangle reflection")

    root.geometry('550x400')

    # Triangle
    coordinates = Label(text="Triangle coordinates", font='Helvetica 18 bold')
    coordinates.grid(row=0, column=1, sticky="n")

    x_a = StringVar()
    y_a = StringVar()
    x_b = StringVar()
    y_b = StringVar()
    x_c = StringVar()
    y_c = StringVar()

    x_a_label = Label(text="X_1:")
    y_a_label = Label(text="Y_1:")
    x_b_label = Label(text="X_2:")
    y_b_label = Label(text="Y_2:")
    x_c_label = Label(text="X_3:")
    y_c_label = Label(text="Y_3:")

    x_a_label.grid(row=1, column=0, sticky="w")
    y_a_label.grid(row=2, column=0, sticky="w")
    x_b_label.grid(row=3, column=0, sticky="w")
    y_b_label.grid(row=4, column=0, sticky="w")
    x_c_label.grid(row=5, column=0, sticky="w")
    y_c_label.grid(row=6, column=0, sticky="w")

    x_a_entry = Entry(textvariable=x_a)
    y_a_entry = Entry(textvariable=y_a)
    x_b_entry = Entry(textvariable=x_b)
    y_b_entry = Entry(textvariable=y_b)
    x_c_entry = Entry(textvariable=x_c)
    y_c_entry = Entry(textvariable=y_c)

    x_a_entry.grid(row=1, column=1, padx=5, pady=5)
    y_a_entry.grid(row=2, column=1, padx=5, pady=5)
    x_b_entry.grid(row=3, column=1, padx=5, pady=5)
    y_b_entry.grid(row=4, column=1, padx=5, pady=5)
    x_c_entry.grid(row=5, column=1, padx=5, pady=5)
    y_c_entry.grid(row=6, column=1, padx=5, pady=5)

    # Line
    line_params = Label(text="Line parameters \n (y = kx + b)", font='Helvetica 18 bold')
    line_params.grid(row=0, column=4, sticky="n")

    k = StringVar()
    b = StringVar()

    k_line_label = Label(text="k:")
    b_line_label = Label(text="b:")

    k_line_label.grid(row=3, column=3, sticky="w")
    b_line_label.grid(row=4, column=3, sticky="w")

    k_entry = Entry(textvariable=k)
    b_entry = Entry(textvariable=b)

    k_entry.grid(row=3, column=4, padx=5, pady=5)
    b_entry.grid(row=4, column=4, padx=5, pady=5)

    # Button
    message_button = Button(text="Build",height=2, width=6,
                            command=lambda: return_parameters(x_a, y_a, x_b, y_b, x_c, y_c,
                                                              k, b, triangle, line, root))

    message_button.grid(row=7, column=2, padx=5, pady=5, sticky="e")

    root.mainloop()

