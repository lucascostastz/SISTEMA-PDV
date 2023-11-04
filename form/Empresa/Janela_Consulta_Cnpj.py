from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from form.Empresa.Form_Consulta_cnpj import Ui_Form_Consulta_Cnpj


class Classe_Consulta_Cnpj(QMainWindow, Ui_Form_Consulta_Cnpj):
    def __init__(self):
        super(Classe_Consulta_Cnpj, self).__init__()
        self.setupUi(self)
        
        self.Bt_Voltar.clicked.connect(self.sair)

    def sair(self):
        self.Tx_Cnpj.clear()
        self.tx_Cep.clear()
        self.tx_Bairro.clear()
        self.tx_Email.clear()
        self.tx_municipio.clear()
        self.tx_Nome.clear()
        self.tx_Uf.clear()
        self.tx_Telefone.clear()
        self.tx_Numero.clear()
        self.txLogradouro.clear()
        self.close()       
      
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    system = Classe_Consulta_Cnpj()
    system.show()
    sys.exit(app.exec())