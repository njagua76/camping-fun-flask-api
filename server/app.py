from flask import Flask
from flask_migrate import Migrate
from models import db
from controllers.campers_controller import campers_bp
from controllers.activities_controller import activities_bp
from controllers.signups_controller import signups_bp

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(campers_bp)
app.register_blueprint(activities_bp)
app.register_blueprint(signups_bp)

if __name__ == '__main__':
    app.run(port=5555)
    