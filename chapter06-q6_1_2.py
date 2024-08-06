class Person:
    def __init__(self, name, nationality, address, birth_year):
        self.name = name
        self.nationality = nationality
        self.address = address
        self.birth_year = birth_year

    def show_attributes(self):
        print(f"Name: {self.name}")
        print(f"Nationality: {self.nationality}")
        print(f"Address: {self.address}")
        print(f"Birth_year: {self.birth_year}")

person1 = Person("Dwayne Douglas Johnson", "American","ヘイワード (カリフォルニア州)",1972)
person1.show_attributes()
