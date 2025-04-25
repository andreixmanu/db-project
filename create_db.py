from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()  # Crea le tabelle nel database
    print("Tabelle create con successo!")
