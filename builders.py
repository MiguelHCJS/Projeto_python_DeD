class Monstro:

    def __init__(self, nome, forca, destreza, constituicao, inteligencia, sabedoria, carisma, deslocamento, armadura):
        self.nome = nome
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.inteligencia = inteligencia
        self.sabedoria = sabedoria
        self.carisma = carisma
        self.deslocamento = deslocamento
        self.armadura = armadura

class tamanhoMonstro:

    def __init__(self, nomeTamanho, vida):
        self.nomeTamanho = nomeTamanho
        self.vida = vida
