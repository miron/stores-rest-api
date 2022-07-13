import os 
from datetime import timedelta
from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT
from db import db
os.environ["DB_URL"] = "postgresql://streetyogi:<pwd>@localhost:5432/streetyogi"

from security import authenticate, identity as identity_function
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
# from models.user import UserModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "miron"
api = Api(app)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

# app.config["JWT_AUTH_URL_RULE"] = "/login"
jwt = JWT(app, authenticate, identity_function)  # / auth
# config JWT to expire within half an hour
app.config["JWT_EXPIRATION_DELTA"] = timedelta(seconds=1800)
# config JWT auth key name to be 'email' instead of default 'username'
# app.config["JWT_AUTH_USERNAME_KEY"] = "email"


@jwt.auth_response_handler
def customized_response_handler(access_token, identity):
    return jsonify(
        {"access_token": access_token.decode("utf-8"), "user_id": identity.id}
    )


@jwt.jwt_error_handler
def customized_error_handler(error):
    return jsonify({
                       'message': error.description,
                       'code': error.status_code
                   }), error.status_code


api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, "/register")
# api.add_resource(UserModel, "/user")


if __name__ == "__main__":
    app.run(port=5000, debug=True)


