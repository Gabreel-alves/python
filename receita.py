class Receita():
    def __init__(self, sabor, ovo, farinha, fermento, leite, manteiga):
        self.sabor = sabor
        self.ovo = ovo 
        self.farinha = farinha
        self.fermento = fermento
        self.leite = leite
        self.manteiga = manteiga
        
    def get_all(self):
        print("Esse é um bolo, com sabor de {}, vai {} ovo, {} kg de farinha, {}colher de fermento, {}ml de leite e {} colheres de manteiga".format(self.sabor, self.ovo, self.farinha,self.fermento, self.leite, self.manteiga))

bolo = Receita("chocolate",1,1,1,200,3)

class Doce(Receita):
    def __init__(self,sabor,ovo,leite,acucar,leite_condensado):
        self.sabor = sabor
        self.ovo = ovo 
        self.leite = leite
        self.acucar = acucar
        self.leite_condensado = leite_condensado

    def get_pudim(self):
        print("esse é um pudim com sabor de {},nele vai {} ovos, {}ml de leite, {}colheres de acucar, e {}caixa de leite condensado ".format(self.sabor, self.ovo, self.leite, self.acucar, self.leite_condensado))

pudim = Doce("Leite", 3,700,3,1)

pudim.get_pudim()