class Monstro:

    def __init__(self, nome, vida, forca, destreza, constituicao, inteligencia, sabedoria, carisma, deslocamento, armadura, tipo_monstro):
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
        self.__tipo_monstro = tipo_monstro

    def __str__(self):
        pass

    @property  # Acesso direto com o "."
    def hp(self):
        print(f'O {self.__nome} está com a vida em {self.__vida}')

    @hp.setter  # Parametro é passado atribuindo-o "="
    def hp(self, valor):
        self.__vida = valor

    @staticmethod
    def tipo_monstro():
        tipos = {
            "1": "Aberração",
            "2": "Besta",
            "3": "Celestial",
            "4": "Constructo",
            "5": "Corruptor",
            "6": "Dragão",
            "7": "Elemental",
            "8": "Fada",
            "9": "Gigante",
            "10": "Humanoide",
            "11": "Limo",
            "12": "Monstruosidade",
            "13": "Morto-vivo",
            "14": "Planta"
        }
        return tipos

    def defende(self, destreza, armadura):
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
