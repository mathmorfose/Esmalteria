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

        # TOGGLE MENU
        ########################################################################
        self.ui.btn_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 150, True))

        # PAGES
        ########################################################################

        # PAGINA NOVO CLIENTE
        self.ui.btn_users.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_menu))
        self.ui.btn_users.clicked.connect(lambda: UIFunctions.toggleMenu(self, 150, True))

        # NEW
        self.ui.menu_btn_new.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_newUser))
        self.ui.newUser_btn_cancel.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_menu))
        self.ui.newUser_btn_conclude.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_menu))
        self.ui.newUser_btn_conclude.clicked.connect(lambda: user.add_new(self))

        # EDIT
        self.ui.menu_btn_edit.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_editUser))
        self.ui.menu_btn_edit.clicked.connect(lambda: UIFunctions.fill_clientBoxes(self.ui.editUser_nameBox))
        self.ui.editUser_btn_cancel.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_menu))
        self.ui.editUser_btn_conclude.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_menu))
        self.ui.editUser_btn_conclude.clicked.connect(lambda: user.edit(self))
        self.ui.editUser_nameBox.currentTextChanged.connect(lambda: user.fill_edit_inputs(self))

        # DELETE
        self.ui.menu_btn_delete.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_deleteUser))
        self.ui.menu_btn_delete.clicked.connect(lambda: UIFunctions.fill_clientBoxes(self.ui.deleteUser_box_names))
        self.ui.deleteUser_btn_cancel.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_menu))
        self.ui.deleteUser_btn_conclude.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_menu))
        self.ui.deleteUser_btn_conclude.clicked.connect(lambda: user.delete(self.ui.deleteUser_box_names))

        # PAGINA ESTOQUE
        self.ui.btn_stock.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_stock))
        self.ui.btn_stock.clicked.connect(lambda: stock.show_items(self.ui.stock_list))
        self.ui.btn_stock.clicked.connect(lambda: UIFunctions.toggleMenu(self, 150, True))

        self.ui.stock_btn_update.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_stock_update))
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

        # PAGINA AGENDA
        self.ui.btn_schedule.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_toSchedule))
        self.ui.btn_schedule.clicked.connect(lambda: UIFunctions.fill_clientBoxes(self.ui.toSchedule_box_users))
        self.ui.btn_schedule.clicked.connect(lambda: UIFunctions.toggleMenu(self, 150, True))
        self.ui.toSchedule_calendar.selectionChanged.connect(lambda: toSchedule.show_date(self))
        self.ui.toSchedule_btn_conclude.clicked.connect(lambda: toSchedule.update_schedule(self))

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
