#classe Carro
class Carro:
    #Construtor da classe
    def __init__(self, rodas=5, pneu=5, retrovisor=2, motor=0, modelo=""): #construtor de uma classe em python self diz para construir a propria classe, estou referenciando ela os argumentos são obrigatórios
        #propriedades/atributos da classe
        self.rodas = rodas
        self.pneu = pneu
        self.retrovisor = retrovisor
        self.motor = motor
        self.modelo = modelo

    #métodos da classe
    def ligar_motor(self, empurrar):
        if empurrar:
            return "ligou a chave, empurrou e o motor pegou no tranco..."
        else:
            return "motor ligado pela chave..."
    
    def acelerar_carro(self):
        return "carro acelerado..."
    
    def get_informacoes(self):
        return self.motor, self.modelo
