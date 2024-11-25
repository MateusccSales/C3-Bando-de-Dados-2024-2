from model.jogadores import Jogador
from model.personagens import Personagem

class JogadorPersonagem:
    def __init__ (self,
                  id_classificacao:int=None,
                  jogador:Jogador=None,
                  personagem:Personagem=None,
                  pontuacao:int=None
                 ):
        self.set_id_classificacao(id_classificacao)
        self.set_jogador(jogador)
        self.set_personagem(personagem)
        self.set_pontuacao(pontuacao)
    
    def set_id_classificacao(self, id_classificacao:int):
        self.id_classificacao = id_classificacao
    
    def set_jogador(self, jogador:Jogador):
        self.jogador = jogador
    
    def set_personagem(self, personagem:Personagem):
        self.personagem = personagem
    
    def set_pontuacao(self, pontuacao:int):
        self.pontuacao = pontuacao
    
    def get_id_classificacao(self) -> int:
        return self.id_classificacao
    
    def get_jogador(self) -> Jogador:
        return self.jogador
    
    def get_personagem(self) -> Personagem:
        return self.personagem
    
    def get_pontuacao(self) -> int:
        return self.pontuacao
    
    def to_string(self):
        return f"ID_Classificação: {self.get_id_classificacao()} | ID_Jogador: {self.get_jogador().get_id_jogador()} | ID_Personagem: {self.get_personagem().get_id_personagem()} | Pontuacao: {self.get_pontuacao()}"