import sys


from PySide6.QtWidgets import (QPushButton, QLineEdit, QLabel,
                               QWidget, QVBoxLayout, QHBoxLayout, QApplication, QMessageBox)
from PySide6.QtGui import QIcon
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp


class GraphicCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Graphic Calculator")
        self.setGeometry(320, 80, 900, 700)
        self.setWindowIcon(QIcon("images.ico"))

        main_layout = QVBoxLayout()
        secondary_layout = QHBoxLayout()
        third_degree_layout = QHBoxLayout()
        fourth_layout = QHBoxLayout()

        self.canvas = FigureCanvas(Figure(figsize=(5, 4)))
        self.ax = self.canvas.figure.subplots()
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.formula_box = QLineEdit()
        self.formula_box.setText('cos(x)')
        self.formula_box.setPlaceholderText("Formula of f(x), example cos(x)")
        self.limit_box = QLineEdit()
        self.limit_box.setText("-8, 8, 40000")
        self.limit_box.setPlaceholderText("start, end, points (e.g. -5, 5, 1000)")

        self.button_check = QPushButton("More Option")
        self.button_check.setCheckable(True)

        self.calculate_button = QPushButton("Plot Graph!")
        self.calculate_critical_points = QPushButton("Critical Points!")
        self.calculate_critical_points.setCheckable(True)
        self.three_d_button = QPushButton("Plot 3D!")
        self.three_d_button.setCheckable(True)
        self.clear_all_button = QPushButton("CLEAR ALL!")

        self.explain = QLabel("Calculate Area From: ")
        self.explain.hide()
        self.input_box = QLineEdit()
        self.to_word = QLabel("To: ")
        self.to_word.hide()
        self.input_box_2 = QLineEdit()
        self.input_box.hide()
        self.input_box_2.hide()
        self.calculate_area = QPushButton("Operate!")
        self.calculate_area.hide()
        self.clear_button_area = QPushButton("Clear!")
        self.clear_button_area.hide()



        secondary_layout.addWidget(self.formula_box)
        secondary_layout.addWidget(self.limit_box)
        secondary_layout.addWidget(self.calculate_button)

        third_degree_layout.addWidget(self.explain)
        third_degree_layout.addWidget(self.input_box)
        third_degree_layout.addWidget(self.to_word)
        third_degree_layout.addWidget(self.input_box_2)
        third_degree_layout.addWidget(self.calculate_area)
        third_degree_layout.addWidget(self.clear_button_area)


        fourth_layout.addWidget(self.calculate_critical_points)
        fourth_layout.addWidget(self.three_d_button)
        fourth_layout.addWidget(self.clear_all_button)


        main_layout.addWidget(self.button_check)
        main_layout.addLayout(third_degree_layout)
        main_layout.addWidget(self.toolbar)
        main_layout.addWidget(self.canvas)
        main_layout.addLayout(secondary_layout)
        main_layout.addLayout(fourth_layout)

        self.setLayout(main_layout)

        self.calculate_button.clicked.connect(self.calculate)
        self.button_check.clicked.connect(self.show_input)
        self.calculate_area.clicked.connect(self.operate_area)
        self.clear_button_area.clicked.connect(self.clear_area)
        self.calculate_critical_points.clicked.connect(self.find_critical)

    def calculate(self):
        limit_values = self.limit_box.text()

        try:
            a = [int(i) for i in limit_values.split(",")]
            x = np.linspace(a[0], a[1], a[2])
            allowed_names = {'x': x, 'sin': np.sin, 'cos': np.cos,'tan': np.tan,'log': np.log,
                             'exp': np.exp,'sqrt': np.sqrt,'abs': np.abs,'pi': np.pi,'e': np.e}

            y_value = self.formula_box.text()
            y = eval(y_value, {"__builtins__": {}}, allowed_names)

            y_diff = sp.diff(sp.sympify(y_value))

            if y_diff.is_constant():
                y_2 = np.full_like(x, float(y_diff))
            else:
                y_2 = eval(str(y_diff), {"__builtins__": {}}, allowed_names)

            self.ax.clear()
            self.ax.plot(x, y, color = 'red', label = f"Function: {y_value}")
            self.ax.plot(x, y_2, color = "blue", linestyle = '--', label = f"Derivative: {y_diff}")
            self.ax.legend()
            self.ax.set_ylim(a[0],a[1])
            self.ax.set_title(f"y = {y_value}")
            self.ax.grid(True)
            self.canvas.draw()


        except:
            QMessageBox.information(self, "Error", "Please check you write start, end, point numbers. "
                                                   "Additionally check you fill both input boxes!")


    def show_input(self):
        if self.button_check.isChecked():
            self.button_check.setText("Hide")
            self.input_box.show()
            self.input_box_2.show()
            self.explain.show()
            self.to_word.show()
            self.calculate_area.show()
            self.clear_button_area.show()

        else:
            self.button_check.setText("More Option")
            self.input_box.hide()
            self.input_box_2.hide()
            self.explain.hide()
            self.to_word.hide()
            self.calculate_area.hide()
            self.clear_button_area.hide()

    def operate_area(self):
        if self.formula_box.text().strip() == "":
            QMessageBox.information(self, "Error", "Please make sure you already plot the graph!")

        else:
            try:
                num_1 = int(self.input_box.text())
                num_2 = int(self.input_box_2.text())

                x = sp.Symbol('x')
                f = sp.sympify(self.formula_box.text())

                integ_f = sp.integrate(f, (x, num_1, num_2))
                print(type(f))
                f_lambdify = sp.lambdify(x, f, modules=['numpy'])

                x_fill = np.linspace(num_1, num_2, 300)
                y_fill = f_lambdify(x_fill)

                self.ax.fill_between(x_fill, y_fill, color = "green", label = f"Area: {integ_f}")
                self.ax.legend()
                self.canvas.draw()

            except:
                QMessageBox.information(self, "Error", "Please make sure you write numbers!")

    def clear_area(self):
        for i in self.ax.collections:
            i.remove()
        self.canvas.draw()

    def find_critical(self):
        limit_values = self.limit_box.text()

        try:
            a = [int(i) for i in limit_values.split(",")]
            x = np.linspace(a[0], a[1], a[2])

            symbol_x = sp.Symbol('x')
            f_x = sp.sympify(self.formula_box.text())
            diff_f = sp.diff(f_x)

            f_x_numpy = sp.lambdify(symbol_x, f_x, modules=['numpy'])
            diff_new_numpy = sp.lambdify(symbol_x, diff_f, modules=['numpy'])

            diff_f_x_numbers = diff_new_numpy(x)

            critical_x = []
            critical_y = []

            for i in range(len(diff_f_x_numbers)):
                if  abs(diff_f_x_numbers[i]) < 10**-int(len(str(a[2]))-2):
                    critical_x.append(x[i])
                    critical_y.append(f_x_numpy(x[i]))
                


            if self.calculate_critical_points.isChecked():
                self.critical_points_plot = self.ax.scatter(critical_x, critical_y, color='green', marker='x', label='Critical Points')
                self.ax.legend()
                self.canvas.draw()

            else:
                if self.critical_points_plot:
                    self.critical_points_plot.remove()
                    self.ax.legend()
                    self.canvas.draw()




        except:
            QMessageBox.information(self, "Error", f"Couldn't find critical points!")



app = QApplication(sys.argv)
window = GraphicCalculator()
window.show()
app.exec()

