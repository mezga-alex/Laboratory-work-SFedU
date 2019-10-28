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

        Label(top, text="Enter dot coordinates").pack()
        Label(top, text="(any formatting, but separated)").pack()

        self.k = Entry(top)
        self.k.pack(padx=5)

        b = Button(top, text="Calculate", command=self.computation)
        b.pack(pady=5)
        top.lift()

        root.mainloop()

    def computation(self):
        dot_coords = re.findall(r"[+-]?\d+(?:\.\d+)?", self.k.get())
        x = float(dot_coords[0])
        y = float(dot_coords[1])
        nums_list = re.findall(r"[+-]?\d+(?:\.\d+)?", self.e.get())
        len_of_nums_list = len(nums_list)

        print(nums_list)
        #
        if len_of_nums_list % 2 == 0 and len_of_nums_list > 2:
            self.top.destroy()

            num_of_angles = int(len_of_nums_list / 2)
            polygon = np.empty([num_of_angles, 2])
            for i in range(num_of_angles):
                polygon[i] = [nums_list[2 * i], nums_list[2 * i + 1]]
            print(polygon)
            # Show the polygon
            pln.build_plot(polygon, x, y)

            # Task 1
            # Check if the polygon is convex
            is_convex = pln.is_convex_polygon(polygon)
            if is_convex:
                messagebox.showinfo("Convex", "The polygon is convex")
            else:
                messagebox.showinfo("Convex", "The polygon is not convex")

            # Task 2
            in_polygon = pln.dot_in_polygon(x, y, polygon)
            # print("in polygon: ", in_polygon)
            if in_polygon == 0:
                messagebox.showinfo("Polygon", "The dot is outside")
            else:
                messagebox.showinfo("Polygon", "The dot is inside")

            # Task 3
            # Calculate the polygon area
            s = pln.area(polygon)
            messagebox.showinfo("Area", "S = {}".format(s))
        else:
            messagebox.showinfo("Parameters Error", "The number of points must be a multiple of 2")
