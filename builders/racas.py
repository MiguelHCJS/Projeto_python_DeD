# Verificar ações específicas da raça, para inserir um método

class racas:

    def __init__(self):
        self._idade = None
        self._alinhamento = None
        self._tamanho = None
        self._deslocamento = None
        self._idioma = []


class anao(racas):

    def __init__(self):
        self._up_con = 2
        self._visao_escuro = True
        self._resiliencia = 'veneno'
        self._proficiencia = ['ferramenta de ferreiro', 'cervejeiro', 'pedreiro']
        self.conhecimento_das_pedras = ''''''
        self.treinamento_anao_em_combate = ''''''


class draconato(racas):

    def __init__(self):
        self._proficiencia = []
        self._up_for = 2
        self._up_car = 1
        self.ataque_de_sopro = ''''''
        self.resistencia_a_dano = ''''''

    @staticmethod
    def heranca_draconica():
        tipos = ({
            "1": ['Azul', 'Eletricidade', 'linha de 1,5 por 9 m (svg. Des)'],
            "2": ['Branco', 'Gelo', 'cone de 4,5 m (svg. Con)'],
            "3": ['Bronze', 'Eletricidade', 'linha de 1,5 por 9 m (svg. Des)'],
            "4": ['Cobre', 'Ácido', 'linha de 1,5 por 9 m (svg. Des)'],
            "5": ['Latão', 'Fogo', 'linha de 1,5 por 9 m (svg. Des)'],
            "6": ['Ouro', 'Fogo', 'cone de 4,5 m (svg. Des)'],
            "7": ['Prata', 'Gelo', 'cone de 4,5 m (svg. Con)'],
            "8": ['Preto', 'Ácido', 'linha de 1,5 por 9 m (svg. Des)'],
            "9": ['Verde', 'Veneno', 'cone de 4,5 m (svg. Des)'],
            "10": ['Vermelho', 'Fogo', 'cone de 4,5 m (svg. Des)']
        })
        return tipos


class elfo(racas):
    
    def __init__(self):
        self._proficiencia = ['percepcao']
        self._up_des = 2
        self.ancestral_feerico = ''''''
        self.transe = ''''''


class gnomo(racas):

    def __init__(self):
        self._up_int = 2
        self._visao_escuro = True
        self.astucia_gnomo = ''''''


class halfling(racas):

    def __init__(self):
        self._up_des = 2
        self.sortudo = ''''''
        self.corajoso = ''''''
        self.agilidade_halfling = ''''''


class tielfling(racas):

    def __init__(self):
        self._up_int = 1
        self._up_car = 2
        self._visao_escuro = True
        self._resistencia_a_dano = ['fogo']
        self.legado_infernal = ''''''


class humano(racas):

    def __init__(self):
        self._up_all = 1


class meio_elfo(racas):

    def __init__(self):
        self._up_car = 2
        self._up_any1 = 1
        self._up_any2 = 1
        self._visao_escuro = True
        self.ancestral_feerico = ''''''
        self.versatilidade_pericias = ''''''


class meio_orc(racas):

    def __init__(self):
        self._proficiencia = ['intimidação']
        self._up_for = 2
        self._up_con = 1
        self._visao_escuro = True
        self.vigor_implacavel = ''''''
        self.ataques_selvagens = ''''''