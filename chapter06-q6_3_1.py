class Nigiri:
    category = "握り"
    top = "ネタ"
    base = "シャリ"

    def show_attributes(self):
        print("top:{}, base:{}, category: {}".format(self.top, self.base, self.category))

class Katuo(Nigiri):
    top = "カツオ"
    toppring = "生姜とネギ"
    price = 100

    def show_attributes(self):
        super().show_attributes()
        print("price: {}円".format(self.price))

b1 = Katuo()
b1.show_attributes()
