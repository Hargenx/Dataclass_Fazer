# Projetos de Exemplo em Python

Este repositório contém dois projetos de exemplo em Python, cada um demonstrando diferentes abordagens para a criação de classes e o uso de anotações de tipo. Abaixo estão breves resumos de cada projeto.

## Projeto 1: Classes

O projeto `ManualPessoa` apresenta uma classe chamada `ManualPessoa`, que representa uma entidade de pessoa. A classe utiliza anotações de tipo para definir atributos como `id`, `nome`, `telefone`, `email`, `endereco` e `texto`. Apesar de não ser uma dataclass, a classe ainda segue boas práticas de programação e implementa métodos especiais como `__eq__` e `__repr__` para manipulação de objetos.

E o `Pessoa`, que com uso de `@Dataclass`, com os mesmos atributos, faz uso de todos os métodos especiais sem nenhuma linha extra. 

### Principais Destaques:
- Utilização de anotações de tipo.
- Implementação manual de métodos especiais.
- Uso do Dataclass

## Projeto 2: Usuario com attrs  e dataclasses

O projeto `Usuario com attrs` utiliza o módulo `attrs` para simplificar a definição de classes em Python. A classe `Usuario` define atributos como `id`, `nome` e `email`, utilizando funcionalidades do `attrs` como validação de atributos, conversores e valores padrão. O código é mais conciso e legível devido ao uso das funcionalidades oferecidas pelo `attrs`.

### Principais Destaques:
- Utilização do módulo `attrs` para simplificar a definição de classes.
- Demonstração de validação de atributos, conversores e valores padrão.