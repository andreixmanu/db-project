from app import create_app, db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # crea le tabelle se non esistono
    app.run(debug=True)