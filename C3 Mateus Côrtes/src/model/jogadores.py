class Jogador:
    def __init__(self,
                 id_jogador:int=None,
                 nome_jogador:str=None,
                 regiao:str=None,
                 ):
        self.set_id_jogador(id_jogador)
        self.set_nome_jogador(nome_jogador)
        self.set_regiao(regiao)
    
    def set_id_jogador(self, id_jogador:int):
        self.id_jogador = id_jogador
    
    def set_nome_jogador(self, nome_jogador:str):
        self.nome_jogador = nome_jogador
    
    def set_regiao(self, regiao:str):
        self.regiao = regiao
    
    def get_id_jogador(self) -> int:
        return self.id_jogador
    
    def get_nome_jogador(self) -> str:
        return self.nome_jogador
    
    def get_regiao(self) -> str:
        return self.regiao
    
    def to_string(self) -> str:
        return f"ID_Jogador: {self.get_id_jogador()} | Nome: {self.get_nome_jogador()} | Região: {self.get_regiao()}"