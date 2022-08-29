class Usuario:

    def __init__(self, id, senha):
        self.id = id
        self.senha = senha
        
class Loja:

    def __init__(self, numero, supervisorio, ip, usuario, senha, endereco, comentarios):
        self.numero = numero
        self.supervisorio = supervisorio
        self.ip = ip
        self.usuario = usuario
        self.senha = senha
        self.endereco = endereco
        self.comentarios = comentarios
        self.sts = ['Automatico', 'Manual']

    def sts_supervisao_resfriados(self, status):
        if status in self.sts:
            self.status_resfriados = status
        else:
            raise Exception('Opção inválida')

    def sts_supervisao_congelados(self, status):
        if status in self.sts:
            self.status_congelados = status
        else:
            raise Exception('Opção inválida')

    def sts_supervisao_iluminacao(self, status):
        if status in self.sts:
            self.status_iluminacao = status
        else:
            raise Exception('Opção inválida')

    def sts_supervisao_arcondicionado(self, status):
        if status in self.sts:
            self.status_arcondicionado = status
        else:
            raise Exception('Opção inválida')

class Status(Loja):
    
    def __init__(self, numero, supervisorio, ip, usuario, senha, endereco, comentarios, status_resfriados, status_congelados, status_iluminacao, status_arcondicionado):
        super().__init__(numero, supervisorio, ip, usuario, senha, endereco, comentarios)
        self.status_resfriados = status_resfriados
        self.status_congelados = status_congelados
        self.status_iluminacao = status_iluminacao
        self.status_arcondicionado = status_arcondicionado
    
   
    
            

## Testando criação de Objetos

loja_0061 = Loja('0061' , 'Honeywell', '10.154.125.45', 'admin', 'admin123', 'Av. Maria, Vila Maria, São Paulo - SP Cep 00000-000','Sem comunicação desde 12/08')
loja_0062 = Loja('0055' , 'Honeywell', '10.154.125.44', 'admin2', 'admin123', 'Av. Maria, Vila Maria, São Paulo - SP Cep 00000-000','Sem comunicação desde 12/08')
loja_0061.sts_supervisao_arcondicionado('Manual')

## usuario_neilton = Usuario('input', 'input')


print(loja_0062.ip)
print(loja_0062.usuario)
print(loja_0062.senha)
print(loja_0061.sts_supervisao_arcondicionado)





       
        




