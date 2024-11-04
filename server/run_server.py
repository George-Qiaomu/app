# run_server.py

from src import create_app
from src.database import db

print("Creating Flask app...")
app = create_app()
print("Flask app created.")

with app.app_context():
    print("Creating database tables...")
    db.create_all()
    print("Database tables created.")

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)
