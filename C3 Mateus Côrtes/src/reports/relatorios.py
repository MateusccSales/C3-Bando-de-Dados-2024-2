from conexion.mongo_queries import MongoQueries
import pandas as pd
from pymongo import ASCENDING, DESCENDING

class Relatorio:
    def __init__(self):
        pass

    def get_relatorio_jogadores(self):
        # Cria uma nova conexão com o banco
        mongo = MongoQueries()
        mongo.connect()
        # Recupera os dados transformando em um DataFrame
        query_result = mongo.db["jogadores"].find({}, 
                                                  {"id_jogador": 1, 
                                                   "nome_jogador": 1, 
                                                    "regiao": 1,
                                                    "_id": 0
                                                }).sort("id_jogador", ASCENDING)
        df_jogador = pd.DataFrame(list(query_result))
        # Fecha a conexão com o mongo
        mongo.close()
        # Exibe o resultado
        print(df_jogador)
        input("Pressione Enter para Sair do Relatório de Jogadores")
    
    def get_relatorio_personagens(self):
        mongo = MongoQueries()
        mongo.connect()

        query_result = mongo.db["personagens"].find({},
                                                    {"id_personagem": 1,
                                                     "nome_personagem": 1,
                                                     "_id": 0
                                                     }).sort("id_personagem", ASCENDING)
        df_personagem = pd.DataFrame(list(query_result))
        mongo.close()
        print(df_personagem)
        input("Pressione Enter para Sair do Relatório de Personagens")

    def get_relatorio_jogadores_personagens(self):
        mongo = MongoQueries()
        mongo.connect()

        query_result = mongo.db["jogadores_personagens"].find({},
                                                              {"id_classificacao": 1,
                                                               "id_jogador": 1,
                                                               "id_personagem": 1,
                                                               "pontuacao": 1,
                                                               "_id": 0
                                                               }).sort("id_classificacao", ASCENDING)
        df_jogador_personagem = pd.DataFrame(list(query_result))
        mongo.close()
        print(df_jogador_personagem)
        input("Pressione Enter para Sair do Relatório Jogadores_Personagens")

    def get_relatorio_classificacao_mundial(self):
        mongo = MongoQueries()
        mongo.connect()

        query_result = mongo.db["jogadores_personagens"].aggregate([
                                                                    {
                                                                        '$lookup': {
                                                                            'from': 'jogadores', 
                                                                            'localField': 'id_jogador', 
                                                                            'foreignField': 'id_jogador', 
                                                                            'as': 'jogador'
                                                                        }
                                                                    }, {
                                                                        '$match': {
                                                                            'jogador': {
                                                                                '$ne': []
                                                                            }
                                                                        }
                                                                    }, {
                                                                        '$unwind': {
                                                                            'path': '$jogador'
                                                                        }
                                                                    }, {
                                                                        '$project': {
                                                                            '_id': 0, 
                                                                            'jogador': '$jogador.nome_jogador', 
                                                                            'regiao': '$jogador.regiao', 
                                                                            'pontuacao': 1, 
                                                                            'id_personagem': 1
                                                                        }
                                                                    }, {
                                                                        '$lookup': {
                                                                            'from': 'personagens', 
                                                                            'localField': 'id_personagem', 
                                                                            'foreignField': 'id_personagem', 
                                                                            'as': 'personagem'
                                                                        }
                                                                    }, {
                                                                        '$match': {
                                                                            'personagem': {
                                                                                '$ne': []
                                                                            }
                                                                        }
                                                                    }, {
                                                                        '$unwind': {
                                                                            'path': '$personagem'
                                                                        }
                                                                    }, {
                                                                        '$project': {
                                                                            '_id': 0, 
                                                                            'jogador': 1, 
                                                                            'regiao': 1, 
                                                                            'personagem': '$personagem.nome_personagem', 
                                                                            'pontuacao': '$pontuacao'
                                                                        }
                                                                    }, {
                                                                        '$sort': {
                                                                            'pontuacao': -1
                                                                        }
                                                                    }
                                                                ])
        df_classificacao = pd.DataFrame(list(query_result))
        mongo.close()
        print(df_classificacao[["jogador", "regiao", "personagem", "pontuacao"]])
        input("Pressione Enter para Sair do Relatório de Classificação Mundial")
    
    def get_relatorio_classificacao_america_sul_central(self):
        mongo = MongoQueries()
        mongo.connect()

        query_result = mongo.db["jogadores_personagens"].aggregate([
                                                                    {
                                                                        '$lookup': {
                                                                            'from': 'jogadores', 
                                                                            'localField': 'id_jogador', 
                                                                            'foreignField': 'id_jogador', 
                                                                            'as': 'jogador'
                                                                        }
                                                                    }, {
                                                                        '$match': {
                                                                            'jogador': {
                                                                                '$ne': []
                                                                            }
                                                                        }
                                                                    }, {
                                                                        '$unwind': {
                                                                            'path': '$jogador'
                                                                        }
                                                                    }, {
                                                                        '$project': {
                                                                            '_id': 0, 
                                                                            'jogador': '$jogador.nome_jogador', 
                                                                            'regiao': '$jogador.regiao', 
                                                                            'pontuacao': 1, 
                                                                            'id_personagem': 1
                                                                        }
                                                                    }, {
                                                                        '$lookup': {
                                                                            'from': 'personagens', 
                                                                            'localField': 'id_personagem', 
                                                                            'foreignField': 'id_personagem', 
                                                                            'as': 'personagem'
                                                                        }
                                                                    }, {
                                                                        '$match': {
                                                                            'personagem': {
                                                                                '$ne': []
                                                                            }
                                                                        }
                                                                    }, {
                                                                        '$unwind': {
                                                                            'path': '$personagem'
                                                                        }
                                                                    }, {
                                                                        '$project': {
                                                                            '_id': 0, 
                                                                            'jogador': 1, 
                                                                            'regiao': 1, 
                                                                            'personagem': '$personagem.nome_personagem', 
                                                                            'pontuacao': '$pontuacao'
                                                                        }
                                                                    }, {
                                                                        '$sort': {
                                                                            'pontuacao': -1
                                                                        }
                                                                    }, {
                                                                        '$match': {
                                                                            '$or': [
                                                                                {
                                                                                    'regiao': 'america do sul'
                                                                                }, {
                                                                                    'regiao': 'america central'
                                                                                }
                                                                            ]
                                                                        }
                                                                    }
                                                                ])
        df_classificacao = pd.DataFrame(list(query_result))
        mongo.close()
        print(df_classificacao[["jogador", "regiao", "personagem", "pontuacao"]])
        input("Pressione Enter para Sair do Relatório de Classificação America do Sul e Central")

    def get_relatorio_classificacao_america_norte(self):
        mongo = MongoQueries()
        mongo.connect()

        query_result = mongo.db["jogadores_personagens"].aggregate([
                                                                    {
                                                                        '$lookup': {
                                                                            'from': 'jogadores', 
                                                                            'localField': 'id_jogador', 
                                                                            'foreignField': 'id_jogador', 
                                                                            'as': 'jogador'
                                                                        }
                                                                    }, {
                                                                        '$match': {
                                                                            'jogador': {
                                                                                '$ne': []
                                                                            }
                                                                        }
                                                                    }, {
                                                                        '$unwind': {
                                                                            'path': '$jogador'
                                                                        }
                                                                    }, {
                                                                        '$project': {
                                                                            '_id': 0, 
                                                                            'jogador': '$jogador.nome_jogador', 
                                                                            'regiao': '$jogador.regiao', 
                                                                            'pontuacao': 1, 
                                                                            'id_personagem': 1
                                                                        }
                                                                    }, {
                                                                        '$lookup': {
                                                                            'from': 'personagens', 
                                                                            'localField': 'id_personagem', 
                                                                            'foreignField': 'id_personagem', 
                                                                            'as': 'personagem'
                                                                        }
                                                                    }, {
                                                                        '$match': {
                                                                            'personagem': {
                                                                                '$ne': []
                                                                            }
                                                                        }
                                                                    }, {
                                                                        '$unwind': {
                                                                            'path': '$personagem'
                                                                        }
                                                                    }, {
                                                                        '$project': {
                                                                            '_id': 0, 
                                                                            'jogador': 1, 
                                                                            'regiao': 1, 
                                                                            'personagem': '$personagem.nome_personagem', 
                                                                            'pontuacao': '$pontuacao'
                                                                        }
                                                                    }, {
                                                                        '$sort': {
                                                                            'pontuacao': -1
                                                                        }
                                                                    }, {
                                                                        '$match': {
                                                                            'regiao': 'america do norte'
                                                                        }
                                                                    }
                                                                ])
        df_classificacao = pd.DataFrame(list(query_result))
        mongo.close()
        print(df_classificacao[["jogador", "regiao", "personagem", "pontuacao"]])
        input("Pressione Enter para Sair do Relatório de Classificação America do Norte")
    
    def get_relatorio_classificacao_europa(self):
        mongo = MongoQueries()
        mongo.connect()

        query_result = mongo.db["jogadores_personagens"].aggregate([
                                                                    {
                                                                        '$lookup': {
                                                                            'from': 'jogadores', 
                                                                            'localField': 'id_jogador', 
                                                                            'foreignField': 'id_jogador', 
                                                                            'as': 'jogador'
                                                                        }
                                                                    }, {
                                                                        '$match': {
                                                                            'jogador': {
                                                                                '$ne': []
                                                                            }
                                                                        }
                                                                    }, {
                                                                        '$unwind': {
                                                                            'path': '$jogador'
                                                                        }
                                                                    }, {
                                                                        '$project': {
                                                                            '_id': 0, 
                                                                            'jogador': '$jogador.nome_jogador', 
                                                                            'regiao': '$jogador.regiao', 
                                                                            'pontuacao': 1, 
                                                                            'id_personagem': 1
                                                                        }
                                                                    }, {
                                                                        '$lookup': {
                                                                            'from': 'personagens', 
                                                                            'localField': 'id_personagem', 
                                                                            'foreignField': 'id_personagem', 
                                                                            'as': 'personagem'
                                                                        }
                                                                    }, {
                                                                        '$match': {
                                                                            'personagem': {
                                                                                '$ne': []
                                                                            }
                                                                        }
                                                                    }, {
                                                                        '$unwind': {
                                                                            'path': '$personagem'
                                                                        }
                                                                    }, {
                                                                        '$project': {
                                                                            '_id': 0, 
                                                                            'jogador': 1, 
                                                                            'regiao': 1, 
                                                                            'personagem': '$personagem.nome_personagem', 
                                                                            'pontuacao': '$pontuacao'
                                                                        }
                                                                    }, {
                                                                        '$sort': {
                                                                            'pontuacao': -1
                                                                        }
                                                                    }, {
                                                                        '$match': {
                                                                            'regiao': 'europa'
                                                                        }
                                                                    }
                                                                ])
        df_classificacao = pd.DataFrame(list(query_result))
        mongo.close()
        print(df_classificacao[["jogador", "regiao", "personagem", "pontuacao"]])
        input("Pressione Enter para Sair do Relatório de Classificação Europa")
    
    def get_relatorio_classificacao_asia(self):
        mongo = MongoQueries()
        mongo.connect()

        query_result = mongo.db["jogadores_personagens"].aggregate([
                                                                    {
                                                                        '$lookup': {
                                                                            'from': 'jogadores', 
                                                                            'localField': 'id_jogador', 
                                                                            'foreignField': 'id_jogador', 
                                                                            'as': 'jogador'
                                                                        }
                                                                    }, {
                                                                        '$match': {
                                                                            'jogador': {
                                                                                '$ne': []
                                                                            }
                                                                        }
                                                                    }, {
                                                                        '$unwind': {
                                                                            'path': '$jogador'
                                                                        }
                                                                    }, {
                                                                        '$project': {
                                                                            '_id': 0, 
                                                                            'jogador': '$jogador.nome_jogador', 
                                                                            'regiao': '$jogador.regiao', 
                                                                            'pontuacao': 1, 
                                                                            'id_personagem': 1
                                                                        }
                                                                    }, {
                                                                        '$lookup': {
                                                                            'from': 'personagens', 
                                                                            'localField': 'id_personagem', 
                                                                            'foreignField': 'id_personagem', 
                                                                            'as': 'personagem'
                                                                        }
                                                                    }, {
                                                                        '$match': {
                                                                            'personagem': {
                                                                                '$ne': []
                                                                            }
                                                                        }
                                                                    }, {
                                                                        '$unwind': {
                                                                            'path': '$personagem'
                                                                        }
                                                                    }, {
                                                                        '$project': {
                                                                            '_id': 0, 
                                                                            'jogador': 1, 
                                                                            'regiao': 1, 
                                                                            'personagem': '$personagem.nome_personagem', 
                                                                            'pontuacao': '$pontuacao'
                                                                        }
                                                                    }, {
                                                                        '$sort': {
                                                                            'pontuacao': -1
                                                                        }
                                                                    }, {
                                                                        '$match': {
                                                                            'regiao': 'asia'
                                                                        }
                                                                    }
                                                                ])
        df_classificacao = pd.DataFrame(list(query_result))
        mongo.close()
        print(df_classificacao[["jogador", "regiao", "personagem", "pontuacao"]])
        input("Pressione Enter para Sair do Relatório de Classificação Asia")

    def get_relatorio_classificacao_oriente_medio(self):
        mongo = MongoQueries()
        mongo.connect()

        query_result = mongo.db["jogadores_personagens"].aggregate([
                                                                    {
                                                                        '$lookup': {
                                                                            'from': 'jogadores', 
                                                                            'localField': 'id_jogador', 
                                                                            'foreignField': 'id_jogador', 
                                                                            'as': 'jogador'
                                                                        }
                                                                    }, {
                                                                        '$match': {
                                                                            'jogador': {
                                                                                '$ne': []
                                                                            }
                                                                        }
                                                                    }, {
                                                                        '$unwind': {
                                                                            'path': '$jogador'
                                                                        }
                                                                    }, {
                                                                        '$project': {
                                                                            '_id': 0, 
                                                                            'jogador': '$jogador.nome_jogador', 
                                                                            'regiao': '$jogador.regiao', 
                                                                            'pontuacao': 1, 
                                                                            'id_personagem': 1
                                                                        }
                                                                    }, {
                                                                        '$lookup': {
                                                                            'from': 'personagens', 
                                                                            'localField': 'id_personagem', 
                                                                            'foreignField': 'id_personagem', 
                                                                            'as': 'personagem'
                                                                        }
                                                                    }, {
                                                                        '$match': {
                                                                            'personagem': {
                                                                                '$ne': []
                                                                            }
                                                                        }
                                                                    }, {
                                                                        '$unwind': {
                                                                            'path': '$personagem'
                                                                        }
                                                                    }, {
                                                                        '$project': {
                                                                            '_id': 0, 
                                                                            'jogador': 1, 
                                                                            'regiao': 1, 
                                                                            'personagem': '$personagem.nome_personagem', 
                                                                            'pontuacao': '$pontuacao'
                                                                        }
                                                                    }, {
                                                                        '$sort': {
                                                                            'pontuacao': -1
                                                                        }
                                                                    }, {
                                                                        '$match': {
                                                                            'regiao': 'oriente medio'
                                                                        }
                                                                    }
                                                                ])
        df_classificacao = pd.DataFrame(list(query_result))
        mongo.close()
        print(df_classificacao[["jogador", "regiao", "personagem", "pontuacao"]])
        input("Pressione Enter para Sair do Relatório de Classificação Oriente Médio")