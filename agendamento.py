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
    
    def __str__(self):
        return f"""{"---" * 10 + " Agendamento de Serviço " + "---" * 10}
'Nome do pet: {self.pet.nome}',
'Espécie do pet: {self.pet.especie}',
'Raça do {self.pet.especie}: {self.pet.raca}',
'Idade: {self.pet.idade} anos',
'Nome do Dono: {self.dono.nome}',
'Telefone: {self.dono.telefone}',
'Endereço: {self.dono.endereco}',
'Serviço: {self.servico.nome_do_servico}',
'Preço: {self.servico.preco}',
'Duração estimada: {self.servico.duracao_estimada}',
'Data e hora: {self.data} | {self.horario}'
{"---" * 30}"""

dono1 = Dono('Carlos', '99999-9999', 'Rua A, 123')
pet1 = Pet('Paçoca', 'Cachorro', 'Vira-lata', '3', dono1)
pet2 = "Bola"
servico1 = Servico('Banho e Tosa', 'R$ 100.00', '1 hora')
agendamento1 = Agendamento(pet1, dono1, servico1, '31/03/2025', '10:00')

dono1.adicionar_pet(pet1)
pet1.atualizar_dados(idade = 4)

print(agendamento1)
