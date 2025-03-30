class Servico:
    def __init__(self, nome_do_servico, preco, duracao_estimada):
        self.nome_do_servico = nome_do_servico
        self.preco = preco
        self.duracao_estimada = duracao_estimada
    
    def exibir_detalhes(servico):
        return [
            f'Serviço: {servico.nome_do_servico}',
            f'Preço: {servico.preco}',
            f'Duração estimada: {servico.duracao_estimada}'
        ]
    
    def atualizar_preco(self, preco):
        self.preco = preco