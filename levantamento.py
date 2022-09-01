# espoçando a ideia de uma aplicação para levantamento de carga
class Cliente:
    def __init__(self, nome, contato, endereco, responsavel, horario_funcionamento):
        self.nome = nome
        self.contato = contato
        self.endereco = endereco
        self.responsavel = responsavel
        self.horario_funcionamento = horario_funcionamento
        

class ConsumoReferencia(Cliente):
    def __init__(self, balcao, iluminacao, outras_cargas, rack_congelados, rack_resfriados,
    selfs, gerador, medidor, quadros, ar_condicionado, camara_preparo):
        self.balcao = balcao
        self.ilunicao = iluminacao
        self.outras_cargas = outras_cargas
        self.rack_congelados = rack_congelados
        self.rack_resfriados = rack_resfriados
        self.selfs = selfs
        self.gerador = gerador
        self.medidor = medidor
        self.quadros = quadros
        self.ar_condicionado = ar_condicionado
        self.camara_preparo = camara_preparo
    


    
        

