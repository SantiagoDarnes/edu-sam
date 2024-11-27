from flask import Flask
from app.extensions import db
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.modules.home import bp as home_bp
    app.register_blueprint(home_bp, url_prefix='/home')

    from app.modules.login import bp as login_bp
    app.register_blueprint(login_bp, url_prefix='/login')
    
    from app.modules.subject_registration import bp as subject_registration_bp
    app.register_blueprint(subject_registration_bp, url_prefix='/subject_registration')
    
    from app.modules.exam_registration import bp as exam_registration_bp
    app.register_blueprint(exam_registration_bp, url_prefix='/exam_registration')
    
    from app.modules.reports import bp as reports_bp
    app.register_blueprint(reports_bp, url_prefix='/reports')

    return app