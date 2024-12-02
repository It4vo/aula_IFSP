from flask import Flask
from database import init_db
from controllers import viagensController

app = Flask(__name__)
app.register_blueprint(viagensController)

if __name__ == "__main__":
    init_db(app)
    app.run(debug = True)
    