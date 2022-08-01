from flask import Flask, render_template

# Create a Flask instance
app = Flask(__name__)

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