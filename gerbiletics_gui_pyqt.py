import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5 import uic
from gerbiletics_source import *
from support_file import genotype_phenotype

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

Ui_MainWindow, QtBaseClass = uic.loadUiType("gerbiletics_gui.ui")


def create_genotype(a, c, d, e, g, p):
    genotype = ""
    genes = [a, c, d, e, g, p]
    for i in range(6):
        genes[i] = genes[i].replace(' ', '.')
    genotype = ','.join(genes)
    return genotype


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.phen_mom.addItems(list(genotype_phenotype.keys()))
        self.ui.phen_dad.addItems(list(genotype_phenotype.keys()))
        self.ui.phen_mom.addItem('Unknown')
        self.ui.phen_dad.addItem('Unknown')
        self.ui.a_mom.currentTextChanged.connect(self.show_mom_dad_phenotype)
        self.ui.c_mom.currentTextChanged.connect(self.show_mom_dad_phenotype)
        self.ui.d_mom.currentTextChanged.connect(self.show_mom_dad_phenotype)
        self.ui.e_mom.currentTextChanged.connect(self.show_mom_dad_phenotype)
        self.ui.g_mom.currentTextChanged.connect(self.show_mom_dad_phenotype)
        self.ui.p_mom.currentTextChanged.connect(self.show_mom_dad_phenotype)
        self.ui.a_dad.currentTextChanged.connect(self.show_mom_dad_phenotype)
        self.ui.c_dad.currentTextChanged.connect(self.show_mom_dad_phenotype)
        self.ui.d_dad.currentTextChanged.connect(self.show_mom_dad_phenotype)
        self.ui.e_dad.currentTextChanged.connect(self.show_mom_dad_phenotype)
        self.ui.g_dad.currentTextChanged.connect(self.show_mom_dad_phenotype)
        self.ui.p_dad.currentTextChanged.connect(self.show_mom_dad_phenotype)



    def show_mom_dad_phenotype(self):
        mom = Genotype(create_genotype(str(self.ui.a_mom.currentText()),
                                       str(self.ui.c_mom.currentText()),
                                       str(self.ui.d_mom.currentText()),
                                       str(self.ui.e_mom.currentText()),
                                       str(self.ui.g_mom.currentText()),
                                       str(self.ui.p_mom.currentText())))

        dad = Genotype(create_genotype(str(self.ui.a_dad.currentText()),
                                       str(self.ui.c_dad.currentText()),
                                       str(self.ui.d_dad.currentText()),
                                       str(self.ui.e_dad.currentText()),
                                       str(self.ui.g_dad.currentText()),
                                       str(self.ui.p_dad.currentText())))

        mom_color = mom.genotype_to_phenotype()
        dad_color = dad.genotype_to_phenotype()

        index = self.ui.phen_mom.findText(mom_color[0])
        if index >= 0:
            self.ui.phen_mom.setCurrentIndex(index)
        else:
            index = self.ui.phen_mom.findText('Unknown')
            self.ui.phen_mom.setCurrentIndex(index)

        index = self.ui.phen_dad.findText(dad_color[0])
        if index >= 0:
            self.ui.phen_dad.setCurrentIndex(index)
        else:
            index = self.ui.phen_dad.findText('Unknown')
            self.ui.phen_dad.setCurrentIndex(index)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
