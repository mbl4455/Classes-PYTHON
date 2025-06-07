class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def somar(self):
        print(self.numero1 + self.numero2)

    def subtrair(self):
        print(self.numero1 - self.numero2)

    def multiplicar(self):
        print(self.numero1 * self.numero2)

    def divisao(self):
        try:
            print(self.numero1 / self.numero2)
        except ZeroDivisionError:
            print("Erro: Divisão por Zero")