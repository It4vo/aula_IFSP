from dao import ViagemDAO
from model.viagem import Viagem

class ViagemRepository:
    def __init__(self) -> None:
        self.userDao = ViagemDAO()

    def create_viagem(self, id,ida,chegada,preco,destino):
        nova_viagem
        return self.userDao.add_viagem(id,ida,chegada,preco,destino)
