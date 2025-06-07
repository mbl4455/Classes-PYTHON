from Person import Person
from Calculadora import Calculadora
from Carro import Carro
from Dog import Dog
from Product import Product

person_1 = Person('José', 17)
person_2 = Person('Marcelo', 15)
dog_1 = Dog('João', "Dalmata")
dog_2 = Dog('Lua', "Pastor-Alemão")
dog_3 = Dog('Kauan', "Buldogue")
calc = Calculadora(100, 100)
car = Carro('Fusca', 0)
product = Product('Macarrão', 50, 25)

person_1.apresentar()
person_2.apresentar()

calc.somar()
calc.subtrair()
calc.multiplicar()
calc.divisao()

car.acelerar()
car.frear()
car.mostrar_velocidade()

dog_1.latir()
dog_2.latir()
dog_3.latir()

product.comprar(1)
product.repor(1)
product.mostrar_estoque()
