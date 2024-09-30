from flask import Blueprint,render_templete
from models import tarefas

tarefas_controller= Blueprint('tarefa',__name__)

@tarefas_controller.route('/')
def index():
    return render_template('index.html', tarefas=tarefas)