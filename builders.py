class Monstro:

    def __init__(self, nome, vida, forca, destreza, constituicao, inteligencia, sabedoria, carisma, deslocamento, armadura):
        self.__nome = nome
        self.__forca = forca
        self.__destreza = destreza
        self.__constituicao = constituicao
        self.__inteligencia = inteligencia
        self.__sabedoria = sabedoria
        self.__carisma = carisma
        self.__deslocamento = deslocamento
        self.__armadura = armadura
        self.__vida = vida

    def status(self):
        print(f'O monstro está com a vida em {self.__vida}')

    def defenda(self, destreza, armadura):
        self.__destreza = destreza
        self.__armadura = armadura

    def dano_fisico(self, alvo):
        dano = self.__forca
        alvo.recebe_dano(dano)

    def dano_distancia(self, alvo):
        dano = self.__destreza
        alvo.recebe_dano(dano)

    def dano_magico(self, alvo):
        dano = self.__sabedoria
        alvo.recebe_dano(dano)

    def recebe_dano(self, dano):
        self.__vida -= dano
