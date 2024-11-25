import pandas as pd
from model.jogadores import Jogador
from conexion.mongo_queries import MongoQueries

class Controller_Jogador:
    def __init__(self):
        self.mongo = MongoQueries()
    
    def inserir_jogador(self) -> Jogador:
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        id_jogador = int(input("Novo ID de jogador (numero inteiro positivo): "))
        while id_jogador < 1:
            id_jogador = int(input("Insira um numero inteiro positivo para o novo Id de jogador: "))
        
        if self.verifica_existencia_jogador(id_jogador):
            nome_jogador = input("Nome do novo jogador: ")
            print("""Escolha a região do jogador: 
                    1 - America do Sul
                    2 - America Central
                    3 - America do Norte
                    4 - Europa
                    5 - Ásia
                    6 - Oriente Médio
                  """)
            opcao = int(input("Digite uma opção: "))
            while( opcao < 0 or opcao > 6):
                opcao = int(input("Digite uma opção válida: "))
            
            if(opcao == 1):
                regiao = "america do sul"
            elif(opcao == 2):
                regiao = "america central"
            elif(opcao == 3):
                regiao = "america do norte"
            elif(opcao == 4):
                regiao = "europa"
            elif(opcao == 5):
                regiao = "asia"
            elif(opcao == 6):
                regiao = "oriente medio"
            
            # Insere e persiste o novo jogador
            self.mongo.db["jogadores"].insert_one({"id_jogador": id_jogador, "nome_jogador": nome_jogador, "regiao": regiao})
            # Recupera os dados do novo jogador criado transformando em um DataFrame
            df_jogador = self.recupera_jogador(id_jogador)
            # Cria um novo objeto Jogador
            novo_jogador = Jogador(df_jogador.id_jogador.values[0], df_jogador.nome_jogador.values[0], df_jogador.regiao.values[0])
            # Exibe os atributos do novo Jogador
            print(novo_jogador.to_string())
            input("Pressione enter para sair")
            self.mongo.close()
            # Retorna o objeto novo_jogador para utilização posterior, caso necessário
            return novo_jogador
        else:
            self.mongo.close()
            print(f"O ID {id_jogador} já está cadastrado.")
            input("Pressione enter para sair")
            return None
    
    def atualizar_jogador(self) -> Jogador:
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        id_jogador = int(input("Informe o ID do jogador que deseja atualizar: "))

        if not self.verifica_existencia_jogador(id_jogador):
            nome_jogador = input("Novo Nome do jogador: ")

            print("""Escolha a região do jogador: 
                    1 - America do Sul
                    2 - America Central
                    3 - America do Norte
                    4 - Europa
                    5 - Ásia
                    6 - Oriente Médio
                  """)
            opcao = int(input("Digite uma opção: "))
            while( opcao < 0 or opcao > 6):
                opcao = int(input("Digite uma opção válida: "))
            
            if(opcao == 1):
                regiao = "america do sul"
            elif(opcao == 2):
                regiao = "america central"
            elif(opcao == 3):
                regiao = "america do norte"
            elif(opcao == 4):
                regiao = "europa"
            elif(opcao == 5):
                regiao = "asia"
            elif(opcao == 6):
                regiao = "oriente medio"            
            # Atualiza o nome do jogador existente
            self.mongo.db["jogadores"].update_one({"id_jogador": id_jogador}, {"$set": {"nome_jogador": nome_jogador, "regiao": regiao}})
            # Recupera os dados do novo jogador criado transformando em um DataFrame
            df_jogador = self.recupera_jogador(id_jogador)
            # Cria um novo objeto jogador
            jogador_atualizado = Jogador(df_jogador.id_jogador.values[0], df_jogador.nome_jogador.values[0], df_jogador.regiao.values[0])
            # Exibe os atributos do novo Jogador
            print(jogador_atualizado.to_string())
            input("Pressione enter para sair")
            self.mongo.close()
            # Retorna o objeto jogador_atualizado para utilização posterior, caso necessário
            return jogador_atualizado
        else:
            self.mongo.close()
            print(f"O ID {id_jogador} não existe.")
            input("Pressione enter para sair")
            return None
    
    def excluir_jogador(self):
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        id_jogador = int(input("Informe o ID do jogador que deseja atualizar: "))
        if not self.verifica_existencia_jogador(id_jogador):
            # Recupera os dados do jogador transformando em um DataFrame
            df_jogador = self.recupera_jogador(id_jogador)
            # Revome o jogador da tabela
            self.mongo.db["jogadores"].delete_one({"id_jogador":id_jogador})
            # Cria um novo objeto Jogador para informar que foi removido
            jogador_excluido = Jogador(df_jogador.id_jogador.values[0], df_jogador.nome_jogador.values[0], df_jogador.regiao.values[0])
            self.mongo.close()
            # Exibe os atributos do jogador excluído
            print("Jogador Removido com Sucesso!")
            print(jogador_excluido.to_string())
            input("Pressione enter para sair")
        else:
            self.mongo.close()
            print(f"O ID {id_jogador} não existe.")
            input("Pressione enter para sair")

    def verifica_existencia_jogador(self, id_jogador:int=None, external:bool=False) -> bool:
        if external:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect()
        
        # Recupera os dados do novo jogador criado transformando em um DataFrame
        df_jogador = pd.DataFrame(self.mongo.db["jogadores"].find({"id_jogador":id_jogador}, {"id_jogador": 1, "nome_jogador": 1, "regiao": 1, "_id": 0}))

        if external:
            # Fecha a conexão com o Mongo
            self.mongo.close()
        
        return df_jogador.empty
    
    def recupera_jogador(self, id_jogador:int=None, external:bool=False) -> pd.DataFrame:
        if external:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect()
        
        # Recupera os dados do novo jogador criado transformando em um DataFrame
        df_jogador = pd.DataFrame(list(self.mongo.db["jogadores"].find({"id_jogador":id_jogador}, {"id_jogador": 1, "nome_jogador": 1, "regiao": 1, "_id": 0})))

        if external:
            # Fecha a conexão com o Mongo
            self.mongo.close()

        return df_jogador