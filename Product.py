class Product:
    def __init__(self, def_name, def_price, def_stock):
        self.name = def_name
        self.stock = def_stock
        self.price = def_price

    def comprar(self, qtd):
        self.stock = self.stock - qtd
        if self.stock - qtd < 0:
            self.stock = self.stock = 0
        print(f"Você comprou o produto: {self.name}, que custava: {self.price}R$ e agora tem {self.stock} em estoque.")

    def repor(self, qtd):
        self.stock = self.stock + qtd
        print(f"Você repos o estoque de {self.name}, e agora tem {self.stock}")

    def mostrar_estoque(self):
        print(f"O estoque de {self.name} é {self.stock}")
        