import datetime
from flask import (
    Flask,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
    flash,
)
from flask_sqlalchemy import SQLAlchemy
from config import Config
from forms import LoginForm

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html", utc_dt=datetime.datetime.utcnow())


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            "Login request for {}, remember={}".format(
                form.username.data, form.remember_me.data
            )
        )
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)


if __name__ == "__main__":
    app.run()
