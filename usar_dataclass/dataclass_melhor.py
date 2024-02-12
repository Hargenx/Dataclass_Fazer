# from typing import Optional, List

import dataclasses
import inspect

class ManualPessoa:
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: str, texto: str):
        self.id: int = id
        self.nome: str = nome
        self.telefone: str = telefone
        self.email: str = email
        self.endereco: str = endereco
        self.texto: str = texto
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, nome={self.nome}, telefone={self.telefone}, " \
               f"email={self.email}, endereco={self.endereco}, texto={self.texto})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return (self.id, self.nome, self.telefone, self.email, self.endereco, self.texto) == (
                other.id, other.nome, other.telefone, other.email, other.endereco, other.texto
            )
        else:
            return NotImplemented

    def __ne__(self, other: object) -> bool:
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        else:
            return not result

    def __hash__(self) -> int:
        return hash((self.__class__, self.id, self.nome, self.telefone, self.email, self.endereco, self.texto))

    def __lt__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return (self.id, self.nome, self.telefone, self.email, self.endereco, self.texto) < (
                other.id, other.nome, other.telefone, other.email, other.endereco, other.texto
            )
        else:
            return NotImplemented

    def __le__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return (self.id, self.nome, self.telefone, self.email, self.endereco, self.texto) <= (
                other.id, other.nome, other.telefone, other.email, other.endereco, other.texto
            )
        else:
            return NotImplemented

    def __gt__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return (self.id, self.nome, self.telefone, self.email, self.endereco, self.texto) > (
                other.id, other.nome, other.telefone, other.email, other.endereco, other.texto
            )
        else:
            return NotImplemented

    def __ge__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return (self.id, self.nome, self.telefone, self.email, self.endereco, self.texto) >= (
                other.id, other.nome, other.telefone, other.email, other.endereco, other.texto
            )
        else:
            return NotImplemented


@dataclasses.dataclass(frozen=True, order=True)
class Pessoa:
    id: int
    nome: str
    telefone: str
    email: str
    endereco: str


def principal() -> None:
    pessoa_manual = ManualPessoa(1, "Raphael", "44444444", "rrrrr", "bbbbbbb", "texto")
    print(pessoa_manual)
    print(inspect.getmembers(ManualPessoa), inspect.isfunction)

    pessoa = Pessoa(1, "Raphael", "2222222", "eeeee", "aaaaaaa")
    # pessoa.id = 2  # Não vai, imutável!
    print(pessoa)
    print(dataclasses.astuple(pessoa))
    print(dataclasses.asdict(pessoa))
    copia = dataclasses.replace(pessoa, id=3)
    print(copia)

    print(inspect.getmembers(Pessoa, inspect.isfunction))


if __name__ == '__main__':
    principal()
