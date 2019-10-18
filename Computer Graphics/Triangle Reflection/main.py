import ui
import triangle as tr


if __name__ == '__main__':
    triangle = tr.Triangle()
    line = tr.Line()

    # Create new dialog window
    ui.ui_window(triangle, line)

    # Check values and create new triangle
    if (triangle.check_value() is True) and (line.check_value() is True):
        ref_triangle = tr.create_reflection_triangle(triangle, line)
        ref_triangle.print_value()
        tr.build_plot(triangle, ref_triangle, line)

