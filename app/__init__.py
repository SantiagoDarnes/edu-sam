from flask import Flask
from app.extensions import db, mail
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    mail.init_app(app)

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
    
    from app.modules.procedures import bp as procedures_bp
    app.register_blueprint(procedures_bp, url_prefix='/procedures')
    
    from app.modules.personal_data import bp as personal_data_bp
    app.register_blueprint(personal_data_bp, url_prefix='/personal_data')

    from app.modules.settings import bp as settings_bp
    app.register_blueprint(settings_bp, url_prefix='/settings')

    return app