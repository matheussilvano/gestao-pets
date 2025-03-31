class Dono:
    def __init__(self, nome: str, telefone: str, endereco: str, lista_de_pets: list=[]):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.lista_de_pets = lista_de_pets 

    def adicionar_pet(self, pet):
        from pet import Pet # importado dentro da função para evitar dependência circular
        
        if not isinstance(pet, Pet):
            raise ValueError("O objeto deve ser da classe Pet.")
        
        if pet in self.lista_de_pets:
            raise ValueError("Este pet já está na lista.")
        
        self.lista_de_pets.append(pet)
