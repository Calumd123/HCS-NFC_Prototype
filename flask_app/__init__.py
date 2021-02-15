from flask import Flask 
from .routes.main import main

def create_app():
    app = Flask(__name__,)
    app.run(threaded=True)
    app.register_blueprint(main)
    return app 
