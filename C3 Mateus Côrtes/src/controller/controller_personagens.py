import pandas as pd
from model.personagens import Personagem
from conexion.mongo_queries import MongoQueries

class Controller_Personagem:
    def __init__(self):
        self.mongo = MongoQueries()

    def inserir_personagem(self) -> Personagem:
        self.mongo.connect()

        id_personagem = int(input("Novo ID de personagem (numero inteiro positivo): "))
        while id_personagem < 1:
            id_personagem = int(input("Insira um numero inteiro positivo para o novo Id de personagem: "))
        
        if self.verifica_existencia_personagem(id_personagem):
            nome_personagem = input("Nome do novo personagem: ")

            self.mongo.db["personagens"].insert_one({"id_personagem": id_personagem, "nome_personagem": nome_personagem})

            df_personagem = self.recupera_personagem(id_personagem)

            novo_personagem = Personagem(df_personagem.id_personagem.values[0], df_personagem.nome_personagem.values[0])

            print(novo_personagem.to_string())
            input("Pressione enter para sair")

            self.mongo.close()
            
            return # novo_personagem
        else:
            self.mongo.close()
            print(f"O ID {id_personagem} já está cadastrado.")
            input("Pressione enter para sair")
            return None
    
    def atualizar_personagem(self) -> Personagem:
        self.mongo.connect()

        id_personagem = int(input("Informe o ID do personagem que deseja atualizar: "))

        if not self.verifica_existencia_personagem(id_personagem):
            nome_personagem = input("Novo nome do personagem: ")

            self.mongo.db["personagens"].update_one({"id_personagem": id_personagem}, {"$set": {"nome_personagem": nome_personagem}})

            df_personagem = self.recupera_personagem(id_personagem)

            personagem_atualizado = Personagem(df_personagem.id_personagem.values[0], df_personagem.nome_personagem.values[0])

            print(personagem_atualizado.to_string())
            input("Pressione enter para sair")
            
            self.mongo.close()

            return personagem_atualizado
        else:
            self.mongo.close()
            print(f"O ID {id_personagem} não existe.")
            input("Pressione enter para sair")
            return None
    
    def excluir_personagem(self):
        self.mongo.connect()

        id_personagem = int(input("Informe o ID do personagem que deseja excluir: "))

        if not self.verifica_existencia_personagem(id_personagem):
            df_personagem = self.recupera_personagem(id_personagem)

            self.mongo.db["personagens"].delete_one({"id_personagem": id_personagem})

            personagem_excluido = Personagem(df_personagem.id_personagem.values[0], df_personagem.nome_personagem.values[0])

            self.mongo.close()

            print("Personagem Removido com Sucesso!")
            print(personagem_excluido.to_string())
            input("Pressione enter para sair")
        else:
            self.mongo.close()
            print(f"O ID {id_personagem} não existe.")
            input("Pressione enter para sair")
    
    def verifica_existencia_personagem(self, id_personagem:int=None, external:bool=False) -> bool:
        if external:
            self.mongo.connect()
            
        df_personagem = pd.DataFrame(self.mongo.db["personagens"].find({"id_personagem":id_personagem}, {"id_personagem": 1, "nome_personagem": 1, "_id": 0}))

        if external:
            self.mongo.close()
        
        return df_personagem.empty
    
    def recupera_personagem(self, id_personagem:int=None, external:bool=False) -> pd.DataFrame:
        if external:
            self.mongo.connect()
        
        df_personagem = pd.DataFrame(list(self.mongo.db["personagens"].find({"id_personagem":id_personagem}, {"id_personagem": 1, "nome_personagem": 1, "_id": 0})))

        if external:
            self.mongo.close()
        
        return df_personagem