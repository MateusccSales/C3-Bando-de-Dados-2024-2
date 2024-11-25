import pandas as pd

from reports.relatorios import Relatorio

from model.jogadores import Jogador
from model.personagens import Personagem
from model.jogadores_personagens import JogadorPersonagem

from controller.controller_jogadores import Controller_Jogador
from controller.controller_personagens import Controller_Personagem

from conexion.mongo_queries import MongoQueries

class Controller_Jogador_Personagem:
    def __init__(self):
        self.ctrl_jogador = Controller_Jogador()
        self.ctrl_personagem = Controller_Personagem()
        self.mongo = MongoQueries()
        self.relatorio = Relatorio()

    def inserir_jogador_personagem(self) -> JogadorPersonagem:
        self.mongo.connect()

        self.relatorio.get_relatorio_jogadores()        
        id_jogador = int(input("Informe o ID do jogador: "))
        jogador = self.valida_jogador(id_jogador)
        if jogador == None:
            return None
        
        self.relatorio.get_relatorio_personagens()
        id_personagem = int(input("Informe o ID do personagem: "))
        personagem = self.valida_personagem(id_personagem)
        if personagem == None:
            return None
        
        if self.verifica_existencia_jogador_personagem(id_jogador=id_jogador, id_personagem=id_personagem):
            pontuacao = int(input("Insira uma pontuação (numero inteiro positivo menor ou igual a 3000)"))
            while pontuacao < 0 or pontuacao > 3000:
                pontuacao = int(input("Insira uma pontuação valida: "))
            
            id_classificacao = self.mongo.db["jogadores_personagens"].count_documents({})

            self.mongo.db["jogadores_personagens"].insert_one({"id_classificacao": id_classificacao, "id_jogador": jogador.get_id_jogador(), "id_personagem": personagem.get_id_personagem(), "pontuacao": pontuacao})

            df_jogador_personagem = self.recupera_jogador_personagem(id_jogador=id_jogador, id_personagem=id_personagem)

            novo_jogador_personagem = JogadorPersonagem(df_jogador_personagem.id_classificacao.values[0], jogador, personagem, df_jogador_personagem.pontuacao.values[0])

            print(novo_jogador_personagem.to_string())
            input("Pressione enter para sair")
            self.mongo.close()
            return novo_jogador_personagem
        else:
            input(f"A combinação de ID de jogador {id_jogador} e do ID de Personagem {id_personagem} já está cadastrada.")
            return None
    
    def atualizar_jogador_personagem(self) -> JogadorPersonagem:
        self.mongo.connect()

        self.relatorio.get_relatorio_jogadores()        
        id_jogador = int(input("Informe o ID do jogador: "))
        jogador = self.valida_jogador(id_jogador)
        if jogador == None:
            return None
        
        self.relatorio.get_relatorio_personagens()
        id_personagem = int(input("Informe o ID do personagem: "))
        personagem = self.valida_personagem(id_personagem)
        if personagem == None:
            return None
        
        df_jogador_personagem = self.recupera_jogador_personagem(id_jogador=id_jogador, id_personagem=id_personagem)
        jogador_personagem = JogadorPersonagem(df_jogador_personagem.id_classificacao.values[0], jogador, personagem, df_jogador_personagem.pontuacao.values[0])
        id_classificacao = jogador_personagem.get_id_classificacao()
        
        if not self.verifica_existencia_jogador_personagem(id_jogador=id_jogador, id_personagem=id_personagem):
            print("""Deseja mudar o ID do jogador?
                    1 - Sim
                    2 - Não""")
            opcao = int(input("Digite o numero da opção: "))
            while(opcao < 1 or opcao > 2):
                opcao = int(input("Digite uma opcao valida: "))
            
            if opcao == 1:
                self.relatorio.get_relatorio_jogadores()
                novo_id_jogador = int(input("Informe o novo ID de jogador: "))
                novo_jogador = self.valida_jogador(id_jogador=novo_id_jogador)
                if novo_jogador == None:
                    return None
                else:
                    jogador = novo_jogador
            elif opcao == 2:
                novo_id_jogador = id_jogador
                jogador = jogador

            print("""Deseja mudar o ID do personagem?
                    1 - Sim
                    2 - Não""")
            opcao = int(input("Digite o numero da opção: "))
            while(opcao < 1 or opcao > 2):
                opcao = int(input("Digite uma opcao valida: "))

            if opcao == 1:
                novo_id_personagem = int(input("Informe o novo ID de personagem: "))
                novo_personagem = self.valida_personagem(id_personagem=novo_id_personagem)
                if novo_personagem == None:
                    return None
                else:
                    personagem = novo_personagem
            elif opcao == 2:
                novo_id_personagem = id_personagem
                personagem = personagem
            
            if self.verifica_existencia_jogador_personagem(id_jogador=novo_id_jogador, id_personagem=novo_id_personagem):
                nova_pontuacao = int(input("Insira uma nova pontuação (numero inteiro positivo menor ou igual a 3000)"))
                while nova_pontuacao < 0 or nova_pontuacao > 3000:
                    nova_pontuacao = int(input("Insira uma pontuação valida: "))
                
                self.mongo.db["jogador_personagem"].update_one({"id_classificacao": id_classificacao}, {"$set": {"id_jogador": jogador.get_id_jogador(), "id_personagem": personagem.get_id_personagem(), "pontuacao": nova_pontuacao}})
                df_jogador_personagem = self.recupera_jogador_personagem(id_jogador=jogador.get_id_jogador(), id_personagem=personagem.get_id_personagem())
                jogador_personagem_atualizado = JogadorPersonagem(df_jogador_personagem.id_classificacao.values[0], jogador, personagem, df_jogador_personagem.pontuacao.values[0])
                print(jogador_personagem_atualizado.to_string())
                input("Pressione enter para sair")
                self.mongo.close()
                return jogador_personagem_atualizado
            else:
                self.mongo.close()
                print(f"A combinação de ID de jogador {novo_id_jogador} e do ID de Personagem {novo_id_personagem} já está cadastrada.")
                input("Pressione enter para sair")
                return None
    
    def excluir_jogador_personagem(self):
        self.mongo.connect()

        self.relatorio.get_relatorio_jogadores()        
        id_jogador = int(input("Informe o ID do jogador: "))
        jogador = self.valida_jogador(id_jogador)
        if jogador == None:
            return None
        
        self.relatorio.get_relatorio_personagens()
        id_personagem = int(input("Informe o ID do personagem: "))
        personagem = self.valida_personagem(id_personagem)
        if personagem == None:
            return None
        
        if not self.verifica_existencia_jogador_personagem(id_jogador=id_jogador, id_personagem=id_personagem):
            df_jogador_personagem = self.recupera_jogador_personagem(id_jogador=id_jogador, id_personagem=id_personagem)
            jogador_personagem = JogadorPersonagem(df_jogador_personagem.id_classificacao.values[0], jogador, personagem, df_jogador_personagem.pontuacao.values[0])
            id_classificacao = jogador_personagem.get_id_classificacao()

            print("""Deseja excluir esse registro?
                    1 - Sim
                    2 - Não""")
            print(jogador_personagem.to_string())
            opcao_excluir = int(input("Digite o numero da opção: "))
            while(opcao_excluir < 1 or opcao_excluir > 2):
                opcao_excluir = int(input("Digite uma opcao valida: "))
            
            if opcao_excluir == 1:
                self.mongo.db["jogadores_personagens"].delete_one({"id_classificacao": id_classificacao})
                self.mongo.close()
                input("Registro Removido com Sucesso!")
                print(jogador_personagem.to_string())
                input("Pressione enter para sair")
        else:
            self.mongo.close()
            print("O registro informado não existe")
            input("Pressione enter para sair")

    def verifica_existencia_jogador_personagem(self, id_jogador:int=None, id_personagem:int=None, external:bool=False) -> bool:
        df_jogador_personagem = self.recupera_jogador_personagem(id_jogador=id_jogador, id_personagem=id_personagem, external=external)
        return df_jogador_personagem.empty
    
    def recupera_jogador_personagem(self, id_jogador:int=None, id_personagem:int=None, external:bool=False) -> pd.DataFrame:
        if external:
            self.mongo.connect()
        
        df_jogador_personagem = pd.DataFrame(list(self.mongo.db["jogadores_personagens"].find({"id_jogador": id_jogador, "id_personagem": id_personagem}, {"id_classificacao": 1, "id_jogador": 1, "id_personagem": 1, "pontuacao": 1, "_id": 0})))

        if external:
            self.mongo.close()
        
        return df_jogador_personagem
    
    def valida_jogador(self, id_jogador:int=None) -> Jogador:
        if self.ctrl_jogador.verifica_existencia_jogador(id_jogador=id_jogador, external=True):
            print(f"O ID {id_jogador} não existe na base.")
            return None
        else:
            df_jogador = self.ctrl_jogador.recupera_jogador(id_jogador=id_jogador, exteral=True)
            jogador = Jogador(df_jogador.id_jogador.values[0], df_jogador.nome_jogador.values[0], df_jogador.regiao.values[0])
            return jogador

    def valida_personagem(self, id_personagem) -> Personagem:
        if self.ctrl_personagem.verifica_existencia_personagem(id_personagem=id_personagem, external=True):
            print(f"O ID {id_personagem} não existe na base.")
            return None
        else:
            df_personagem = self.ctrl_personagem.recupera_personagem(id_personagem=id_personagem, external=True)
            personagem = Personagem(df_personagem.id_personagem.values[0], df_personagem.nome_personagem.values[0])
            return personagem