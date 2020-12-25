from flask import Blueprint

from flask import render_template,  request
from flaskPracticalWebapp.models import Practical
from flask_login import current_user


main = Blueprint("main", __name__)

@main.route('/')
def home():
    title = "Dashboard"
    page = request.args.get("page", 1, type=int)
    if current_user.is_authenticated:
        practicals = Practical.query.filter_by(user_id=current_user.id).paginate(page=page, per_page=5)
    else:
        practicals = Practical.query.filter_by(default=True).paginate(page=page, per_page=5)



    return render_template("index.html", title=title, practicals=practicals)
