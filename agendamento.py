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
    
    def exibir_agendamento(self):
        return [
            f'Nome do pet: {self.pet.nome}',
            f'Espécie do pet: {self.pet.especie}',
            f'Raça do {self.pet.especie}: {self.pet.raca}',
            f'Idade: {self.pet.idade} anos',
            f'Nome do Dono: {self.dono.nome}',
            f'Telefone: {self.dono.telefone}',
            f'Endereço: {self.dono.endereco}',
            f'Serviço: {self.servico.nome_do_servico}',
            f'Preço: {self.servico.preco}',
            f'Duração estimada: {self.servico.duracao_estimada}',
            f'Data e hora: {self.data} | {self.horario}'
        ]

dono1 = Dono('Carlos', '99999-9999', 'Rua A, 123')
pet1 = Pet('Paçoca', 'Cachorro', 'Vira-lata', '3', dono1)
servico1 = Servico('Banho e Tosa', 'R$ 100.00', '1 hora')
agendamento1 = Agendamento(pet1, dono1, servico1, '31/03/2025', '10:00')

dono1.adicionar_pet(pet1)
pet1.atualizar_dados(idade = 4)

print(agendamento1.exibir_agendamento())
