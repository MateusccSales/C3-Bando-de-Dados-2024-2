from utils import config
from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorio

from controller.controller_jogadores import Controller_Jogador
from controller.controller_personagens import Controller_Personagem
from controller.controller_jogadores_personagens import Controller_Jogador_Personagem

tela_inicial = SplashScreen()
relatorio = Relatorio()
ctrl_jogador = Controller_Jogador()
ctrl_personagem = Controller_Personagem()
ctrl_jogador_personagem = Controller_Jogador_Personagem()

def reports(opcao_relatorio:int=0):
    if opcao_relatorio == 1:
        relatorio.get_relatorio_jogadores()
    elif opcao_relatorio == 2:
        relatorio.get_relatorio_personagens()
    elif opcao_relatorio == 3:
        relatorio.get_relatorio_jogadores_personagens()
    elif opcao_relatorio == 4:
        relatorio.get_relatorio_classificacao_mundial()
    elif opcao_relatorio == 5:
        relatorio.get_relatorio_classificacao_america_sul_central()
    elif opcao_relatorio == 6:
        relatorio.get_relatorio_classificacao_america_norte()
    elif opcao_relatorio == 7:
        relatorio.get_relatorio_classificacao_europa()
    elif opcao_relatorio == 8:
        relatorio.get_relatorio_classificacao_oriente_medio()
    elif opcao_relatorio == 9:
        relatorio.get_relatorio_classificacao_asia()

def inserir(opcao_inserir:int=0):
    if opcao_inserir == 1:
        ctrl_jogador.inserir_jogador()
    elif opcao_inserir == 2:
        ctrl_personagem.inserir_personagem()
    elif opcao_inserir == 3:
        ctrl_jogador_personagem.inserir_jogador_personagem()

def atualizar(opcao_atualizar:int=0):
    if opcao_atualizar == 1:
        relatorio.get_relatorio_jogadores()
        ctrl_jogador.atualizar_jogador()
    elif opcao_atualizar == 2:
        relatorio.get_relatorio_personagens()
        ctrl_personagem.atualizar_personagem()
    elif opcao_atualizar == 3:
        relatorio.get_relatorio_jogadores_personagens()
        ctrl_jogador_personagem.atualizar_jogador_personagem()

def excluir(opcao_excluir:int=0):
    if opcao_excluir == 1:
        relatorio.get_relatorio_jogadores()
        ctrl_jogador.excluir_jogador()
    elif opcao_excluir == 2:
        relatorio.get_relatorio_personagens()
        ctrl_personagem.excluir_personagem()
    elif opcao_excluir == 3:
        relatorio.get_relatorio_jogadores_personagens()
        ctrl_jogador_personagem.excluir_jogador_personagem()

def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console()

    while True:
        print(config.MENU_PRINCIPAL)
        opcao = int(input("Escolha uma opção [1-5]: "))
        config.clear_console(1)

        if opcao == 1: # Relatórios
            
            print(config.MENU_RELATORIOS)
            opcao_relatorio = int(input("Escolha uma opção [0-9]: "))
            config.clear_console(1)

            reports(opcao_relatorio)

            config.clear_console(1)
        
        elif opcao == 2: # Inserir Novos Registros
            
            print(config.MENU_ENTIDADES)
            opcao_inserir = int(input("Escolha uma opção [1-3]: "))
            config.clear_console(1)

            inserir(opcao_inserir=opcao_inserir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()
        
        elif opcao == 3: # Atualizar Registros

            print(config.MENU_ENTIDADES)
            opcao_atualizar = int(input("Escolha uma opção [1-3]: "))
            config.clear_console(1)

            atualizar(opcao_atualizar=opcao_atualizar)

            config.clear_console()
        
        elif opcao == 4: # Excluir registros

            print(config.MENU_ENTIDADES)
            opcao_excluir = int(input("Escolha uma opção [1-3]: "))
            config.clear_console(1)

            excluir(opcao_excluir=opcao_excluir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()
        
        elif opcao == 5:

            print(tela_inicial.get_updated_screen())
            config.clear_console()
            print("Obrigada por utilizar o sistema.")
            exit(0)

        else:
            print("Opção incorreta.")
            exit(1)

if __name__ == "__main__":
    run()