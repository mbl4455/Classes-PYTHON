class Dog:
    def __init__(self, def_name, def_race):
        self.name = def_name
        self.race = def_race

    def latir(self):
        print(f"Au au! Eu sou o {self.name}, da raça {self.race}")