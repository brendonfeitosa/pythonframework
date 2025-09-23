class Carro:
    def __init__(self, rodas, pneu, retrovisor, motor): #construtor de uma classe em python self diz para construir a propria classe, estou referenciando ela os argumentos são obrigatórios
        self.rodas = rodas
        self.pneu = pneu
        self.retrovisor = retrovisor
        self.motor = motor

    def ligar_motor(self):
        return "motor ligado..."
    
    def acelerar_carro(self):
        return "carro acelerado..."
