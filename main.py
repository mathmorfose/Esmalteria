import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from GUI import Ui_MainWindow

# IMPORT FUNCTIONS
from gui_functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pages_widget.setCurrentWidget(self.ui.page_login)
        self.ui.frame_toggle.hide()
        self.ui.incorrect_login.hide()
        self.ui.login_btn_connect.clicked.connect(lambda: self.autentication())

        # SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        # ==> END

    def autentication(self):
        if self.ui.login_input_name.text() == "admin" and self.ui.login_input_password.text() == "1234":
            self.login()
        else:
            self.ui.incorrect_login.show()
            self.ui.login_incorrect_btn.clicked.connect(lambda: self.ui.incorrect_login.hide())


    def login(self):
        # TOGGLE MENU
        ########################################################################
        self.ui.frame_toggle.show()
        self.ui.btn_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 150, True))

        # MENU
        self.ui.pages_widget.setCurrentWidget(self.ui.page_menu)
        self.ui.menu_btn_users.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_userControl))
        self.ui.menu_btn_stock.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_stock))
        self.ui.menu_btn_schedule.clicked.connect(
            lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_toSchedule))

        # PAGES
        ########################################################################

        self.ui.btn_users.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_userControl))
        self.ui.btn_users.clicked.connect(lambda: UIFunctions.toggleMenu(self, 150, True))

        # USER CONTROL

        ## NEW
        self.ui.userControl_btn_new.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_newUser))
        self.ui.newUser_btn_cancel.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_userControl))
        self.ui.newUser_btn_conclude.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_userControl))
        self.ui.newUser_btn_conclude.clicked.connect(lambda: user.add_new(self))

        ## EDIT
        self.ui.userControl_btn_edit.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_editUser))
        self.ui.userControl_btn_edit.clicked.connect(lambda: UIFunctions.fill_clientBoxes(self.ui.editUser_nameBox))
        self.ui.editUser_btn_cancel.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_userControl))
        self.ui.editUser_btn_conclude.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_editUser))
        self.ui.editUser_btn_conclude.clicked.connect(lambda: user.edit(self))
        self.ui.editUser_nameBox.currentTextChanged.connect(lambda: user.fill_edit_inputs(self))

        ## DELETE
        self.ui.userControl_btn_delete.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_deleteUser))
        self.ui.userControl_btn_delete.clicked.connect(lambda: UIFunctions.fill_clientBoxes(self.ui.deleteUser_box_names))
        self.ui.deleteUser_btn_cancel.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_userControl))
        self.ui.deleteUser_btn_conclude.clicked.connect(
            lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_menu))
        self.ui.deleteUser_btn_conclude.clicked.connect(lambda: user.delete(self.ui.deleteUser_box_names))

        # STOCK
        self.ui.btn_stock.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_stock))
        self.ui.btn_stock.clicked.connect(lambda: stock.show_items(self.ui.stock_list))
        self.ui.btn_stock.clicked.connect(lambda: UIFunctions.toggleMenu(self, 150, True))

        self.ui.stock_btn_update.clicked.connect(
            lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_stock_update))
        self.ui.stock_btn_update.clicked.connect(lambda: stock.modify_item_quantity(self.ui.stock_update_box_items))

        self.ui.stock_update_btn_cancel.clicked.connect(
            lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_stock))
        self.ui.stock_new_btn_cancel.clicked.connect(
            lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_stock))

        self.ui.stock_new_btn_conclude.clicked.connect(
            lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_stock))
        self.ui.stock_new_btn_conclude.clicked.connect(lambda: stock.add_new_item(self))

        self.ui.stock_btn_new.clicked.connect(
            lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_stock_new))

        self.ui.stock_update_btn_conclude.clicked.connect(
            lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_stock))
        self.ui.stock_update_btn_conclude.clicked.connect(lambda: stock.update_item_quantity(self))

        # SCHEDULE
        self.ui.btn_schedule.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_toSchedule))
        self.ui.btn_schedule.clicked.connect(lambda: UIFunctions.fill_clientBoxes(self.ui.toSchedule_box_users))
        self.ui.btn_schedule.clicked.connect(lambda: UIFunctions.toggleMenu(self, 150, True))
        self.ui.toSchedule_calendar.selectionChanged.connect(lambda: toSchedule.show_date(self))
        self.ui.toSchedule_btn_conclude.clicked.connect(lambda: toSchedule.update_schedule(self))
        self.ui.toSchedule_btn_cancel.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_menu))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
