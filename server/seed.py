from models import db
from models.camper import Camper
from models.activity import Activity
from models.signup import Signup
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()

    c1 = Camper(name="Caitlin", age=8)
    c2 = Camper(name="Lizzie", age=9)

    a1 = Activity(name="Archery", difficulty=2)
    a2 = Activity(name="Swimming", difficulty=3)

    db.session.add_all([c1, c2, a1, a2])
    db.session.commit()

    print("✅ Database seeded successfully!")
