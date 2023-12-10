import random

class AspiradorRacional:
    def __init__(self):
        self.nivel_energia = 100
        self.sujeira_na_bolsa = 0
        self.posicao_atual = [0, 0] 
        self.objetivo_alcancado = False
        self.direcoes = {'Norte': (-1, 0), 'Sul': (1, 0), 'Leste': (0, 1), 'Oeste': (0, -1)}
        self.ambiente = [['A', 'B', 'C', 'D', 'E', 'F'],
                        ['G', 'H', 'I', 'J', 'K', 'L'],
                        ['M', 'N', 'O', 'P', 'Q', 'R'],
                        ['S', 'T', 'U', 'V', 'W', 'X'],
                        ['Y', 'Z', 'AA', 'AB', 'AC', 'AD'],
                        ['AE', 'AF', 'AG', 'AH', 'AI', 'AJ']]

    def aspirar_sujeira(self):
        linha, coluna = self.posicao_atual
        local_atual = self.ambiente[linha][coluna]
        self.ambiente[linha][coluna] = ' '

        self.sujeira_na_bolsa += 1
        self.nivel_energia -= 1
        print(f"Aspirou sujeira em {local_atual}")

    def mover(self, direcao):
        linha, coluna = self.posicao_atual
        deslocamento = self.direcoes[direcao]
        nova_linha = linha + deslocamento[0]
        nova_coluna = coluna + deslocamento[1]

        if self.validar_posicao(nova_linha, nova_coluna):
            self.posicao_atual = [nova_linha, nova_coluna]
            self.nivel_energia -= 1

    def validar_posicao(self, linha, coluna):
        return 0 <= linha < 6 and 0 <= coluna < 6

    def voltar_para_casa(self):
        while self.posicao_atual != [0, 0]:
            self.mover(self.determinar_direcao_de_volta())

    def determinar_direcao_de_volta(self):
        linha, coluna = self.posicao_atual
        if linha > 0:
            return 'Norte'
        elif coluna > 0:
            return 'Oeste'
        else:
            return 'Sul'

    def verificar_objetivo(self):
        if self.sujeira_na_bolsa >= 10:
            self.sujeira_na_bolsa = 0
            self.objetivo_alcancado = True

    def limpar_quarto(self):
        while not self.objetivo_alcancado:
            if self.nivel_energia <= 0:
                print("Sem energia suficiente para continuar.")
                break

            self.aspirar_sujeira()
            self.verificar_objetivo()

            if self.objetivo_alcancado:
                print("\nBolsa cheia.")
                self.voltar_para_casa()
                self.sujeira_na_bolsa = 0 
                print("\nBolsa esvaziada, continuando a limpeza.")

            if not self.objetivo_alcancado:
                self.mover(self.determinar_proxima_acao())

        print("\nQuarto limpo!")

    def determinar_proxima_acao(self):
        direcoes_possiveis = list(self.direcoes.keys())
        return random.choice(direcoes_possiveis)


def interagir_com_aspirador(aspirador):
    while True:
        print("Comandos disponíveis:")
        print("1 - Mover [direcao]")
        print("2 - Limpar")
        print("3 - Sair")

        escolha = input("Escolha um comando (1, 2, 3): ").lower()

        if escolha == "1":
            direcao = input("Digite a direcao (Norte, Sul, Leste, Oeste): ").capitalize()
            aspirador.mover(direcao)
        elif escolha == "2":
            aspirador.limpar_quarto()
            break
        elif escolha == "3":
            break
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    aspirador = AspiradorRacional()
    interagir_com_aspirador(aspirador)
