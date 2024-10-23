from app import create_app, db

def main():
    app = create_app()
    
    with app.app_context():
        db.create_all()
        print("Tablas creadas correctamente.")


if __name__ == "__main__":
    main()