# IMPORT QT CORE
from PIL.ImageQt import ImageQt
from matplotlib.pyplot import flag
import numpy as np
from qt_core import *

from gui.pages.ui_image import Ui_application_image
from gui.pages.ui_esteganografia import Ui_Frame
from gui.pages.ui_left_menu import Ui_LeftMenu
from gui.pages.ui_linear_parts import Ui_LinearParts
from gui.pages.ui_sections_2 import Ui_Secoes

from .img import Img
import functions.general as fc

from PyQt5 import QtGui

class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")
        
        # SET INITIAL PARAMETERS
        parent.resize(1600, 900)
        parent.setMinimumSize(960, 800)

        # CREATE CENTRAL WIDGET
        self.central_frame = QFrame()
        # self.central_frame.setStyleSheet("background-color: #313131")

        # CREATE MAIN LAYOUT
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)

        # LEFT MENU WIDGET
        self.left_menu = QFrame()
        self.ui_left_menu = Ui_LeftMenu()
        self.ui_left_menu.setupUi(self.left_menu)

        # IMPORT BUTTON
        self.ui_left_menu.import_button.clicked.connect(self.import_image)

        # GENERAL BUTTON
        self.ui_left_menu.general_button.clicked.connect(self.to_general)

        # ESTEGANOGRAPHY BUTTON
        self.ui_left_menu.esteg_button.clicked.connect(self.to_esteganography)

        # LINEAR PARTS BUTTON
        self.ui_left_menu.linear_parts_button.clicked.connect(self.to_linear_parts)

        # FILTERS BUTTON
        self.ui_left_menu.filters_button.clicked.connect(self.to_filters)

        # GENERIC FILTER BUTTON
        self.ui_left_menu.generic_filter_button.clicked.connect(self.to_generic_filter)

        # COLORS BUTTON
        self.ui_left_menu.colors_button.clicked.connect(self.to_colors)

        # self.left_menu.setStyleSheet("background-color: #525252")
        self.left_menu.setMinimumWidth(200)
        self.left_menu.setMaximumWidth(200)

        # CONTENT(IMAGE) WIDGET
        self.content = QFrame()
        # self.content.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.369318 rgba(31, 31, 31, 255), stop:1 rgba(74, 0, 111, 255));")

        # CONTENT LAYOUT
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)

        # APPLICATION IMAGE
        self.image = QStackedWidget()
        self.ui_image = Ui_application_image()
        self.ui_image.setupUi(self.image)

        self.content_layout.addWidget(self.image)
        # self.image = QLabel()
        # self.image.setPixmap(QtGui.QPixmap('reitoria.png'))
        # self.content_layout.addWidget(self.image)

        # MORE INFO WIDGET
        self.info = QStackedWidget()
        self.ui_info = Ui_Secoes()
        self.ui_info.setupUi(self.info)
        self.info.setCurrentWidget(self.ui_info.general)
        self.info.setMinimumWidth(350)
        self.info.setMaximumWidth(350)


        """
        CLEAR
        """

        self.ui_left_menu.clear.clicked.connect(self.clear)


        """
        GENERAL CHECKBOXES
        """

        # EQUALIZE HISTOGRAM
        self.check_equalize_bool = False
        self.ui_info.equalize_bool.stateChanged.connect(lambda:self.change_equalize_bool(self.ui_info.equalize_bool))
        # NEGATIVE
        self.check_negative_bool = False
        self.ui_info.negative_bool.toggled.connect(lambda:self.change_negative_bool(self.ui_info.negative_bool))
        # LOG
        self.check_log_bool = False
        self.ui_info.log_bool.stateChanged.connect(lambda:self.change_log_bool(self.ui_info.log_bool))

        # SLIDERS
        # GAMA
        self.ui_info.gama_slider.valueChanged.connect(self.gama_slider_changed)
        self.gama_slider_value = 100
        # BRIGHTNESS
        self.ui_info.brightness_slider.valueChanged.connect(self.brightness_slider_changed)
        self.brightness_slider_value = 100
        # HUE
        self.ui_info.hue_slider.valueChanged.connect(self.hue_slider_changed)
        self.hue_slider_value = 180
        # SATURATION
        self.ui_info.saturation_slider.valueChanged.connect(self.saturation_slider_changed)
        self.saturation_slider_value = 100

        # APPLY BUTTON
        self.ui_info.apply_button.clicked.connect(self.apply_checkbox_test)


        """
        ESTEGANOGRAPHY
        """

        # ENCODE
        self.ui_info.encode_button.clicked.connect(self.apply_encryption)

        # DECODE
        self.ui_info.decode_button.clicked.connect(self.apply_decryption)


        """
        LINEAR PARTS
        """

        # SEE PLOT
        self.ui_info.see_plot_button.clicked.connect(self.show_linear)

        # APPLY LINEAR PARTS
        self.check_lp_bool = False
        self.ui_info.lp_bool.stateChanged.connect(lambda:self.change_lp_bool(self.ui_info.lp_bool))

        # APPLY BUTTON
        self.ui_info.apply_lp.clicked.connect(self.apply_checkbox_test)


        """
        FILTERS CHECKBOXES
        """

        # MEDIAN FILTER
        self.check_median_bool = False
        self.ui_info.median_bool.stateChanged.connect(lambda:self.change_median_bool(self.ui_info.median_bool))
        # MEDIAN SIMPLE WEIGHTED FILTER
        self.check_mean_simple_w_bool = False
        self.ui_info.median_simple_w_bool.stateChanged.connect(lambda:self.change_median_simple_w_bool(self.ui_info.median_simple_w_bool))
        # MEDIAN SIMPLE FILTER
        self.check_mean_simple_bool = False
        self.ui_info.median_simple_bool.stateChanged.connect(lambda:self.change_median_simple_bool(self.ui_info.median_simple_bool))
        # HIGH BOOST
        self.check_high_boost_bool = False
        self.ui_info.high_boost_bool.stateChanged.connect(lambda:self.change_high_boost_bool(self.ui_info.high_boost_bool))
        # LAPLACIAN
        self.check_laplacian_bool = False
        self.ui_info.laplacian_bool.stateChanged.connect(lambda:self.change_laplacian_bool(self.ui_info.laplacian_bool))
        # SOBEL X
        self.check_sobel_x_bool = False
        self.ui_info.sobel_x_bool.stateChanged.connect(lambda:self.change_sobel_x_bool(self.ui_info.sobel_x_bool))
        # SOBEL Y
        self.check_sobel_y_bool = False
        self.ui_info.sobel_y_bool.stateChanged.connect(lambda:self.change_sobel_y_bool(self.ui_info.sobel_y_bool))
        # NON LINEAR EDGE DETECTION
        self.check_nled_bool = False
        self.ui_info.nled_bool.stateChanged.connect(lambda:self.change_nled_bool(self.ui_info.nled_bool))
        # GRAY SCALE MEAN
        self.check_gray_scale_mean_bool = False
        self.ui_info.gray_scale_mean_bool.stateChanged.connect(lambda:self.change_gray_scale_mean_bool(self.ui_info.gray_scale_mean_bool))
        # GRAY SCALE AVG
        self.check_gray_scale_avg_bool = False
        self.ui_info.gray_scale_avg_bool.stateChanged.connect(lambda:self.change_gray_scale_avg_bool(self.ui_info.gray_scale_avg_bool))
        # LOW FOURIER
        self.check_low_fourier_bool = False
        self.ui_info.low_fourier_bool.stateChanged.connect(lambda:self.change_low_fourier_bool(self.ui_info.low_fourier_bool))
        # HIGH FOURIER
        self.check_high_fourier_bool = False
        self.ui_info.high_fourier_bool.stateChanged.connect(lambda:self.change_high_fourier_bool(self.ui_info.high_fourier_bool))
        # DES FOURIER
        self.check_des_fourier_bool = False
        self.ui_info.des_fourier_bool.stateChanged.connect(lambda:self.change_des_fourier_bool(self.ui_info.des_fourier_bool))
        # LIMIAR
        self.check_limiar_bool = False
        self.ui_info.limiar_bool.stateChanged.connect(lambda:self.change_limiar_bool(self.ui_info.limiar_bool))
        # HUE
        self.check_hue_bool = False
        self.ui_info.hue_bool.stateChanged.connect(lambda:self.change_hue_bool(self.ui_info.hue_bool))
        # SATURATION
        self.check_saturation_bool = False
        self.ui_info.saturation_bool.stateChanged.connect(lambda:self.change_saturation_bool(self.ui_info.saturation_bool))
        # RESIZE
        self.check_resize_bool = False
        self.ui_info.resize_bool.stateChanged.connect(lambda:self.change_resize_bool(self.ui_info.resize_bool))
        # ROTATE
        self.check_rotate_bool = False
        self.ui_info.rotate_bool.stateChanged.connect(lambda:self.change_rotate_bool(self.ui_info.rotate_bool))
        # SERPIA
        self.check_serpia_bool = False
        self.ui_info.serpia_bool.stateChanged.connect(lambda:self.change_serpia_bool(self.ui_info.serpia_bool))
        # GENERIC FILTER
        self.check_generic_filter_bool = False
        self.ui_info.generic_filter_bool.stateChanged.connect(lambda:self.change_generic_filter_bool(self.ui_info.generic_filter_bool))
        # CHROMA KEY
        self.check_chroma_key_bool = False
        self.ui_info.chroma_key_bool.stateChanged.connect(lambda:self.change_chroma_key_bool(self.ui_info.chroma_key_bool))

        # FILTERS APPLY
        self.ui_info.apply_filters.clicked.connect(self.apply_checkbox_test)


        """
        COLORS
        """

        # APPLY
        self.ui_info.apply_colors_button.clicked.connect(self.apply_checkbox_test)

        # IMPORT CHROMA KEY
        self.ui_info.import_chroma_key.clicked.connect(self.chroma_key_import)
        

        # ADD WIDGETS TO APP
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)
        self.main_layout.addWidget(self.info)


        # SET CENTRAL WIDGET
        parent.setCentralWidget(self.central_frame)

    def clear(self):
        self.check_equalize_bool = False
        self.check_negative_bool = False
        self.check_log_bool = False
        self.check_lp_bool = False
        self.check_median_bool = False
        self.check_mean_simple_w_bool = False
        self.check_mean_simple_bool = False
        self.check_high_boost_bool = False
        self.check_laplacian_bool = False
        self.check_sobel_x_bool = False
        self.check_sobel_y_bool = False
        self.check_nled_bool = False
        self.check_gray_scale_mean_bool = False
        self.check_gray_scale_avg_bool = False
        self.check_low_fourier_bool = False
        self.check_high_fourier_bool = False
        self.check_des_fourier_bool = False
        self.check_limiar_bool = False
        self.check_hue_bool = False
        self.check_saturation_bool = False
        self.check_resize_bool = False
        self.check_rotate_bool = False
        self.check_serpia_bool = False
        self.check_generic_filter_bool = False
        self.check_chroma_key_bool = False

        done = self.reset_checkboxes()

        if (done):
            self.apply_checkbox_test()
    
    def reset_checkboxes(self):
        self.flag = False
        self.ui_info.negative_bool.setChecked(False)
        self.ui_info.log_bool.setChecked(False)
        self.ui_info.equalize_bool.setChecked(False)
        self.ui_info.lp_bool.setChecked(False)
        self.ui_info.median_bool.setChecked(False)
        self.ui_info.median_simple_bool.setChecked(False)
        self.ui_info.high_boost_bool.setChecked(False)
        self.ui_info.laplacian_bool.setChecked(False)
        self.ui_info.sobel_x_bool.setChecked(False)
        self.ui_info.sobel_y_bool.setChecked(False)
        self.ui_info.nled_bool.setChecked(False)
        self.ui_info.gray_scale_avg_bool.setChecked(False)
        self.ui_info.gray_scale_mean_bool.setChecked(False)
        self.ui_info.low_fourier_bool.setChecked(False)
        self.ui_info.high_fourier_bool.setChecked(False)
        self.ui_info.des_fourier_bool.setChecked(False)
        self.ui_info.limiar_bool.setChecked(False)
        self.ui_info.hue_bool.setChecked(False)
        self.ui_info.saturation_bool.setChecked(False)
        self.ui_info.resize_bool.setChecked(False)
        self.ui_info.rotate_bool.setChecked(False)
        self.ui_info.serpia_bool.setChecked(False)
        self.ui_info.generic_filter_bool.setChecked(False)
        self.ui_info.chroma_key_bool.setChecked(False)
        self.flag = True

        return True


    def display(self, arg):
        print(arg)
    
    def show_linear(self):
        points_x = self.ui_info.points_x_values.toPlainText()
        points_y = self.ui_info.points_y_values.toPlainText()

        points_x = fc.transform_points(points_x)
        points_y = fc.transform_points(points_y)

        img_curve = fc.plot_linear_parts(points_x, points_y)
        MAX_SIZE = (300, 300)
        img_curve.thumbnail(MAX_SIZE)

        # img_curve = ImageTk.PhotoImage(img_curve)
        img_lp = ImageQt(img_curve)
        self.ui_info.lp_image.setPixmap(QPixmap.fromImage(img_lp))
        

        # lbl_img_curve.configure(image=img_curve)
        # lbl_img_curve.image = img_curve

    def apply_encryption(self):
        global img_encrypted

        img_encrypted = img.encrypt(self.ui_info.esteg_entry_text.toPlainText())
    
    def apply_decryption(self):
        decrypted = img.decrypt(img_encrypted)
        self.ui_info.decrypted_label.setText(decrypted)
        self.ui_info.decrypted_label.setStyleSheet("font-size:12pt; color:#ffffff;")

    def change_negative_bool(self, new_negative_bool):
        self.check_negative_bool = new_negative_bool.isChecked()
        if self.flag:
            self.apply_checkbox_test()
            print("IT WENT THROUGH")
    
    def change_log_bool(self, new_log_bool):
        self.check_log_bool = new_log_bool.isChecked()
        if self.flag: self.apply_checkbox_test()

    def change_equalize_bool(self, new_equalize_bool):
        self.check_equalize_bool = new_equalize_bool.isChecked()
        if self.flag: self.apply_checkbox_test()

    def change_lp_bool(self, new_lp_bool):
        self.check_lp_bool = new_lp_bool.isChecked()
        if self.flag: self.apply_checkbox_test()


    """
        FILTERS FUNCTIONS
    """
    
    def change_median_bool(self, new_median_bool):
        self.check_median_bool = new_median_bool.isChecked()
        if self.flag: self.apply_checkbox_test()
    def change_median_simple_w_bool(self, median_simple_w_bool):
        self.check_mean_simple_w_bool = median_simple_w_bool.isChecked()
        if self.flag: self.apply_checkbox_test()
    def change_median_simple_bool(self, median_simple_bool):
        self.check_mean_simple_bool = median_simple_bool.isChecked()
        if self.flag: self.apply_checkbox_test()
    def change_high_boost_bool(self, high_boost_bool):
        self.check_high_boost_bool = high_boost_bool.isChecked()
        if self.flag: self.apply_checkbox_test()
    def change_laplacian_bool(self, laplacian_bool):
        self.check_laplacian_bool = laplacian_bool.isChecked()
        if self.flag: self.apply_checkbox_test()
    def change_sobel_x_bool(self, sobel_x_bool):
        self.check_sobel_x_bool = sobel_x_bool.isChecked()
        if self.flag: self.apply_checkbox_test()
    def change_sobel_y_bool(self, sobel_y_bool):
        self.check_sobel_y_bool = sobel_y_bool.isChecked()
        if self.flag: self.apply_checkbox_test()
    def change_nled_bool(self, nled_bool):
        self.check_nled_bool = nled_bool.isChecked()
        if self.flag: self.apply_checkbox_test()
    def change_gray_scale_mean_bool(self, gray_scale_mean_bool):
        self.check_gray_scale_mean_bool = gray_scale_mean_bool.isChecked()
        if self.flag: self.apply_checkbox_test()
    def change_gray_scale_avg_bool(self, gray_scale_avg_bool):
        self.check_gray_scale_avg_bool = gray_scale_avg_bool.isChecked()
        if self.flag: self.apply_checkbox_test()
    def change_low_fourier_bool(self, low_fourier_bool):
        self.check_low_fourier_bool = low_fourier_bool.isChecked()
        if self.flag: self.apply_checkbox_test()
    def change_high_fourier_bool(self, high_fourier_bool):
        self.check_high_fourier_bool = high_fourier_bool.isChecked()
        if self.flag: self.apply_checkbox_test()
    def change_des_fourier_bool(self, des_fourier_bool):
        self.check_des_fourier_bool = des_fourier_bool.isChecked()
        if self.flag: self.apply_checkbox_test()
    def change_limiar_bool(self, limiar_bool):
        self.check_limiar_bool = limiar_bool.isChecked()
        if self.flag: self.apply_checkbox_test()
    def change_hue_bool(self, hue_bool):
        self.check_hue_bool = hue_bool.isChecked()
        if self.flag: self.apply_checkbox_test()
    def change_saturation_bool(self, saturation_bool):
        self.check_saturation_bool = saturation_bool.isChecked()
        if self.flag: self.apply_checkbox_test()
    def change_resize_bool(self, resize_bool):
        self.check_resize_bool = resize_bool.isChecked()
        if self.flag: self.apply_checkbox_test()
    def change_rotate_bool(self, rotate_bool):
        self.check_rotate_bool = rotate_bool.isChecked()
        if self.flag: self.apply_checkbox_test()
    def change_serpia_bool(self, serpia_bool):
        self.check_serpia_bool = serpia_bool.isChecked()
        if self.flag: self.apply_checkbox_test()
    def change_generic_filter_bool(self, generic_filter_bool):
        self.check_generic_filter_bool = generic_filter_bool.isChecked()
        if self.flag: self.apply_checkbox_test()
    def change_chroma_key_bool(self, chroma_key_bool):
        self.check_chroma_key_bool = chroma_key_bool.isChecked()
        if self.flag: self.apply_checkbox_test()
    
    def apply_gama_brightness(self):

        self.img_display = img.gama_test(self.img_display, self.gama_slider_value/100)
        self.img_display = img.brightness_test(self.img_display, self.brightness_slider_value/100)
    
    def apply_gama(self):
        print("aplicar gama")
        # self.img_display = img.img_now
        # print("now: ", img.img_now)
        # print("original: ", img.img_original)

        # self.img_display = img.gama_test(self.img_display, self.gama_slider_value/100)
        # img.img_now = self.img_display
        
        # self.img_display = img.convert(self.img_display)

        # qim = ImageQt(self.img_display)
        # self.ui_image.image_label.setPixmap(QPixmap.fromImage(qim))
    
    def apply_brightness(self):
        print("aplicar brightness")
        # self.img_display = img.img_now

        # self.img_display = img.brightness_test(self.img_display, self.brightness_slider_value/100)
        # self.img_display = img.convert(self.img_display)

        # img.img_now = self.img_display
        # qim = ImageQt(self.img_display)
        # self.ui_image.image_label.setPixmap(QPixmap.fromImage(qim))
    
    def chroma_key_import(self):
        global chroma_key_image
        
        filename = QFileDialog.getOpenFileName(self.image, 'Open file', "", "Image files (*.jpg *.png *.tif *jpeg *.bmp)")
        chroma_key_image = filename[0]

    def apply_checkbox_test(self):
        # self.img_display = img.img_now
        # self.img_display = img.img_original

        # self.img_display = img.gama_test(self.img_display, self.gama_slider_value/100)
        # self.img_display = img.brightness_test(self.img_display, self.brightness_slider_value/100)
        print("commence")
        self.img_display = img.img_original
        print(len(self.img_display.shape))
        size = int(self.ui_info.kernel_size_select.currentText())
        radius = self.ui_info.radius_value.value()
        resize = float(self.ui_info.resize_value.currentText())
        rotate = float(self.ui_info.rotate_value.currentText())
        color_scheme = 0 # GRAY
        if(len(img.img_now.shape) > 2):
            color_scheme = 1 # COLORED
        
        # CHROMA KEY
        if (self.check_chroma_key_bool and color_scheme == 1):
            self.img_display = img.chroma_key(self.img_display, chroma_key_image)
        # RESIZE
        if(self.check_resize_bool):
            self.img_display = img.resize_i(self.img_display, fator=resize)
        
        # GAMA BRIGHTNESS
        self.apply_gama_brightness()
        
        # NEGATIVE
        if (self.check_negative_bool):
            self.img_display = img.negative_image_test(self.img_display)
        # LOG
        if (self.check_log_bool):
            self.img_display = img.log_test(self.img_display)
        # EQUALIZE
        if (self.check_equalize_bool):
            self.img_display = img.equalize_hist_test(self.img_display)
        # GRAY SCALE MEAN
        if (self.check_gray_scale_mean_bool and color_scheme == 1):
            self.img_display = img.gray_scale_mean_test(self.img_display)
            color_scheme = 0
        # GRAY SCALE AVG
        if (self.check_gray_scale_avg_bool and color_scheme == 1):
            self.img_display = img.gray_scale_avg_test(self.img_display)
            color_scheme = 0
        # MEDIAN
        if (self.check_median_bool):
            self.img_display = img.median_filter_test(self.img_display, size)
        # MEAN SIMPLE FOR BOTH
        if (self.check_mean_simple_bool):
            self.img_display = img.mean_simple_filter_test(self.img_display, size)
        # MEAN SIMPLE WEIGHTED FOR BOTH
        if (self.check_mean_simple_w_bool):
            self.img_display = img.mean_weighted_filter_test(self.img_display, size)
        # LAPLACIAN
        if (self.check_laplacian_bool and color_scheme == 0):
            self.img_display = img.laplacian_filter_test(self.img_display)
        if (self.check_laplacian_bool and color_scheme == 1):
            self.img_display = img.col_laplacian_filter_test(self.img_display)
        # if (self.check_laplacian_bool):
        #     self.img_display = img.laplacian_filter(self.img_display)
        # LOW FOURIER
        if (self.check_low_fourier_bool and color_scheme == 0):
            self.img_display = img.low_fourier_test(self.img_display, radius=radius)
        # HIGH FOURIER
        if (self.check_high_fourier_bool and color_scheme == 0):
            self.img_display = img.high_fourier_test(self.img_display, radius=radius)
        # DES FOURIER
        if (self.check_des_fourier_bool and color_scheme == 0):
            self.img_display = img.fourier_test(self.img_display)
        # HIGH BOOST FOR BOTH
        if (self.check_high_boost_bool):
            self.img_display = img.high_boost_filter_test(self.img_display)
        # SOBEL X
        if (self.check_sobel_x_bool and color_scheme == 0):
            self.img_display = img.sobel_x_filter_test(self.img_display)
        # SOBEL Y
        if (self.check_sobel_y_bool and color_scheme == 0):
            self.img_display = img.sobel_y_filter_test(self.img_display)
        # NON LINEAR EDGE DETECTION
        if (self.check_nled_bool and color_scheme == 0):
            self.img_display = img.non_linear_test(self.img_display)
        # LIMIAR
        if (self.check_limiar_bool and color_scheme == 0):
            self.img_display = img.limiar_test(self.img_display)
        # HUE
        if (self.check_hue_bool and color_scheme == 1):
            self.img_display = img.hue(self.img_display, self.hue_slider_value)
        # SATURATION
        if (self.check_saturation_bool and color_scheme == 1):
            self.img_display = img.saturation_enc(self.img_display, self.saturation_slider_value/100)
        # SERPIA
        if (self.check_serpia_bool and color_scheme == 1):
            self.img_display = img.serpia(self.img_display)
        # GENERIC FILTER
        if (self.check_generic_filter_bool and color_scheme == 0):
            m = [
                self.ui_info.a11_input.value(), self.ui_info.a12_input.value(), self.ui_info.a13_input.value(),
                self.ui_info.a21_input.value(), self.ui_info.a22_input.value(), self.ui_info.a23_input.value(),
                self.ui_info.a31_input.value(), self.ui_info.a32_input.value(), self.ui_info.a33_input.value()
            ]
            print(m)
            self.img_display = img.generic_filter(self.img_display,
                fc.matriz_convert(
                    m[0], m[1], m[2], m[3], m[4], m[5], m[6], m[7], m[8]
                )
            ).clip(0, 255)
            print(self.img_display)

        if (self.check_lp_bool) == True:
            if (len(self.ui_info.points_x_values.toPlainText()) > 0):
                points_x = self.ui_info.points_x_values.toPlainText()
                points_y = self.ui_info.points_y_values.toPlainText()

                points_x = fc.transform_points(points_x)
                points_y = fc.transform_points(points_y)

                self.img_display = img.linear_parts_test(points_x, points_y, self.img_display)
        if(self.check_rotate_bool):
            self.img_display = img.rotate_i(self.img_display, rot=rotate)

        # print(type(self.img_display))
        # qimage = QtGui.QImage(self.img_display, self.img_display.shape[1], self.img_display.shape[0], self.img_display.shape[1]*2, QtGui.QImage.Format_Grayscale16)

        # self.img_display = img.convert(self.img_display)
        qim2 = img.convert(self.img_display)
        # print("qpixmap", self.img_display.toqpixmap)
        # print("type", type(self.img_display))

        # img.img_now = np.array(self.img_display)
        # qim = ImageQt(self.img_display)
        self.ui_image.image_label.setPixmap(QPixmap.fromImage(qim2))

        MAX_SIZE = (300, 300)

        hist_plot = img.histogram_plot(self.img_display)
        hist_plot.thumbnail(MAX_SIZE)
        img_hist_plot = ImageQt(hist_plot)
        self.ui_info.histogram_image.setPixmap(QPixmap.fromImage(img_hist_plot))

        if (color_scheme == 1):
            colored_hist_plot = img.colored_hist(self.img_display)
            colored_hist_plot.thumbnail(MAX_SIZE)
            img_colored_hist_plot = ImageQt(colored_hist_plot)
            self.ui_info.color_histogram_image.setPixmap(QPixmap.fromImage(img_colored_hist_plot))

        print("done")

    def gama_slider_changed(self):
        new_slider_value = str(self.ui_info.gama_slider.value())
        self.gama_slider_value = self.ui_info.gama_slider.value()
        self.ui_info.gama_value_label.setText(new_slider_value)
        self.ui_info.gama_value_label.setStyleSheet(" font-size:12pt; color:#ffffff;")
        self.apply_gama()

    def brightness_slider_changed(self):
        new_slider_value = str(self.ui_info.brightness_slider.value())
        self.brightness_slider_value = self.ui_info.brightness_slider.value()
        self.ui_info.brightness_value_label.setText(new_slider_value)
        self.ui_info.brightness_value_label.setStyleSheet(" font-size:12pt; color:#ffffff;")
        self.apply_brightness()
        
    def hue_slider_changed(self):
        new_slider_value = str(self.ui_info.hue_slider.value())
        self.hue_slider_value = self.ui_info.hue_slider.value()
        print(self.hue_slider_value)
        self.ui_info.hue_value_label.setText(new_slider_value)
        self.ui_info.hue_value_label.setStyleSheet(" font-size:12pt; color:#ffffff;")

    def saturation_slider_changed(self):
        new_slider_value = str(self.ui_info.saturation_slider.value())
        self.saturation_slider_value = self.ui_info.saturation_slider.value()
        self.ui_info.saturation_value_label.setText(new_slider_value)
        self.ui_info.saturation_value_label.setStyleSheet(" font-size:12pt; color:#ffffff;")

    def import_image(self):

        global img
        global img_s
        global window
        global lbl_img
        global lbl_hist
        global curve

        self.flag = True

        fname = QFileDialog.getOpenFileName(self.image, 'Open file', "", "Image files (*.jpg *.png *.tif *jpeg *.bmp)")
        image_path = fname[0]

        img = Img(image_path)
        self.img_display = img.img_now
        print(img.size())

        img_pixmap = QtGui.QPixmap(image_path)
        self.ui_image.image_label.setPixmap(QPixmap(img_pixmap))

        # First Histogram
        hist_plot = img.histogram_plot(self.img_display)
        MAX_SIZE = (300, 300)
        hist_plot.thumbnail(MAX_SIZE)
        img_hist_plot = ImageQt(hist_plot)
        self.ui_info.histogram_image.setPixmap(QPixmap.fromImage(img_hist_plot))

        if (len(img.img_now.shape) > 2):
            colored_hist_plot = img.colored_hist(self.img_display)
            colored_hist_plot.thumbnail(MAX_SIZE)
            img_colored_hist_plot = ImageQt(colored_hist_plot)
            self.ui_info.color_histogram_image.setPixmap(QPixmap.fromImage(img_colored_hist_plot))
    
    def to_linear_parts(self):
        self.info.setCurrentWidget(self.ui_info.linear_parts)

    def to_esteganography(self):
        self.info.setCurrentWidget(self.ui_info.esteganography)

    def to_general(self):
        self.info.setCurrentWidget(self.ui_info.general)
    
    def to_filters(self):
        self.info.setCurrentWidget(self.ui_info.filters)

    def to_generic_filter(self):
        self.info.setCurrentWidget(self.ui_info.generic_filter)

    def to_colors(self):
        self.info.setCurrentWidget(self.ui_info.colors)

    def apply_checkbox(self, checkbox_type, checkbox):
        if checkbox.isChecked():
            if(checkbox_type == 1):
                img_now = img.negative_image()
            elif(checkbox_type == 2):
                img_now = img.log_apply()
        else:
            img_now = img.img
        
        qim = ImageQt(img_now)
        self.ui_image.image_label.setPixmap(QPixmap.fromImage(qim))
    
    def apply(self):
        gama = self.ui_info.gama_slider.value()
        brightness = self.ui_info.brightness_slider.value()

        self.img_display = img.gama_apply(gama/100)
        self.img_display = img.brightness_apply(brightness/100)

        qim = ImageQt(self.img_display)
        self.ui_image.image_label.setPixmap(QPixmap.fromImage(qim))
