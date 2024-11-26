class Personagem:
    def __init__ (self, 
                  id_personagem:int=None,
                  nome_personagem:str=None
                 ):
        self.set_id_personagem(id_personagem)
        self.set_nome_personagem(nome_personagem)
    
    def set_id_personagem(self, id_personagem:int):
        self.id_personagem = id_personagem
    
    def set_nome_personagem(self, nome_personagem:str):
        self.nome_personagem = nome_personagem
    
    def get_id_personagem(self) -> int:
        return self.id_personagem
    
    def get_nome_personagem(self) -> str:
        return self.nome_personagem
    
    def to_string(self) -> str:
        return f"ID_Personagem: {self.get_id_personagem()} | Nome: {self.get_nome_personagem()}"