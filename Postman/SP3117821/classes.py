class Pessoa:
    def __init__ (self,nome,prontuario):
        self.nome=nome
        self.prontuario=prontuario
class Professor(Pessoa):
    def __init__ (self,diciplina):
        super().__init__("Igor","3117821")
        self.diciplina=diciplina
    

    def apresentarProfessor(self):
        print(f"Ola, meu nome é {self.nome} e tenho o prontuário:{self.prontuario} e sou da diciplina {self.diciplina}.")





class Aluno(Pessoa):
    def __init__ (self,turma):
        super().__init__("Rafael","3117821")
        self.turma=turma
    

    def apresentarAluno(self):
        print(f"Ola, meu nome é {self.nome} e tenho o prontuário:{self.prontuario} e sou da turma {self.turma}.")


class Disciplina:
    def __init__ (self,nome,professor):
        self.nome=nome
        self.professor=professor
    def apresentarDiciplina(self):
        print(f"O nome da máteria é {self.nome} e o professor é {self.professor}")

class Nota:
    def __init__ (self,nota):
        self.nota=nota

    def apresentarNota(self):
        print(f"sua nota foi {self.nota}")




