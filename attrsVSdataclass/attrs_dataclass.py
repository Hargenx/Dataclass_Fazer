from __future__ import annotations

import inspect
from typing import Any

from attrs import validators, setters
from attrs import define, frozen, field, Factory
#https://www.attrs.org/en/stable/examples.html

@define
class Usuario:
    id: int = field(validator=validators.instance_of(int))
    nome: str = field(converter=str)
    email: str = field(repr=False)

    @email.default
    def _email_default(self):
        return f"{self.nome}@exemplo.com.br"

def slots_padroes():
    usuario = Usuario(0, "Raphael", "raphael@exemplo.com.br")
    usuario.nome = "Raphael"

def mostrar_fontes():
    print(inspect.getsource(Usuario.__init__))
    print(inspect.getsource(Usuario.__eq__))
    print(inspect.getsource(Usuario.__repr__))

def main():
    slots_padroes()
    mostrar_fontes()

if __name__ == '__main__':
    main()