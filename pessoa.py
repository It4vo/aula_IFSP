class Gente:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def apresentar(self):
        print(
              f'Ola meu nome eh {self.nome} e eu tenho {self.idade} anos'
        )


