from model.viagem import Viagem, db

class ViagemDAO:
   @staticmethod
    def add_viagem(viagem):
        db.session.add(viagem)
        db.session.commit()
        return viagem

