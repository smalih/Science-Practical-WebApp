from flask import render_template, url_for, flash, redirect, request
from flaskPracticalWebapp.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flaskPracticalWebapp.models import User, Practical
from flaskPracticalWebapp import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
def home():
    title = "Dashboard"

    return render_template("index.html", title=title)


@app.route('/register', methods=["GET", "POST"])
def register():
    title = "Register"
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been successfully created! You are now able to log in.", "success")
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
            # [1:] in place as request.args.get returns url with \ included (eg \profile rather than just profile). url_for takes in name of function.
            return redirect(url_for(next_page[1:])) if next_page else redirect(url_for("home"))


        else:
            flash("Login credentials incorrect. Please check email and password", "danger")
    return render_template("login.html", title=title, form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateAccountForm()

    if form.validate_on_submit():

        current_user.fname = form.fname.data
        current_user.surname = form.surname.data
        current_user.dob = form.dob.data
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
