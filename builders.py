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
        self.nomeTamanho = nomeTamanho
        self.vida = vida
