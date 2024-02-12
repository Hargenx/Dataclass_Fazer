# Projeto de Exemplo com attrs

Este é um projeto de exemplo que utiliza o módulo `attrs` para definir e trabalhar com classes em Python. O projeto inclui a criação da classe `Usuario` e demonstra algumas funcionalidades do `attrs`, como validação de atributos, conversores e atributos padrão.

## Classe `Usuario`

A classe `Usuario` representa um usuário com os seguintes atributos:

- `id`: um inteiro validado para garantir que seja uma instância de `int`.
- `nome`: uma string com um conversor para garantir que seja uma string.
- `email`: uma string que não é exibida na representação (`repr`) da classe.

O email é gerado automaticamente com um valor padrão utilizando o nome do usuário.

## Funcionalidades Demonstradas

O projeto demonstra as seguintes funcionalidades do `attrs`:

- A validação do tipo de atributo usando `validator`.
- A conversão de atributos usando `converter`.
- A definição de um valor padrão para um atributo usando `default`.

## Execução

Para executar o script principal `main.py`, utilize o seguinte comando:

```bash
python main.py
```

## Contribuição
Se deseja contribuir para o projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.


## Licença
Este projeto é licenciado sob a [Licença MIT](LICENSE).