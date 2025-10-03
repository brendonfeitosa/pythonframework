from flask import Flask

app = Flask(__name__) #objeto que vai rodar na função main do python

@app.route('/buscar/<int:user_id>/<string:nome>', methods=['GET', 'POST']) #decorator para passar uma rota, ele deve sempre estar em cima da sua função
def buscar(user_id, nome):
    return f"Usuário: id: {user_id} - Nome: {nome}"
    
"""
@app.route('/buscar/<int:user_id>', methods=['GET']) #decorator para passar uma rota, ele deve sempre estar em cima da sua função #aqui estou pedindo para que o usuário passe na url o id do usuário
def buscar(user_id):
    if user_id == 1:
        return "Brendon"
    elif user_id == 2:
        return "Helena"
    else:
        return "Usuário não encontrado..."
"""





if __name__ == '__main__': #checando se main existe no __name__
    app.run(debug=True)


