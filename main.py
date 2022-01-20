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
        self.ui.pages_widget.setCurrentWidget(self.ui.page_inicial)

        # TOGGLE MENU
        ########################################################################
        self.ui.btn_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 150, True))

        # PAGES
        ########################################################################

        # PAGINA NOVO CLIENTE
        self.ui.btn_user.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_user))
        self.ui.btn_user.clicked.connect(lambda: UIFunctions.toggleMenu(self, 150, True))

        # NEW
        self.ui.btn_addnewuser.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_user_new))
        self.ui.btn_cancelar_newuser.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_user))
        self.ui.btn_concluir_newuser.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_user))
        self.ui.btn_concluir_newuser.clicked.connect(lambda: user.add_new(self))

        # EDIT
        self.ui.btn_edituser.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_user_edit))
        self.ui.btn_edituser.clicked.connect(lambda: UIFunctions.fill_clientBoxes(self.ui.caixa_nomes_edit))
        self.ui.btn_cancelar_edit.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_user))
        self.ui.btn_concluir_edit.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_user))
        self.ui.btn_concluir_edit.clicked.connect(lambda: user.edit(self))
        self.ui.caixa_nomes_edit.currentTextChanged.connect(lambda: user.fill_edit_inputs(self))

        # DELETE
        self.ui.btn_removeuser.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_user_remove))
        self.ui.btn_removeuser.clicked.connect(lambda: UIFunctions.fill_clientBoxes(self.ui.caixa_nomes_remove))
        self.ui.btn_cancelar_remove.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_user))
        self.ui.btn_concluir_remove.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_user))
        self.ui.btn_concluir_remove.clicked.connect(lambda: user.delete(self.ui.caixa_nomes_remove))

        # PAGINA ESTOQUE
        self.ui.btn_estoque.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_estoque))
        self.ui.btn_estoque.clicked.connect(lambda: stock.show_items(self.ui.lista_estoque))
        self.ui.btn_estoque.clicked.connect(lambda: UIFunctions.toggleMenu(self, 150, True))

        self.ui.btn_altqntd.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_estoque_altqntd))
        self.ui.btn_altqntd.clicked.connect(lambda: stock.modify_item_quantity(self.ui.caixa_itens_altqntd))

        self.ui.btn_cancelar_altqntd.clicked.connect(
            lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_estoque))
        self.ui.btn_cancelar_additem.clicked.connect(
            lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_estoque))

        self.ui.btn_concluir_additem.clicked.connect(
            lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_estoque))
        self.ui.btn_concluir_additem.clicked.connect(lambda: stock.add_new_item(self))

        self.ui.btn_addnewitem.clicked.connect(
            lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_estoque_additem))

        self.ui.btn_concluir_altqntd.clicked.connect(
            lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_estoque))
        self.ui.btn_concluir_altqntd.clicked.connect(lambda: stock.update_item_quantity(self))

        # PAGINA AGENDA
        self.ui.btn_agenda.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_agendar))
        self.ui.btn_agenda.clicked.connect(lambda: UIFunctions.fill_clientBoxes(self.ui.caixa_agendar_nomes))
        self.ui.btn_agenda.clicked.connect(lambda: UIFunctions.toggleMenu(self, 150, True))
        self.ui.calendario_agendar.selectionChanged.connect(lambda: toSchedule.show_date(self))
        self.ui.btn_concluir_agendar.clicked.connect(lambda: toSchedule.update_schedule(self))

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
