from flask import Flask
from app.api.v2 import api_bp as api_v2_blueprint


app = Flask(__name__)
app.register_blueprint(api_v2_blueprint)


@app.route("/")
def index():
    return "<h1>Test from flask app</h1>"


if __name__ == "__main__":
    app.run()
