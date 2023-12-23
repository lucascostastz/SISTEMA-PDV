import mysql.connector
import sqlite3


def criar_tabelas():
  bc = sqlite3.connect('banco.db')
  cur = bc.cursor() 
  cur.execute("SELECT *FROM informacoes")
  dados_lidos = cur.fetchall()
  ip = dados_lidos[0][0]
  porta = dados_lidos[0][1]
  usuario = dados_lidos[0][2]
  senha = dados_lidos[0][3]
  banco = mysql.connector.connect(
  host=ip,
  user=usuario,
  port=porta,
  password=senha)
  # Crie um objeto cursor
  mycursor = banco.cursor()
  # Crie um banco de dados
  mycursor.execute("CREATE DATABASE if not exists pdv")
  # Use o banco de dados
  mycursor.execute("USE pdv")
  # Crie uma tabela
  mycursor.execute("CREATE TABLE if not exists usuarios (idusuarios INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(45), login VARCHAR(45), senha1 VARCHAR(45), senha2 VARCHAR(45), nivel_de_acesso VARCHAR(45), permissao VARCHAR(45))")
  mycursor.execute("INSERT INTO usuarios (nome, login, senha1, senha2, nivel_de_acesso, permissao) VALUES ('ADMIN', 'ADMIN', 'ADMIN', 'ADMIN', 'ADMINISTRADOR', 'TODAS')")
  mycursor.execute("CREATE TABLE if not exists produtos(idprodutos INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, descricao VARCHAR(65), categoria VARCHAR(45), marca VARCHAR(45), estoque VARCHAR(10), codigo VARCHAR(45), preco VARCHAR(15), v_atacado VARCHAR(15), v_varejo VARCHAR(15), qm_atacado VARCHAR(10), data_cadastro VARCHAR(20), validade VARCHAR(20), imagem VARCHAR(300))")
  mycursor.execute("CREATE TABLE if not exists clientes (idclientes INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY , nome VARCHAR(50), cpf VARCHAR(21), rg VARCHAR(21), telefone VARCHAR(25), email VARCHAR(45), cep VARCHAR(21), endereco VARCHAR(65), numero VARCHAR(10), bairro VARCHAR(65), cidade VARCHAR(65), estado VARCHAR(45), credito VARCHAR(15), credito_utilizado VARCHAR(15), credito_saldo VARCHAR(15))")
  mycursor.execute("CREATE TABLE if not exists empresa (idempresa INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY , razaosocial VARCHAR(70), cnpj VARCHAR(45), ie VARCHAR(25), telefone VARCHAR(25), email VARCHAR(45), endereco VARCHAR(65), logoempresa VARCHAR(165))")
  mycursor.execute("CREATE TABLE if not exists vendas (idvendas INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY , data VARCHAR(21), valor_venda VARCHAR(15), operador VARCHAR(45), tipo_venda VARCHAR(25), cliente VARCHAR(45))")
  mycursor.execute("CREATE TABLE if not exists configuracoes (idconfiguracoes INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY , categorias VARCHAR(45))")
  banco.commit()
  # Feche o cursor e a conexão com o banco de dados
  mycursor.close()
  banco.close()
criar_tabelas()

