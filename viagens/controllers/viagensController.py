from flask import Blueprint, redirect

viagensController = Blueprint('viagens',__name__)

@viagensController

@app.route('/add_viagem', methods=['GET', 'POST'])
def add_viagem():
    if request.method == 'POST':
        # Obtendo os dados do formulário
        destino = request.form['destino']
        ida = datetime.strptime(request.form['ida'], '%Y-%m-%dT%H:%M')
        chegada = datetime.strptime(request.form['chegada'], '%Y-%m-%dT%H:%M')
        preco = float(request.form['preco'])

        # Criando a nova viagem
        nova_viagem = Viagem(ida=ida, chegada=chegada, preco=preco, destino=destino)

        # Salvando a viagem no banco de dados
        db.session.add(nova_viagem)
        db.session.commit()

        # Redirecionando para uma página de sucesso ou listagem de viagens
        
    return render_template('formulario_viagem.html')
