class Servico:
    def __init__(self, nome_do_servico, preco, duracao_estimada):
        self.nome_do_servico = nome_do_servico
        self._preco = preco
        self.duracao_estimada = duracao_estimada
    
    def __str__(self):
        return f"""'Serviço: {self.nome_do_servico}',
'Preço: {self.preco}',
'Duração estimada: {self.duracao_estimada}'"""
    
    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, preco):
        if preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        self._preco = preco
