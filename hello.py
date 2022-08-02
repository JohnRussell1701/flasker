from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Create a Flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "my super secret key that noone is supposed to know"


# Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("What's your name", validators=[DataRequired()])
    submit = SubmitField("Submit")


# Create a route decorator
# @app.route('/')
# def index():
#     return "<h1>Hello, World!</h1>"


@app.route('/')
def index():
    name = 'John'
    stuff = "this is lowercase text that has been changed to title case."
    favorite_pizza = ['pepperoni', 'cheese', 'black olives']
    return render_template('index.html',
                           name=name,
                           stuff=stuff,
                           favorite_pizza=favorite_pizza)


# localhost:5000/user/john
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)


#Custom Error Pages


#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


def page_not_found(e):
    return render_template('500.html'), 500


@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    # Validate form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Successfully!")

    return render_template('name.html', name=name, form=form)
