from PyQt6.QtWidgets import QMessageBox


class Classe_Alertas():
    def __init__(self):
        super().__init__()

    def alerta_cliente_editado(self):
            msg = QMessageBox()
            msg.setWindowTitle("Sucesso!")
            msg.setText("Cliente editado!")
            msg.setIcon(QMessageBox.Icon.Information)   
            msg.exec() 

    def alerta_registro(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alerta!")
        msg.setText("Registro Não Encontrado!")
        msg.setIcon(QMessageBox.Icon.Information)   
        msg.exec()
   
    
    def alerta_valor_invalido(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alerta!")
        msg.setText("Valor inválido!")
        msg.setIcon(QMessageBox.Icon.Information)   
        msg.exec()
    

    def alt_cnpj_invalido(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alerta!")
        msg.setText("Cnpj Inválido!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()   

    
    def alt_cep_invalido(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alerta!")
        msg.setText("O Cep está inválido!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()    

    
    def alt_erro_cad_nivel_acesso(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alerta!")
        msg.setText("Selecione um Nível de Acesso do Usuário!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

    def alt_erro_cad_permissao(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alerta!")
        msg.setText("Selecione as Permissões de Acesso do Usuário!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

    def alt_cad_em_branco(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alerta!")
        msg.setText("Complete os Campos em Branco!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

    def alt_senha_diferente(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alerta!")
        msg.setText("As Senhas Estão Diferentes!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

    def alt_insirir_produto(self):
        msg = QMessageBox()
        msg.setWindowTitle("Atenção!")
        msg.setText("Insira um produto")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

    def valor_invalido(self):
        msg = QMessageBox()
        msg.setWindowTitle("Atenção!")
        msg.setText("Insira um valor válido, utilize ponto no lugar da vírgula")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

    def alt_remover_linha(self):
        msg = QMessageBox()
        msg.setWindowTitle("Atenção!")
        msg.setText("Selecione um produto para remover")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()
        
    def alt_campo_invalido(self):
        msg = QMessageBox()
        msg.setWindowTitle("Verifique!")
        msg.setText("Algum campo do produto buscado pode está incorreto.")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

    
    def alt_cadastro_sucesso(self):
        msg = QMessageBox()
        msg.setWindowTitle("Parabéns!")
        msg.setText("Usuário Cadastrado Com Sucesso!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

    
    def alerta_produto_cadastrado(self):
        msg = QMessageBox()
        msg.setWindowTitle("Sucesso!")
        msg.setText("Produto cadastrado!")
        msg.setIcon(QMessageBox.Icon.Information)   
        msg.exec()

    
    def alerta_produto_editado(self):
        msg = QMessageBox()
        msg.setWindowTitle("Sucesso!")
        msg.setText("Produto editado!")
        msg.setIcon(QMessageBox.Icon.Information)   
        msg.exec()


    def alerta_pagamento(self):
        msg = QMessageBox()
        msg.setWindowTitle("Atenção!")
        msg.setText("Selecione o tipo de pagamento!")
        msg.setIcon(QMessageBox.Icon.Information)   
        msg.exec() 

    
    def alerta_id_cliente(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alerta!")
        msg.setText(f"Cliente com ID {self.valor_id_cliente_venda} não encontrado")
        msg.setIcon(QMessageBox.Icon.Information)   
        msg.exec()