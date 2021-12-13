from qt_core import *

from PyQt5 import QtGui

class Ui_Secoes(object):
    def setupUi(self, Secoes):
        if not Secoes.objectName():
            Secoes.setObjectName(u"Secoes")
        Secoes.resize(350, 900)
        Secoes.setStyleSheet(u"#general{background-color: rgb(17,17, 17);}\n"
"#linear_parts{background-color: rgb(17,17, 17);}\n"
"#esteganography{background-color: rgb(17,17, 17);}\n"
"#filters{background-color: rgb(17,17, 17);}\n"
"#colors{background-color: rgb(17,17, 17);}\n"
"#generic_filter{background-color: rgb(17,17, 17);}")
        self.linear_parts = QWidget()
        self.linear_parts.setObjectName(u"linear_parts")
        self.lp_title = QLabel(self.linear_parts)
        self.lp_title.setObjectName(u"lp_title")
        self.lp_title.setGeometry(QRect(20, 20, 171, 31))
        self.lp_title.setLayoutDirection(Qt.LeftToRight)
        self.lp_title.setAlignment(Qt.AlignCenter)
        self.configure_lp_box = QGroupBox(self.linear_parts)
        self.configure_lp_box.setObjectName(u"configure_lp_box")
        self.configure_lp_box.setGeometry(QRect(20, 70, 311, 311))
        self.configure_lp_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.lp_bool = QCheckBox(self.configure_lp_box)
        self.lp_bool.setObjectName(u"lp_bool")
        self.lp_bool.setGeometry(QRect(80, 250, 151, 41))
        self.lp_bool.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.points_x_label = QLabel(self.configure_lp_box)
        self.points_x_label.setObjectName(u"points_x_label")
        self.points_x_label.setGeometry(QRect(130, 30, 51, 31))
        self.see_plot_button = QPushButton(self.configure_lp_box)
        self.see_plot_button.setObjectName(u"see_plot_button")
        self.see_plot_button.setGeometry(QRect(90, 190, 131, 31))
        self.see_plot_button.setStyleSheet(u"background-color: rgb(65, 65, 65);\n"
"color: rgb(255, 255, 255);")
        self.points_y_label = QLabel(self.configure_lp_box)
        self.points_y_label.setObjectName(u"points_y_label")
        self.points_y_label.setGeometry(QRect(130, 100, 51, 31))
        self.points_x_values = QPlainTextEdit(self.configure_lp_box)
        self.points_x_values.setObjectName(u"points_x_values")
        self.points_x_values.setGeometry(QRect(20, 60, 271, 31))
        self.points_x_values.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.points_y_values = QPlainTextEdit(self.configure_lp_box)
        self.points_y_values.setObjectName(u"points_y_values")
        self.points_y_values.setGeometry(QRect(20, 130, 271, 31))
        self.points_y_values.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.plot_box = QGroupBox(self.linear_parts)
        self.plot_box.setObjectName(u"plot_box")
        self.plot_box.setGeometry(QRect(20, 400, 311, 261))
        self.plot_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.lp_image = QLabel(self.plot_box)
        self.lp_image.setObjectName(u"lp_image")
        self.lp_image.setGeometry(QRect(10, 20, 291, 231))
        Secoes.addWidget(self.linear_parts)
        self.esteganography = QWidget()
        self.esteganography.setObjectName(u"esteganography")
        self.esteg_title = QLabel(self.esteganography)
        self.esteg_title.setObjectName(u"esteg_title")
        self.esteg_title.setGeometry(QRect(20, 20, 181, 31))
        self.encode_box = QGroupBox(self.esteganography)
        self.encode_box.setObjectName(u"encode_box")
        self.encode_box.setGeometry(QRect(20, 70, 311, 191))
        self.encode_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.esteg_entry_text = QPlainTextEdit(self.encode_box)
        self.esteg_entry_text.setObjectName(u"esteg_entry_text")
        self.esteg_entry_text.setGeometry(QRect(20, 60, 271, 61))
        self.esteg_entry_text.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.encode_button = QPushButton(self.encode_box)
        self.encode_button.setObjectName(u"encode_button")
        self.encode_button.setGeometry(QRect(80, 140, 151, 31))
        self.encode_button.setStyleSheet(u"background-color: rgb(82, 82, 82);\n"
"color: rgb(255, 255, 255);")
        self.enter_text_label = QLabel(self.encode_box)
        self.enter_text_label.setObjectName(u"enter_text_label")
        self.enter_text_label.setGeometry(QRect(100, 20, 121, 31))
        self.decode_box = QGroupBox(self.esteganography)
        self.decode_box.setObjectName(u"decode_box")
        self.decode_box.setGeometry(QRect(20, 280, 311, 171))
        self.decode_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.decrypted_label = QLabel(self.decode_box)
        self.decrypted_label.setObjectName(u"decrypted_label")
        self.decrypted_label.setGeometry(QRect(30, 60, 251, 51))
        self.decrypted_label.setStyleSheet(u"font: 700 14pt \"Segoe UI\";")
        self.enter_text_decode_label = QLabel(self.decode_box)
        self.enter_text_decode_label.setObjectName(u"enter_text_decode_label")
        self.enter_text_decode_label.setGeometry(QRect(110, 20, 91, 31))
        self.decode_button = QPushButton(self.decode_box)
        self.decode_button.setObjectName(u"decode_button")
        self.decode_button.setGeometry(QRect(80, 120, 151, 31))
        self.decode_button.setAutoFillBackground(False)
        self.decode_button.setStyleSheet(u"background-color: rgb(82, 82, 82);\n"
"color: rgb(255, 255, 255);")
        Secoes.addWidget(self.esteganography)
        self.general = QWidget()
        self.general.setObjectName(u"general")
        self.apply_button = QPushButton(self.general)
        self.apply_button.setObjectName(u"apply_button")
        self.apply_button.setGeometry(QRect(110, 830, 131, 31))
        self.apply_button.setStyleSheet(u"background-color: rgb(65, 65, 65);\n"
"color: rgb(255, 255, 255);")
        self.title_general = QLabel(self.general)
        self.title_general.setObjectName(u"title_general")
        self.title_general.setGeometry(QRect(30, 20, 171, 31))
        self.title_general.setLayoutDirection(Qt.LeftToRight)
        self.title_general.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.sliders_box = QGroupBox(self.general)
        self.sliders_box.setObjectName(u"sliders_box")
        self.sliders_box.setGeometry(QRect(20, 320, 311, 101))
        self.sliders_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.gama_value_label = QLabel(self.sliders_box)
        self.gama_value_label.setObjectName(u"gama_value_label")
        self.gama_value_label.setGeometry(QRect(140, 60, 31, 31))
        self.gama_label = QLabel(self.sliders_box)
        self.gama_label.setObjectName(u"gama_label")
        self.gama_label.setGeometry(QRect(130, 10, 51, 31))
        self.gama_slider = QSlider(self.sliders_box)
        self.gama_slider.setObjectName(u"gama_slider")
        self.gama_slider.setGeometry(QRect(10, 40, 291, 22))
        self.gama_slider.setMinimum(0)
        self.gama_slider.setMaximum(200)
        self.gama_slider.setValue(100)
        self.gama_slider.setSliderPosition(100)
        self.gama_slider.setOrientation(Qt.Horizontal)
        self.gama_slider.setInvertedAppearance(False)
        self.effects_box = QGroupBox(self.general)
        self.effects_box.setObjectName(u"effects_box")
        self.effects_box.setGeometry(QRect(20, 70, 311, 131))
        self.effects_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.verticalLayout_5 = QVBoxLayout(self.effects_box)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.negative_bool = QCheckBox(self.effects_box)
        self.negative_bool.setObjectName(u"negative_bool")
        self.negative_bool.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.negative_bool)

        self.log_bool = QCheckBox(self.effects_box)
        self.log_bool.setObjectName(u"log_bool")
        self.log_bool.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.log_bool)

        self.equalize_bool = QCheckBox(self.effects_box)
        self.equalize_bool.setObjectName(u"equalize_bool")
        self.equalize_bool.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.equalize_bool)

        self.histogram_box = QGroupBox(self.general)
        self.histogram_box.setObjectName(u"histogram_box")
        self.histogram_box.setGeometry(QRect(20, 540, 311, 261))
        self.histogram_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.histogram_image = QLabel(self.histogram_box)
        self.histogram_image.setObjectName(u"histogram_image")
        self.histogram_image.setGeometry(QRect(10, 20, 291, 231))
        self.geometry_box = QGroupBox(self.general)
        self.geometry_box.setObjectName(u"geometry_box")
        self.geometry_box.setGeometry(QRect(20, 210, 311, 101))
        self.geometry_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.resize_bool = QCheckBox(self.geometry_box)
        self.resize_bool.setObjectName(u"resize_bool")
        self.resize_bool.setGeometry(QRect(10, 28, 67, 26))
        self.resize_bool.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.rotate_bool = QCheckBox(self.geometry_box)
        self.rotate_bool.setObjectName(u"rotate_bool")
        self.rotate_bool.setGeometry(QRect(10, 62, 68, 26))
        self.rotate_bool.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.resize_value = QComboBox(self.geometry_box)
        self.resize_value.addItem("")
        self.resize_value.addItem("")
        self.resize_value.addItem("")
        self.resize_value.addItem("")
        self.resize_value.addItem("")
        self.resize_value.addItem("")
        self.resize_value.addItem("")
        self.resize_value.setObjectName(u"resize_value")
        self.resize_value.setGeometry(QRect(111, 30, 161, 21))
        self.resize_value.setStyleSheet(u"background-color: rgb(77, 77, 77);")
        self.rotate_value = QComboBox(self.geometry_box)
        self.rotate_value.addItem("")
        self.rotate_value.addItem("")
        self.rotate_value.addItem("")
        self.rotate_value.addItem("")
        self.rotate_value.addItem("")
        self.rotate_value.setObjectName(u"rotate_value")
        self.rotate_value.setGeometry(QRect(110, 70, 161, 21))
        self.rotate_value.setStyleSheet(u"background-color: rgb(77, 77, 77);")
        self.brightness_box = QGroupBox(self.general)
        self.brightness_box.setObjectName(u"brightness_box")
        self.brightness_box.setGeometry(QRect(20, 430, 311, 101))
        self.brightness_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.brightness_value_label = QLabel(self.brightness_box)
        self.brightness_value_label.setObjectName(u"brightness_value_label")
        self.brightness_value_label.setGeometry(QRect(140, 70, 31, 31))
        self.brightness_label = QLabel(self.brightness_box)
        self.brightness_label.setObjectName(u"brightness_label")
        self.brightness_label.setGeometry(QRect(110, 10, 81, 31))
        self.brightness_slider = QSlider(self.brightness_box)
        self.brightness_slider.setObjectName(u"brightness_slider")
        self.brightness_slider.setGeometry(QRect(10, 50, 291, 22))
        self.brightness_slider.setMinimum(0)
        self.brightness_slider.setMaximum(200)
        self.brightness_slider.setValue(100)
        self.brightness_slider.setSliderPosition(100)
        self.brightness_slider.setOrientation(Qt.Horizontal)
        Secoes.addWidget(self.general)
        self.effects_box.raise_()
        self.sliders_box.raise_()
        self.apply_button.raise_()
        self.title_general.raise_()
        self.histogram_box.raise_()
        self.geometry_box.raise_()
        self.brightness_box.raise_()
        self.filters = QWidget()
        self.filters.setObjectName(u"filters")
        self.title_filters = QLabel(self.filters)
        self.title_filters.setObjectName(u"title_filters")
        self.title_filters.setGeometry(QRect(30, 20, 171, 31))
        self.title_filters.setLayoutDirection(Qt.LeftToRight)
        self.title_filters.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.adjust_box = QGroupBox(self.filters)
        self.adjust_box.setObjectName(u"adjust_box")
        self.adjust_box.setGeometry(QRect(20, 70, 311, 71))
        self.adjust_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.horizontalLayout = QHBoxLayout(self.adjust_box)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.kernel_size_label = QLabel(self.adjust_box)
        self.kernel_size_label.setObjectName(u"kernel_size_label")
        self.kernel_size_label.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.kernel_size_label)

        self.kernel_size_select = QComboBox(self.adjust_box)
        self.kernel_size_select.addItem("")
        self.kernel_size_select.addItem("")
        self.kernel_size_select.addItem("")
        self.kernel_size_select.addItem("")
        self.kernel_size_select.addItem("")
        self.kernel_size_select.addItem("")
        self.kernel_size_select.setObjectName(u"kernel_size_select")
        self.kernel_size_select.setStyleSheet(u"background-color: rgb(77, 77, 77);")

        self.horizontalLayout.addWidget(self.kernel_size_select)

        self.select_filter_box = QGroupBox(self.filters)
        self.select_filter_box.setObjectName(u"select_filter_box")
        self.select_filter_box.setGeometry(QRect(20, 150, 311, 471))
        self.select_filter_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.verticalLayout = QVBoxLayout(self.select_filter_box)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.median_bool = QCheckBox(self.select_filter_box)
        self.median_bool.setObjectName(u"median_bool")
        self.median_bool.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.median_bool)

        self.median_simple_w_bool = QCheckBox(self.select_filter_box)
        self.median_simple_w_bool.setObjectName(u"median_simple_w_bool")
        self.median_simple_w_bool.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.median_simple_w_bool)

        self.median_simple_bool = QCheckBox(self.select_filter_box)
        self.median_simple_bool.setObjectName(u"median_simple_bool")
        self.median_simple_bool.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.median_simple_bool)

        self.high_boost_bool = QCheckBox(self.select_filter_box)
        self.high_boost_bool.setObjectName(u"high_boost_bool")
        self.high_boost_bool.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.high_boost_bool)

        self.laplacian_bool = QCheckBox(self.select_filter_box)
        self.laplacian_bool.setObjectName(u"laplacian_bool")
        self.laplacian_bool.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.laplacian_bool)

        self.sobel_x_bool = QCheckBox(self.select_filter_box)
        self.sobel_x_bool.setObjectName(u"sobel_x_bool")
        self.sobel_x_bool.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.sobel_x_bool)

        self.sobel_y_bool = QCheckBox(self.select_filter_box)
        self.sobel_y_bool.setObjectName(u"sobel_y_bool")
        self.sobel_y_bool.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.sobel_y_bool)

        self.nled_bool = QCheckBox(self.select_filter_box)
        self.nled_bool.setObjectName(u"nled_bool")
        self.nled_bool.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.nled_bool)

        self.limiar_bool = QCheckBox(self.select_filter_box)
        self.limiar_bool.setObjectName(u"limiar_bool")
        self.limiar_bool.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.limiar_bool)

        self.select_fourier_box = QGroupBox(self.filters)
        self.select_fourier_box.setObjectName(u"select_fourier_box")
        self.select_fourier_box.setGeometry(QRect(20, 630, 311, 201))
        self.select_fourier_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.verticalLayout_2 = QVBoxLayout(self.select_fourier_box)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radius_box = QGroupBox(self.select_fourier_box)
        self.radius_box.setObjectName(u"radius_box")
        self.radius_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.horizontalLayout_2 = QHBoxLayout(self.radius_box)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radius_size_label = QLabel(self.radius_box)
        self.radius_size_label.setObjectName(u"radius_size_label")
        self.radius_size_label.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.radius_size_label)

        self.radius_value = QSpinBox(self.radius_box)
        self.radius_value.setObjectName(u"radius_value")
        self.radius_value.setStyleSheet(u"background-color: rgb(77, 77, 77);")

        self.horizontalLayout_2.addWidget(self.radius_value)


        self.verticalLayout_2.addWidget(self.radius_box)

        self.high_fourier_bool = QCheckBox(self.select_fourier_box)
        self.high_fourier_bool.setObjectName(u"high_fourier_bool")
        self.high_fourier_bool.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.high_fourier_bool)

        self.low_fourier_bool = QCheckBox(self.select_fourier_box)
        self.low_fourier_bool.setObjectName(u"low_fourier_bool")
        self.low_fourier_bool.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.low_fourier_bool)

        self.des_fourier_bool = QCheckBox(self.select_fourier_box)
        self.des_fourier_bool.setObjectName(u"des_fourier_bool")
        self.des_fourier_bool.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.des_fourier_bool)

        Secoes.addWidget(self.filters)
        self.adjust_box.raise_()
        self.title_filters.raise_()
        self.select_filter_box.raise_()
        self.select_fourier_box.raise_()
        self.generic_filter = QWidget()
        self.generic_filter.setObjectName(u"generic_filter")
        self.generic_filter_title = QLabel(self.generic_filter)
        self.generic_filter_title.setObjectName(u"generic_filter_title")
        self.generic_filter_title.setGeometry(QRect(30, 20, 171, 31))
        self.generic_filter_title.setLayoutDirection(Qt.LeftToRight)
        self.generic_filter_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.configure_generic_filter_box = QGroupBox(self.generic_filter)
        self.configure_generic_filter_box.setObjectName(u"configure_generic_filter_box")
        self.configure_generic_filter_box.setGeometry(QRect(20, 70, 311, 191))
        self.configure_generic_filter_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.gridLayout = QGridLayout(self.configure_generic_filter_box)
        self.gridLayout.setObjectName(u"gridLayout")
        self.a11_input = QSpinBox(self.configure_generic_filter_box)
        self.a11_input.setObjectName(u"a11_input")
        self.a11_input.setStyleSheet(u"background-color: rgb(77, 77, 77);")

        self.gridLayout.addWidget(self.a11_input, 0, 0, 1, 1)

        self.a21_input = QSpinBox(self.configure_generic_filter_box)
        self.a21_input.setObjectName(u"a21_input")
        self.a21_input.setStyleSheet(u"background-color: rgb(77, 77, 77);")

        self.gridLayout.addWidget(self.a21_input, 1, 0, 1, 1)

        self.a31_input = QSpinBox(self.configure_generic_filter_box)
        self.a31_input.setObjectName(u"a31_input")
        self.a31_input.setStyleSheet(u"background-color: rgb(77, 77, 77);")

        self.gridLayout.addWidget(self.a31_input, 2, 0, 1, 1)

        self.a22_input = QSpinBox(self.configure_generic_filter_box)
        self.a22_input.setObjectName(u"a22_input")
        self.a22_input.setStyleSheet(u"background-color: rgb(77, 77, 77);")

        self.gridLayout.addWidget(self.a22_input, 1, 1, 1, 1)

        self.a13_input = QSpinBox(self.configure_generic_filter_box)
        self.a13_input.setObjectName(u"a13_input")
        self.a13_input.setStyleSheet(u"background-color: rgb(77, 77, 77);")

        self.gridLayout.addWidget(self.a13_input, 0, 2, 1, 1)

        self.a33_input = QSpinBox(self.configure_generic_filter_box)
        self.a33_input.setObjectName(u"a33_input")
        self.a33_input.setStyleSheet(u"background-color: rgb(77, 77, 77);")

        self.gridLayout.addWidget(self.a33_input, 2, 2, 1, 1)

        self.a23_input = QSpinBox(self.configure_generic_filter_box)
        self.a23_input.setObjectName(u"a23_input")
        self.a23_input.setStyleSheet(u"background-color: rgb(77, 77, 77);")

        self.gridLayout.addWidget(self.a23_input, 1, 2, 1, 1)

        self.a12_input = QSpinBox(self.configure_generic_filter_box)
        self.a12_input.setObjectName(u"a12_input")
        self.a12_input.setStyleSheet(u"background-color: rgb(77, 77, 77);")

        self.gridLayout.addWidget(self.a12_input, 0, 1, 1, 1)

        self.a32_input = QSpinBox(self.configure_generic_filter_box)
        self.a32_input.setObjectName(u"a32_input")
        self.a32_input.setStyleSheet(u"background-color: rgb(77, 77, 77);")

        self.gridLayout.addWidget(self.a32_input, 2, 1, 1, 1)

        self.apply_generic_filter = QPushButton(self.generic_filter)
        self.apply_generic_filter.setObjectName(u"apply_generic_filter")
        self.apply_generic_filter.setGeometry(QRect(110, 290, 131, 31))
        self.apply_generic_filter.setStyleSheet(u"background-color: rgb(65, 65, 65);\n"
"color: rgb(255, 255, 255);")
        Secoes.addWidget(self.generic_filter)
        self.colors = QWidget()
        self.colors.setObjectName(u"colors")
        self.colors_title = QLabel(self.colors)
        self.colors_title.setObjectName(u"colors_title")
        self.colors_title.setGeometry(QRect(30, 20, 171, 31))
        self.colors_title.setLayoutDirection(Qt.LeftToRight)
        self.colors_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.colors_box = QGroupBox(self.colors)
        self.colors_box.setObjectName(u"colors_box")
        self.colors_box.setGeometry(QRect(20, 70, 311, 121))
        self.colors_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.verticalLayout_3 = QVBoxLayout(self.colors_box)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gray_scale_mean_bool = QCheckBox(self.colors_box)
        self.gray_scale_mean_bool.setObjectName(u"gray_scale_mean_bool")
        self.gray_scale_mean_bool.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.gray_scale_mean_bool)

        self.gray_scale_avg_bool = QCheckBox(self.colors_box)
        self.gray_scale_avg_bool.setObjectName(u"gray_scale_avg_bool")
        self.gray_scale_avg_bool.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.gray_scale_avg_bool)

        self.serpia_bool = QCheckBox(self.colors_box)
        self.serpia_bool.setObjectName(u"serpia_bool")
        self.serpia_bool.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.serpia_bool)

        self.hue_box = QGroupBox(self.colors)
        self.hue_box.setObjectName(u"hue_box")
        self.hue_box.setGeometry(QRect(20, 210, 311, 118))
        self.hue_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.hue_bool = QCheckBox(self.hue_box)
        self.hue_bool.setObjectName(u"hue_bool")
        self.hue_bool.setGeometry(QRect(130, 30, 51, 26))
        self.hue_bool.setLayoutDirection(Qt.LeftToRight)
        self.hue_bool.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.hue_slider = QSlider(self.hue_box)
        self.hue_slider.setObjectName(u"hue_slider")
        self.hue_slider.setGeometry(QRect(10, 58, 291, 22))
        self.hue_slider.setMinimum(0)
        self.hue_slider.setMaximum(360)
        self.hue_slider.setValue(180)
        self.hue_slider.setSliderPosition(180)
        self.hue_slider.setOrientation(Qt.Horizontal)
        self.hue_slider.setInvertedAppearance(False)
        self.hue_value_label = QLabel(self.hue_box)
        self.hue_value_label.setObjectName(u"hue_value_label")
        self.hue_value_label.setGeometry(QRect(140, 80, 27, 22))
        self.saturation_box = QGroupBox(self.colors)
        self.saturation_box.setObjectName(u"saturation_box")
        self.saturation_box.setGeometry(QRect(20, 340, 311, 118))
        self.saturation_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.saturation_bool = QCheckBox(self.saturation_box)
        self.saturation_bool.setObjectName(u"saturation_bool")
        self.saturation_bool.setGeometry(QRect(110, 30, 91, 26))
        self.saturation_bool.setLayoutDirection(Qt.LeftToRight)
        self.saturation_bool.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.saturation_slider = QSlider(self.saturation_box)
        self.saturation_slider.setObjectName(u"saturation_slider")
        self.saturation_slider.setGeometry(QRect(10, 58, 291, 22))
        self.saturation_slider.setMinimum(0)
        self.saturation_slider.setMaximum(200)
        self.saturation_slider.setValue(100)
        self.saturation_slider.setSliderPosition(100)
        self.saturation_slider.setOrientation(Qt.Horizontal)
        self.saturation_slider.setInvertedAppearance(False)
        self.saturation_value_label = QLabel(self.saturation_box)
        self.saturation_value_label.setObjectName(u"saturation_value_label")
        self.saturation_value_label.setGeometry(QRect(140, 80, 27, 22))
        self.color_histogram_box = QGroupBox(self.colors)
        self.color_histogram_box.setObjectName(u"color_histogram_box")
        self.color_histogram_box.setGeometry(QRect(20, 470, 311, 261))
        self.color_histogram_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.color_histogram_image = QLabel(self.color_histogram_box)
        self.color_histogram_image.setObjectName(u"color_histogram_image")
        self.color_histogram_image.setGeometry(QRect(10, 20, 291, 231))
        self.apply_colors_button = QPushButton(self.colors)
        self.apply_colors_button.setObjectName(u"apply_colors_button")
        self.apply_colors_button.setGeometry(QRect(110, 760, 131, 31))
        self.apply_colors_button.setStyleSheet(u"background-color: rgb(65, 65, 65);\n"
"color: rgb(255, 255, 255);")
        Secoes.addWidget(self.colors)

        self.retranslateUi(Secoes)

        Secoes.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(Secoes)
    # setupUi

    def retranslateUi(self, Secoes):
        Secoes.setWindowTitle(QCoreApplication.translate("Secoes", u"StackedWidget", None))
        self.lp_title.setText(QCoreApplication.translate("Secoes", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">Linear Parts Points</span></p></body></html>", None))
        self.configure_lp_box.setTitle(QCoreApplication.translate("Secoes", u"Configure", None))
        self.lp_bool.setText(QCoreApplication.translate("Secoes", u"Linear Parts Apply", None))
        self.points_x_label.setText(QCoreApplication.translate("Secoes", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Points x</span></p></body></html>", None))
        self.see_plot_button.setText(QCoreApplication.translate("Secoes", u"See Plot", None))
        self.points_y_label.setText(QCoreApplication.translate("Secoes", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Points y</span></p></body></html>", None))
        self.points_x_values.setPlainText("")
        self.points_y_values.setPlainText("")
        self.plot_box.setTitle(QCoreApplication.translate("Secoes", u"Plot", None))
        self.lp_image.setText("")
        self.esteg_title.setText(QCoreApplication.translate("Secoes", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">Esteganography</span></p></body></html>", None))
        self.encode_box.setTitle(QCoreApplication.translate("Secoes", u"Configure Encode", None))
        self.esteg_entry_text.setPlainText("")
        self.encode_button.setText(QCoreApplication.translate("Secoes", u"Encode", None))
        self.enter_text_label.setText(QCoreApplication.translate("Secoes", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Enter some text...</span></p></body></html>", None))
        self.decode_box.setTitle(QCoreApplication.translate("Secoes", u"Configure Decode", None))
        self.decrypted_label.setText(QCoreApplication.translate("Secoes", u"<html><head/><body><p><br/></p></body></html>", None))
        self.enter_text_decode_label.setText(QCoreApplication.translate("Secoes", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Entered text:</span></p></body></html>", None))
        self.decode_button.setText(QCoreApplication.translate("Secoes", u"Decode", None))
        self.apply_button.setText(QCoreApplication.translate("Secoes", u"Apply", None))
        self.title_general.setText(QCoreApplication.translate("Secoes", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">General</span></p></body></html>", None))
        self.sliders_box.setTitle(QCoreApplication.translate("Secoes", u"Gama", None))
        self.gama_value_label.setText(QCoreApplication.translate("Secoes", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">100</span></p></body></html>", None))
        self.gama_label.setText(QCoreApplication.translate("Secoes", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Gama</span></p></body></html>", None))
        self.effects_box.setTitle(QCoreApplication.translate("Secoes", u"Effects", None))
        self.negative_bool.setText(QCoreApplication.translate("Secoes", u"Negative Image", None))
        self.log_bool.setText(QCoreApplication.translate("Secoes", u"Log2", None))
        self.equalize_bool.setText(QCoreApplication.translate("Secoes", u"Equalize Histogram", None))
        self.histogram_box.setTitle(QCoreApplication.translate("Secoes", u"Histogram", None))
        self.histogram_image.setText("")
        self.geometry_box.setTitle(QCoreApplication.translate("Secoes", u"Geometry", None))
        self.resize_bool.setText(QCoreApplication.translate("Secoes", u"Resize", None))
        self.rotate_bool.setText(QCoreApplication.translate("Secoes", u"Rotate", None))
        self.resize_value.setItemText(0, QCoreApplication.translate("Secoes", u"0.25", None))
        self.resize_value.setItemText(1, QCoreApplication.translate("Secoes", u"0.5", None))
        self.resize_value.setItemText(2, QCoreApplication.translate("Secoes", u"0.75", None))
        self.resize_value.setItemText(3, QCoreApplication.translate("Secoes", u"1", None))
        self.resize_value.setItemText(4, QCoreApplication.translate("Secoes", u"1.25", None))
        self.resize_value.setItemText(5, QCoreApplication.translate("Secoes", u"1.5", None))
        self.resize_value.setItemText(6, QCoreApplication.translate("Secoes", u"2", None))

        self.rotate_value.setItemText(0, QCoreApplication.translate("Secoes", u"0", None))
        self.rotate_value.setItemText(1, QCoreApplication.translate("Secoes", u"90", None))
        self.rotate_value.setItemText(2, QCoreApplication.translate("Secoes", u"180", None))
        self.rotate_value.setItemText(3, QCoreApplication.translate("Secoes", u"270", None))
        self.rotate_value.setItemText(4, QCoreApplication.translate("Secoes", u"360", None))

        self.brightness_box.setTitle(QCoreApplication.translate("Secoes", u"Brightness", None))
        self.brightness_value_label.setText(QCoreApplication.translate("Secoes", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">100</span></p></body></html>", None))
        self.brightness_label.setText(QCoreApplication.translate("Secoes", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Brightness</span></p></body></html>", None))
        self.title_filters.setText(QCoreApplication.translate("Secoes", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">Filters</span></p></body></html>", None))
        self.adjust_box.setTitle(QCoreApplication.translate("Secoes", u"Configure Kernel", None))
        self.kernel_size_label.setText(QCoreApplication.translate("Secoes", u"Kernel Size", None))
        self.kernel_size_select.setItemText(0, QCoreApplication.translate("Secoes", u"3", None))
        self.kernel_size_select.setItemText(1, QCoreApplication.translate("Secoes", u"5", None))
        self.kernel_size_select.setItemText(2, QCoreApplication.translate("Secoes", u"7", None))
        self.kernel_size_select.setItemText(3, QCoreApplication.translate("Secoes", u"9", None))
        self.kernel_size_select.setItemText(4, QCoreApplication.translate("Secoes", u"11", None))
        self.kernel_size_select.setItemText(5, QCoreApplication.translate("Secoes", u"13", None))

        self.select_filter_box.setTitle(QCoreApplication.translate("Secoes", u"Select", None))
        self.median_bool.setText(QCoreApplication.translate("Secoes", u"Median Filter", None))
        self.median_simple_w_bool.setText(QCoreApplication.translate("Secoes", u"Mean Simple Weighted Filter", None))
        self.median_simple_bool.setText(QCoreApplication.translate("Secoes", u"Mean Simple Filter", None))
        self.high_boost_bool.setText(QCoreApplication.translate("Secoes", u"High Boost", None))
        self.laplacian_bool.setText(QCoreApplication.translate("Secoes", u"Laplacian", None))
        self.sobel_x_bool.setText(QCoreApplication.translate("Secoes", u"Sobel X", None))
        self.sobel_y_bool.setText(QCoreApplication.translate("Secoes", u"Sobel Y", None))
        self.nled_bool.setText(QCoreApplication.translate("Secoes", u"Non Linear Edge Detection", None))
        self.limiar_bool.setText(QCoreApplication.translate("Secoes", u"Limiar", None))
        self.select_fourier_box.setTitle(QCoreApplication.translate("Secoes", u"Fourier", None))
        self.radius_box.setTitle(QCoreApplication.translate("Secoes", u"Configure Radius", None))
        self.radius_size_label.setText(QCoreApplication.translate("Secoes", u"Radius Size", None))
        self.high_fourier_bool.setText(QCoreApplication.translate("Secoes", u"High Fourier", None))
        self.low_fourier_bool.setText(QCoreApplication.translate("Secoes", u"Low Fourier", None))
        self.des_fourier_bool.setText(QCoreApplication.translate("Secoes", u"Des Fourier", None))
        self.generic_filter_title.setText(QCoreApplication.translate("Secoes", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">Generic Filter</span></p></body></html>", None))
        self.configure_generic_filter_box.setTitle(QCoreApplication.translate("Secoes", u"Configure", None))
        self.apply_generic_filter.setText(QCoreApplication.translate("Secoes", u"Apply", None))
        self.colors_title.setText(QCoreApplication.translate("Secoes", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">Colors</span></p></body></html>", None))
        self.colors_box.setTitle(QCoreApplication.translate("Secoes", u"Color Image", None))
        self.gray_scale_mean_bool.setText(QCoreApplication.translate("Secoes", u"Gray Scale Mean", None))
        self.gray_scale_avg_bool.setText(QCoreApplication.translate("Secoes", u"Gray Scale AVG", None))
        self.serpia_bool.setText(QCoreApplication.translate("Secoes", u"Serpia", None))
        self.hue_box.setTitle(QCoreApplication.translate("Secoes", u"Hue Configuration", None))
        self.hue_bool.setText(QCoreApplication.translate("Secoes", u"Hue", None))
        self.hue_value_label.setText(QCoreApplication.translate("Secoes", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">180</span></p></body></html>", None))
        self.saturation_box.setTitle(QCoreApplication.translate("Secoes", u"Saturation Configuration", None))
        self.saturation_bool.setText(QCoreApplication.translate("Secoes", u"Saturation", None))
        self.saturation_value_label.setText(QCoreApplication.translate("Secoes", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">100</span></p></body></html>", None))
        self.color_histogram_box.setTitle(QCoreApplication.translate("Secoes", u"Color Histogram", None))
        self.color_histogram_image.setText("")
        self.apply_colors_button.setText(QCoreApplication.translate("Secoes", u"Apply", None))
    # retranslateUi
