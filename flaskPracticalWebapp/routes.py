import secrets, os
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from flaskPracticalWebapp.forms import RegistrationForm, LoginForm, UpdateAccountForm, PracticalForm
from flaskPracticalWebapp.models import User, Practical
from flaskPracticalWebapp import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
def home():
    title = "Dashboard"
    practicals = Practical.query.all()
    return render_template("index.html", title=title, practicals=practicals)


@app.route('/register', methods=["GET", "POST"])
def register():
    title = "Register"
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(email=form.email.data, password=hashed_password, dob=form.dob.data)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been successfully created! Please login.", "success")
        return redirect(url_for('login'))
    return render_template("register.html", title=title, form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    title = "Login"
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get("next")
            # [1:] in place as request.args.get returns url with \ included (eg "\profile" rather than just "profile"), url_for takes in name of function.
            return redirect(url_for(next_page[1:])) if next_page else redirect(url_for("home"))


        else:
            flash("Login credentials incorrect. Please check email and password", "danger")
    return render_template("login.html", title=title, form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("login"))


def save_profile_pic(form_picture):
    random_hex = secrets.token_hex(8)
    _, file_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + file_ext
    picture_path = os.path.join(app.root_path, "static/profile_pics", picture_filename)
    output_size = (125, 125)
    resized_pic = Image.open(form_picture)
    resized_pic.thumbnail(output_size)
    resized_pic.save(picture_path)

    return picture_filename



@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateAccountForm()
    update = False

    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_profile_pic(form.picture.data)
            current_user.profile_pic = picture_file
            update = True
        if current_user.fname != form.fname.data or current_user.surname != form.surname.data:
            current_user.fname = form.fname.data
            current_user.surname = form.surname.data
            update = True
        if update:
            db.session.commit()
            flash("Your changes have been saved!", "success")
            return redirect(url_for("profile"))
    elif request.method == "GET":
        form.fname.data = current_user.fname
        form.surname.data = current_user.surname
        form.email.data = current_user.email
    title = f"{current_user.fname} {current_user.surname}"
    if not(title):
        title=f"User Profile"
    profile_pic = url_for('static', filename=f"profile_pics/{current_user.profile_pic}")
    return render_template("profile.html", title=title, form=form, profile_pic=profile_pic)

@app.route('/settings')
@login_required
def settings():
    title = "Settings"
    return render_template("settings.html", title=title)


@app.route('/gcse/biology')
def gcse_biology():
    title = "GCSE Biology"
    return render_template("/biology/biology-gcse.html", title=title)


@app.route('/alevel/biology')
def alevel_biology():
    title = "A Level Biology"
    return render_template("/biology/biology-alevel.html", title=title)


@app.route('/gcse/chemistry')
def gcse_chemistry():
    title = "GCSE Chemistry"
    return render_template("/chemistry/chemistry-gcse.html", title=title)


@app.route('/alevel/chemistry')
def alevel_chemistry():
    title = "A Level Chemistry"
    return render_template("/chemistry/chemistry-alevel.html", title=title)


@app.route('/gcse/physics')
def gcse_physics():
    title = "GCSE Physics"
    return render_template("/physics/physics-gcse.html", title=title)


@app.route('/alevel/physics')
def alevel_physics():
    title = "A Level Physics"
    return render_template("/physics/physics-alevel.html", title=title)

@app.route('/practical/new', methods=["GET", "POST"])
@login_required
def new_practical():
    form = PracticalForm()
    if form.validate_on_submit():
        practical = Practical(title=form.title.data,
                              degStudy=form.degStudy.data,
                              equipment=form.equipment.data,
                              method=form.method.data)
        db.session.add(practical)
        db.session.commit()
        flash("Your new practical has been saved!", "success")
        return redirect(url_for("home"))
    return render_template("create_practical.html", title="New Practical", form=form)


@app.route('/practical/<practical_title>')
def practical(practical_title):

    practical = Practical.query.filter_by(title=practical_title).first()
    return render_template("practical.html", title=practical.title, practical=practical)

@app.route('/practical/<practical_title>/update', methods=["GET", "POST"])
@login_required
def update_practical(practical_title):
    # Should be using get_or_404 or first_or_404 function
    practical = Practical.query.filter_by(title=practical_title).first()
    title = practical.title

    form = PracticalForm()
    if form.validate_on_submit():
        practical.title = form.title.data
        practical.degStudy = form.degStudy.data
        practical.subject = form.subject.data
        practical.equipment = form.equipment.data
        practical.method = form.method.data
        db.session.commit()
        flash("Your practical has been updated!", "success")
        return redirect(url_for("practical", practical_title=practical.title))
    elif request.method == "GET":
        form.title.data = practical.title
        form.degStudy.data = practical.degStudy
        form.subject.data = practical.subject
        form.equipment.data = practical.equipment
        form.method.data = practical.method

    return render_template("create_practical.html", title="Update Practical", form=form)
