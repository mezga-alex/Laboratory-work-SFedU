from tkinter import *
import tkinter as tk
from tkinter import messagebox
import numpy as np
import polygon as pln


class MyDialog:
    def __init__(self):
        root = tk.Tk()
        top = self.top = Toplevel(root)
        top.geometry("400x200+400+300")
        Label(top, text="Enter vertices coordinates").pack()
        Label(top, text="(any formatting, but separated)").pack()

        self.e = Entry(top)
        self.e.pack(padx=5)

        b = Button(top, text="Calculate", command=self.computation)
        b.pack(pady=5)
        top.lift()

        root.mainloop()

    def computation(self):
        nums_list = re.findall(r"[-+]?\d*\.\d+|\d+", self.e.get())
        len_of_nums_list = len(nums_list)

        #
        if len_of_nums_list % 2 == 0 and len_of_nums_list > 2:
            self.top.destroy()

            num_of_angles = int(len_of_nums_list / 2)
            polygon = np.empty([num_of_angles, 2])
            for i in range(num_of_angles):
                polygon[i] = [nums_list[2 * i], nums_list[2 * i + 1]]

            # Show the polygon
            pln.build_plot(polygon)

            # Task 1
            # Check if the polygon is convex
            is_convex = pln.is_convex_polygon(polygon)
            if is_convex:
                messagebox.showinfo("Convex", "The polygon is convex")
            else:
                messagebox.showinfo("Convex", "The polygon is not convex")

            # Task 3
            # Calculate the polygon area
            s = pln.area(polygon)
            messagebox.showinfo("Area", "S = {}".format(s))
        else:
            messagebox.showinfo("Parameters Error", "The number of points must be a multiple of 2")
