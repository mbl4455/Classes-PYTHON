class Person:
    def __init__(self, def_name, def_age):
        self.name = def_name
        self.age = def_age

    def apresentar(self):
        print(f"Olá, meu nome é {self.name} e tenho {self.age} anos.")