from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)


items = [
    {'id': 1, 'campo1': 'Registro 1', 'campo2': 'Registro 1', 'campo3': 'Registro 1', 'campo4': 'Registro 1'},
]


@app.route('/')
def index():
    return render_template('index.html', items=items)


@app.route('/add', methods=['POST'])
def add_item():
    new_item = {
        'id': len(items) + 1,
        'campo1': request.form['campo1'],
        'campo2': request.form['campo2'],
        'campo3': request.form['campo3'],
        'campo4': request.form['campo4']
    }
    items.append(new_item)
    return redirect(url_for('index'))


@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    item = next((i for i in items if i['id'] == item_id), None)
    if request.method == 'POST':
        item['campo1'] = request.form['campo1']
        item['campo2'] = request.form['campo2']
        item['campo3'] = request.form['campo3']
        item['campo4'] = request.form['campo4']
        return redirect(url_for('index'))
    return render_template('edit.html', item=item)


@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
