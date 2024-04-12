from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
import sqlalchemy as sa
from app import db
from app.models import User
from profanity_check import predict

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField(
        "Repeat Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Register") 

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(User.username == username.data))
        if user is not None or predict([username.data]):
            raise ValidationError("Please use a different username.")
    
    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(User.email == email.data))
        if user is not None:
            raise ValidationError("Please use a different email address.")


class EditProfileForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Submit")

    def __init__(self, original_username, original_email, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_username = original_username
        self.original_email = original_email

    def validate_username(self, username):
        if username.data != self.original_username:
            user = db.session.scalar(
                sa.select(User).where(User.username == self.username.data)
            )
            if user is not None or predict([username.data]):
                raise ValidationError("Please use a different username!")

    def validate_email(self, email):
        if email.data != self.original_email:
            user = db.session.scalar(
                sa.select(User).where(User.email == self.email.data)
            )
            if user is not None:
                raise ValidationError("Use a different email!")

class AddIngredientForm(FlaskForm):
    itemname = StringField(
        "Item Name", validators=[DataRequired(), Length(min=1, max=140)]
    )
    supply = IntegerField("Number Added", validators=[DataRequired()])
    menu_id = IntegerField("Menu ID")
    #menu = StringField("Menu Entry", validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField("Submit")

    def validate_itemname(self, itemname):
        if predict([itemname.data]):
            raise ValidationError("Please add a different ingredient!")
    
    def validate_supply(self, supply):
        if supply.data > 9999:
            print(f"error {supply.data} \n")
            raise ValidationError("Please enter a lower number!")


class EditItemForm(FlaskForm):
    itemname = StringField(
        "Item Name", validators=[DataRequired(), Length(min=1, max=140)]
    )
    supply = IntegerField("Total Supply", validators=[DataRequired()])
    submit = SubmitField("Submit")
    
    def validate_itemname(self, itemname):
        if predict([itemname.data]):
            raise ValidationError("Please add a different ingredient!")
    
    def validate_supply(self, supply):
        if supply.data > 9999:
            print("error")
            raise ValidationError("Please enter a lower number!")


#class AddMenuEntry(FlaskForm):
    
