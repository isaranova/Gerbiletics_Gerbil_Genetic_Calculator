import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5 import uic
from gerbiletics_source import *
from support_file import genotype_phenotype

"""if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)"""

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
        self.ui.phen_mom.activated.connect(self.show_mom_genotype)
        self.ui.phen_dad.activated.connect(self.show_dad_genotype)

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

    def show_mom_genotype(self):
        genotype_mom = Genotype(genotype_phenotype[self.ui.phen_mom.currentText()])

        ui_genes_mom = [self.ui.a_mom, 
                        self.ui.c_mom, 
                        self.ui.d_mom,
                        self.ui.e_mom,
                        self.ui.g_mom, 
                        self.ui.p_mom
        ]
        

        for i in range(6):
            g = genotype_mom.genes[i].name.replace('.', ' ')
            index = ui_genes_mom[i].findText(g)
            ui_genes_mom[i].setCurrentIndex(index)
    
    def show_dad_genotype(self):
        genotype_dad = Genotype(genotype_phenotype[self.ui.phen_dad.currentText()])
        
        ui_genes_dad = [self.ui.a_dad,
                        self.ui.c_dad,
                        self.ui.d_dad,
                        self.ui.e_dad,
                        self.ui.g_dad,
                        self.ui.p_dad
        ]
        
        for i in range(6):
            g = genotype_dad.genes[i].name.replace('.', ' ')
            index = ui_genes_dad[i].findText(g)
            ui_genes_dad[i].setCurrentIndex(index)
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
