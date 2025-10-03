from flask_migrate import Migrate
from flask_restful_swagger_3 import Api
from api import register_apis
from application import create_app
from db import db

app = create_app()
migrate = Migrate(app, db)

api = Api(app)
register_apis(api)


if __name__ == "__main__":
    app.run()
