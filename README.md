# Agendamento de Serviços para Pets

Este é um sistema para agendamento de serviços para pets, onde é possível registrar informações sobre o dono, o pet e o serviço, além de realizar a visualização dos agendamentos.

## Estrutura

### Classes:

1. **Pet**: Representa o pet que será atendido.
    - Atributos: 
        - `nome`: Nome do pet.
        - `especie`: Espécie do pet.
        - `raca`: Raça do pet.
        - `idade`: Idade do pet.
        - `dono`: Objeto da classe Dono (responsável pelo pet).
    - Métodos:
        - `atualizar_dados()`: Atualiza informações do pet, como idade.

2. **Dono**: Representa o dono do pet.
    - Atributos:
        - `nome`: Nome do dono.
        - `telefone`: Telefone do dono.
        - `endereco`: Endereço do dono.
    - Métodos:
        - `adicionar_pet()`: Adiciona um pet ao dono.

3. **Servico**: Representa um serviço que pode ser agendado para o pet.
    - Atributos:
        - `nome_do_servico`: Nome do serviço (ex: Banho e Tosa).
        - `preco`: Preço do serviço.
        - `duracao_estimada`: Duração estimada do serviço.

4. **Agendamento**: Representa um agendamento de serviço para o pet.
    - Atributos:
        - `pet`: Objeto da classe Pet.
        - `dono`: Objeto da classe Dono.
        - `servico`: Objeto da classe Servico.
        - `data`: Data do agendamento.
        - `horario`: Horário do agendamento.
    - Métodos:
        - `exibir_agendamento()`: Exibe as informações do agendamento.


## Contribuindo

Sinta-se à vontade para contribuir com melhorias ou correções no código. Para isso, basta criar um fork deste repositório, fazer suas alterações e enviar um pull request.