import sys
from PySide6.QtWidgets import( QApplication, QWidget, QLabel, QPushButton,
                               QMainWindow, QVBoxLayout, QLineEdit, QHBoxLayout, QMessageBox)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import sympy as sp

class TasbehWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.counter = 0

        self.setWindowTitle("Tasbih")
        self.setWindowIcon(QIcon("myapp_icon_order.ico"))
        self.setGeometry(520, 280, 250, 200)
        self.setFixedSize(250, 200)

        main_layout = QVBoxLayout()

        title = QLabel("Hi, Welcome to my App!")

        second_layout = QHBoxLayout()
        self.count_button = QPushButton("Subhanallah")
        self.reset_button = QPushButton("Reset")
        self.about_button = QPushButton("About")
        self.about_button.setFixedSize(60, 20)
        second_layout.addWidget(self.count_button)
        second_layout.addWidget(self.reset_button)

        self.result = QLabel("0")

        main_layout.addWidget(self.about_button, alignment=Qt.AlignRight)
        main_layout.addWidget(title)
        main_layout.addLayout(second_layout)
        main_layout.addWidget(self.result)

        self.setLayout(main_layout)

        self.count_button.clicked.connect(self.count_num)
        self.reset_button.clicked.connect(self.reset_counter)
        self.about_button.clicked.connect(self.about_msg)

    def word_tasbeh(self):
        if self.counter < 33:
            return "Subhanallah"

        elif self.counter <= 66:
            return "Alhamdulillah"

        else:
            return "Allahu Akbar"

    def count_num(self):
        self.counter += 1
        self.result.setText(str(self.counter))

        new_word = self.word_tasbeh()
        self.count_button.setText(new_word)

    def reset_counter(self):
        reply = QMessageBox.question(self, "Reset Counter", "Do you really want to reset counter?",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.counter = 0
            self.result.setText("0")
            self.count_button.setText("Subhanallah")

        else:
            pass


    def about_msg(self):
        QMessageBox.information(self, "About", "The tasbih, as a tool for counting, allows you to keep your focus on the "
                                               "dhikr, rather than trying to keep count mentally. Tasbihs also help focus your attention "
                                               "on the dhikr you are doing by connecting your mind to your body, specifically to your fingers")



class RegisterForm(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Register Form")
        self.setGeometry(550, 250, 400, 300)
        self.setWindowIcon(QIcon("register_photo.ico"))

        self.label = QLabel("Enter your name: ", self)
        self.label.setGeometry(160, 0,400, 30)

        self.fill_name = QLineEdit(self)
        self.fill_name.setGeometry(110, 40, 180, 30)

        self.button = QPushButton("REGISTER", self)
        self.button.setGeometry(140, 80, 120, 30)
        self.button.clicked.connect(self.greet)

        self.label_2 = QLabel(" ", self)
        self.label_2.setGeometry(120, 120, 400, 30)

    def greet(self):
        name = self.fill_name.text()
        if name.strip():
            self.label_2.setText(f"{name} registered successfully")
        else:
            self.label_2.setText("Please fill the blank!")


class RegistrationFormNewVersion(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Register")
        self.setWindowIcon(QIcon("register_photo.ico"))
        self.setGeometry(500, 300, 230, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Enter Your Name: ")
        self.input_box = QLineEdit()
        self.button = QPushButton("Register")
        self.label_2 = QLabel("")

        layout.addWidget(self.label)
        layout.addWidget(self.input_box)
        layout.addWidget(self.button)
        layout.addWidget(self.label_2)

        self.setLayout(layout)

        self.button.clicked.connect(self.greet)

    def greet(self):
        name = self.input_box.text()
        if name.strip():
            self.label_2.setText(f"{name} registered successfully 🎉!")
        else:
            self.label_2.setText("Please fill the blank!")




class GraphicCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Graphic Calculator")
        self.setGeometry(380, 150, 900, 700)
        self.setWindowIcon(QIcon("images.ico"))

        main_layout = QVBoxLayout()
        secondary_layout = QHBoxLayout()
        third_degree_layout = QHBoxLayout()

        self.canvas = FigureCanvas(Figure(figsize=(5, 4)))
        self.ax = self.canvas.figure.subplots()

        self.formula_box = QLineEdit()
        self.limit_box = QLineEdit()

        self.button_check = QPushButton("Show")
        self.button_check.setCheckable(True)

        self.calculate_button = QPushButton("Calculate!")

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

        third_degree_layout.addWidget(self.explain)
        third_degree_layout.addWidget(self.input_box)
        third_degree_layout.addWidget(self.to_word)
        third_degree_layout.addWidget(self.input_box_2)
        third_degree_layout.addWidget(self.calculate_area)
        third_degree_layout.addWidget(self.clear_button_area)


        main_layout.addWidget(self.button_check)
        main_layout.addLayout(third_degree_layout)
        main_layout.addWidget(self.canvas)
        main_layout.addLayout(secondary_layout)
        main_layout.addWidget(self.calculate_button)

        self.setLayout(main_layout)
        self.calculate_button.clicked.connect(self.calculate)
        self.button_check.clicked.connect(self.show_input)
        self.calculate_area.clicked.connect(self.operate_area)
        self.clear_button_area.clicked.connect(self.clear_area)

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
            self.button_check.setText("Show")
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


