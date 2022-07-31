class Monstro:

    def __init__(self, nome, forca, destreza, constituicao, inteligencia, sabedoria, carisma, deslocamento, armadura):
        self.__nome = nome
        self.__forca = forca
        self.__destreza = destreza
        self.__constituicao = constituicao
        self.__inteligencia = inteligencia
        self.__sabedoria = sabedoria
        self.__carisma = carisma
        self.__deslocamento = deslocamento
        self.__armadura = armadura

    def atacar_fisico(self, ataque, elemento, forca):
        self.ataque = ataque
        self.elemento = elemento
        self.carisma = forca

    def atacar_distancia(self, ataque, elemento, destreza):
        self.ataque = ataque
        self.elemento = elemento
        self.carisma = destreza

    def atacar_magico(self, ataque, elemento, sabedoria):
        self.ataque = ataque
        self.elemento = elemento
        self.carisma = sabedoria

    def defender(self, destreza, armadura):
        self.destreza = destreza
        self.armadura = armadura


class tamanhoMonstro:

    def __init__(self, nomeTamanho, vida):
        self.__nomeTamanho = nomeTamanho
        self.__vida = vida
