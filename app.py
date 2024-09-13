from abc import ABCMeta, abstractmethod

class IPessoa(metaclass=ABCMeta):

    @abstractmethod
    def pessoa_metodo():
        ...
        # Metodo de interface
    
class Pessoa(IPessoa):
    def pessoa_metodo(self):
        print('Eu sou a pessoa!')

class ProxyPessoa(IPessoa):
    def __init__(self):
        self.pessoa = Pessoa()

    def pessoa_metodo(self):
        print('Eu sou a funcionalidade do Proxy')
        self.pessoa.pessoa_metodo()

p1 = Pessoa()
p1.pessoa_metodo()

p2 = ProxyPessoa()
p2.pessoa_metodo()