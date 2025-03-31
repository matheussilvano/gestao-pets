from dono import Dono

class Pet:
    def __init__(self, nome: str, especie: str, raca: str, idade: int, dono: Dono):
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.idade = idade
        self.dono = dono

    def __str__(self):
        return f"""'Nome do Pet: {self.nome}'
'Especie do pet: {self.especie}'
'Raca do Pet: {self.raca}'
'Idade do pet: {self.idade}'
'Dono do pet: {self.dono.nome}'"""
    
    def atualizar_dados(self, *args, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)


if __name__ == "__main__":
    dono1 = Dono('Carlos', '99999-9999', 'Rua A, 123')
    pet1 = Pet('Paçoca', 'Cachorro', 'Vira-lata', '3', dono1)

