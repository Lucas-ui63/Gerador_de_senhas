import sqlite3
class Lista:
    def __init__(self, banco):
        self.banco = banco
    def add(self):
        try:
            entrada = input('Digite a tarefa a ser adicionada:')  
            self.banco.inserir_dados(entrada) 
        
        except Exception as e:
            print(e)              
        except:
            print('Erro ao adicionar tarefa')
    def remove(self):
        try:
            remover = input('Digite a tarefa a ser removida:')
            self.banco.remover_dados(remover)
            
        except Exception as e:
            print(e)
        except:
            print('O item nao foi encontrado na lista')
    def listar(self):
        try:
            print(self.banco.ler_dados())
        except Exception as e:
            print(e)
        except:
            print('A lista esta vazia')
    
class SQlite:
    def __init__(self):
        conn = self.conexao()
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY,
            tarefa TEXT
        )
        """)
        conn.commit()
        conn.close()
    def conexao(self):
        try:
            conn = sqlite3.connect('tarefas.db')
            return conn
        except:
            print('Erro ao conectar ao banco de dados')
    def inserir_dados(self,entrada):
        conn = self.conexao()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tarefas (tarefa) VALUES (?)", (entrada,))
        conn.commit()
        conn.close()
    def remover_dados(self,remover):
        conn = self.conexao()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tarefas WHERE tarefa = ?", (remover,))
        conn.commit()
        conn.close()
    def ler_dados(self):
        conn = self.conexao()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tarefas")
        dados = cursor.fetchall()
        conn.close()
        return dados
    
banco = SQlite()    
opcoes = Lista(banco)
while True:
    opcao = input('Escolha uma opção:\n1 - Adicionar\n2 - Remover\n3 - Listar\n4 - Sair')
    if opcao == '1':
        opcoes.add()
    elif opcao == '2':
        opcoes.remove()
    elif opcao == '3':
        opcoes.listar()
    elif opcao == '4':
        break
    else:
        print('Opção inválida')