from tkinter import *
import tkinter as tk
from tkinter import messagebox
import numpy as np
import bezier_curve as bc


class MyDialog:
    def __init__(self):
        root = tk.Tk()
        top = self.top = Toplevel(root)
        top.geometry("400x200+400+300")
        Label(top, text="Enter coordinates").pack()
        Label(top, text="(any formatting, but separated)").pack()

        self.e = Entry(top)
        self.e.pack(padx=5)

        b = Button(top, text="Build", command=self.computation)
        b.pack(pady=5)
        top.lift()

        root.mainloop()

    def computation(self):
        nums_list = re.findall(r"[+-]?\d+(?:\.\d+)?", self.e.get())
        len_of_nums_list = len(nums_list)

        if len_of_nums_list % 2 == 0 and len_of_nums_list > 2:
            num_of_points = int(len_of_nums_list / 2)

            bezier_start_points = np.empty([num_of_points, 2])
            for i in range(num_of_points):
                bezier_start_points[i] = [nums_list[2 * i], nums_list[2 * i + 1]]

            curve_points = np.array(bc.bezier_curve(bezier_start_points, 1000))

            x_points = np.array([p[0] for p in bezier_start_points])
            y_points = np.array([p[1] for p in bezier_start_points])
            xy_bezier_start_points = np.array([x_points, y_points])

            bc.build_plot(xy_bezier_start_points, curve_points)

        else:
            messagebox.showinfo("Parameters Error", "The number of points must be more than 2")


if __name__ == '__main__':
    MyDialog()