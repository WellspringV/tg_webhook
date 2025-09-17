from flask import Blueprint
from flask import render_template


posts_bp = Blueprint("posts", __name__, template_folder="templates")


@posts_bp.route("/")
def index():
    return render_template('posts/index.html')
