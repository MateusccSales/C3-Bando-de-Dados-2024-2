from utils import config

class SplashScreen:

    def __init__(self):
        # Nome(s) do(s) criador(es)
        self.created_by = "Mateus Côrtes"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2024/2"
    
    def get_documents_count(self, collection_name):
        # Retorna o total de registros computado pela query
        df = config.query_count(collection_name=collection_name)
        return df[f"total_{collection_name}"].values[0]
    
    def get_updated_screen(self):
        return f"""
        ########################################################
        #                       SISTEMA                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - JOGADORES:             {str(self.get_documents_count(collection_name="jogadores")).rjust(5)}
        #      2 - PERSONAGENS:           {str(self.get_documents_count(collection_name="personagens")).rjust(5)}
        #      3 - JOGADORES_PERSONAGENS: {str(self.get_documents_count(collection_name="jogadores_personagens")).rjust(5)}
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """