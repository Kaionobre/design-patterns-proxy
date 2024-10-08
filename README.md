# Padrão Proxy em Python

O padrão Proxy é um dos **padrões de design estrutural** que fornece um intermediário para controlar o acesso a um objeto. Ele pode ser utilizado para adicionar funcionalidades antes ou depois de uma chamada a um objeto real, como controle de acesso, cache ou logs, sem modificar o objeto em si.

Neste exemplo, vou explicar como o padrão Proxy funciona em Python usando o código a seguir:

## Código Explicado

```python
from abc import ABCMeta, abstractmethod

class IPessoa(metaclass=ABCMeta):
    @abstractmethod
    def pessoa_metodo():
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
