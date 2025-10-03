from flask import Flask

app = Flask(__name__) #objeto que vai rodar na função main do python









if __name__ == '__main__': #checando se main existe no __name__
    app.run(debug=True)


