from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, login_required, logout_user
import sqlalchemy as sa
from app import app, db
from app.forms import (
    LoginForm,
    RegistrationForm,
    EditProfileForm,
    AddIngredientForm,
    EditItemForm,
)
from app.models import User, Item
from datetime import datetime, timezone
from urllib.parse import urlsplit


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/inventory", methods=["GET", "POST"])
@login_required
def inventory():
    form = AddIngredientForm()
    # additem_form = AddItemForm()
    # edititem_form = EditItemForm()
    if form.validate_on_submit():
        item = Item(name=form.item_name.data, supply=form.supply.data)
        db.session.add(item)
        db.session.commit()
        flash("Inventory Modified")
        return redirect(url_for("inventory"))

    items = db.session.scalars(sa.select(Item)).all()
    # return render_template("inventory.html", title="Celery Stocks - Inventory", additem_form=additem_form, edititem_form=edititem_form)
    return render_template(
        "inventory.html",
        title="Celery Stocks - Manage Inventory",
        form=form,
        items=items,
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data)
        )
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or urlsplit(next_page).netloc != "":
            next_page = url_for("inventory")
        current_user.last_seen = datetime.now(timezone.utc)
        db.session.commit()
        return redirect(next_page)

    return render_template("login.html", title="Sign In", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("inventory"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Registration complete")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)


@app.route("/user/<username>")
@login_required
def user(username):
    user = db.first_or_404(sa.select(User).where(User.username == username))
    return render_template("user.html", user=user)


@app.route("/edit_profile", methods=["GET", "POST"])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        db.session.commit()
        flash("Changes Saved")
        return redirect(url_for("edit_profile"))
    elif request.method == "GET":
        form.username.data = current_user.username
    return render_template("edit_profile.html", title="Edit Account", form=form)


@app.route("/create_menu_item", methods=["GET", "POST"])
@login_required
def createMenuItem():
    form = createMenuItem()
    if form.validate_on_submit():
        db.session.add(form.createMenuItem.data())
        db.session.commit()

#@app.route("/create_order", methods=["GET", "POST"])
#@login_required
# def createOrder():
#    todo
