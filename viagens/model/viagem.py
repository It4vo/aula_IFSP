from datetime import datetime
from database import db

class Viagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ida = db.Column(db.DateTime, nullable=False)
    chegada = db.Column(db.DateTime, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    destino = db.Column(db.String(120), nullable=False)

    

