class Carro:
    def __init__(self, def_model, def_speed):
        self.model = def_model
        self.speed = def_speed


    def acelerar(self):
        self.speed = self.speed + 10
        print(f"Sou um {self.model}, Minha velocidade foi aumentada em 10, estou com a velocidade total de {self.speed} KM por hora.")
    
    def frear(self):
        self.speed = self.speed - 10
        if self.speed < 10:
            self.speed = self.speed = 0
        print(f"Sou um {self.model}, Minha velocidade foi diminuida em 10, estou com a velocidade total de {self.speed} KM por hora.")

    def mostrar_velocidade(self):
        print(f"Sou um {self.model}, Minha velocidade atual é de {self.speed} KM por hora.")