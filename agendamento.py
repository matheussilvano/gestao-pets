from pet import Pet
from dono import Dono
from servico import Servico

class Agendamento:
    
    def __init__(self, pet:Pet, dono:Dono, servico:Servico, data: str, horario: str):
        self.pet = pet
        self.dono = dono
        self.servico = servico
        self.data = data
        self.horario = horario
    
    def exibir_agendamento(agendamento):
        return [
            f'Nome do pet: {agendamento.pet.nome}',
            f'Espécie do pet: {agendamento.pet.especie}',
            f'Raça do {agendamento.pet.especie}: {agendamento.pet.raca}',
            f'Idade: {agendamento.pet.idade} anos',
            f'Nome do Dono: {agendamento.dono.nome}',
            f'Telefone: {agendamento.dono.telefone}',
            f'Endereço: {agendamento.dono.endereco}',
            f'Serviço: {agendamento.servico.nome_do_servico}',
            f'Preço: {agendamento.servico.preco}',
            f'Duração estimada: {agendamento.servico.duracao_estimada}',
            f'Data e hora: {agendamento.data} | {agendamento.horario}'
        ]

dono1 = Dono('Carlos', '99999-9999', 'Rua A, 123')
pet1 = Pet('Paçoca', 'Cachorro', 'Vira-lata', '3', dono1)
servico1 = Servico('Banho e Tosa', 'R$ 100.00', '1 hora')
agendamento1 = Agendamento(pet1, dono1, servico1, '31/03/2025', '10:00')

dono1.adicionar_pet(pet1)
pet1.atualizar_dados(idade = 4)

print(Agendamento.exibir_agendamento(agendamento1))
