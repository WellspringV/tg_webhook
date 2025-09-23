from flask import Blueprint
from flask import render_template


timetrack_bp = Blueprint("timetrack", __name__, template_folder="templates")


@timetrack_bp.route("/")
def index():
    return render_template('timetrack/index.html', menu = ["one", "two", "three"])
