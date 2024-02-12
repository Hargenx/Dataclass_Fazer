# Projeto de Exemplo Class vs Dataclass

Este é um projeto simples que demonstra a utilização de classes em Python, incluindo o uso de dataclasses, anotações de tipo e algumas boas práticas de programação.

## Classes

### ManualPessoa

`ManualPessoa` é uma classe que representa uma pessoa com atributos como `id`, `nome`, `telefone`, `email`, `endereco` e `texto`. Esta classe não é uma dataclass, mas utiliza anotações de tipo para maior clareza.

### Pessoa

`Pessoa` é uma dataclass que representa uma pessoa com atributos semelhantes à classe `ManualPessoa`. A diferença é que `Pessoa` utiliza a decoradora `@dataclass` do módulo `dataclasses`.

## Execução

O script principal `main.py` cria instâncias das classes `ManualPessoa` e `Pessoa` e demonstra o uso de seus métodos e propriedades. Para executar o script, basta rodar:

```bash
python main.py
```

## Contribuição
Se deseja contribuir para o projeto, por favor, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto é licenciado sob a [Licença MIT](LICENSE).