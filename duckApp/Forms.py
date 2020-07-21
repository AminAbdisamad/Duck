from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email, Length, ValidationError
from duckApp.models.User import User


# Registration Form
class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=3, max=20)]
    )
    email = StringField("Email", validators=[DataRequired(), Email(), Length(min=5)])
    password = PasswordField("Password", validators=[DataRequired()])
    confirmPassword = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")

    # Custome validation
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                f"{user.username} already exist. Please choose different one."
            )

    # Custome validation
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email already exist. Please choose different one.")


# Login Form
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


# Androma


# Update AccountForm
class UpdateAccountForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=3, max=20)]
    )
    email = StringField("Email", validators=[DataRequired(), Email(), Length(min=5)])
    name = StringField("Name")
    location = StringField("Location")
    bio = TextAreaField("Bio")
    picture = FileField(
        "Upload Profile Image", validators=[FileAllowed(["jpeg", "jpg", "png"])]
    )

    submit = SubmitField("Update Profile")

    # Custome validation
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(f"{user.username}  waala haystaa fadlan midkale dooro")

    # Custome validation
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("Email waala haystaa fadlan midkale dooro")


class CreatePost(FlaskForm):
    post = TextAreaField(
        "Create Post",
        validators=[DataRequired(), Length(min=5)],
        render_kw={"placeholder": "Maxaa Maskaxdaada ku jira"},
    )
    submit = SubmitField("Submit")
