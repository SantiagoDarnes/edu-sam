from flask import Flask
from app.extensions import db
from app.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    from app.main import bp as main_bp
    from app.account import bp as account_bp
    from app.static import bp as static_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(account_bp)
    app.register_blueprint(static_bp)
    
    
    @app.route("/test")
    def base():
        return "<h1> Es la base </h1>"
    
    print(app.url_map)
    return app

# Esto no se ejecuta nunca
if __name__ == "__main__":
    app = create_app()
    
    with app.app_context():
        db.create_all()
        print("Tablas creadas correctamente.")