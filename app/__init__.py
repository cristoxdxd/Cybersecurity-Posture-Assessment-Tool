from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'dev-key-to-change'

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
