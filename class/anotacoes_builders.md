# Anotações

As classes precisam de um contrutor __init__, inicializa as informações a respeito do objeto a ser criado

Nos atributos do __init__ é importante por em sua definição self.__xxxx, onde o 'self' significa o proprio objeto,
os '__' indicam que se trata de um atributo que não deveria estar sendo acessado diretamente(private).

Declarações antes da definição de uma função:
@property - acessa uma função sem o uso dos ()
@setter - declaração para modificar um atributo que não deveria ser acessado diretamente "private"
@staticmethod - pode ser acessado sem a definição de um objeto e o uso do "self" nos ()

Na classe é importante inserir funções das quais são necessariamente da classe, para que não fuja do propósito da classe específica.
