
class Animal():
    def __init__(self,pelo,especie,olhos,patas):
        self.pelo = pelo
        self.especie = especie
        self.olhos = olhos
        self.patas = patas
    
    def get_all(self):
        print("esse animal é um {} tem{} olhos e tem {} patas.".format(self.especie, self.olhos,
        self.patas))

porco = Animal(True, "Suino",2, 4 )

porco.get_all()







