from flask import Flask              # From the flask module import the Flask Class

# Create an instance of the Flask class into app
app = Flask(__name__)
# app is now an "object"\


# Flask decorator that allows us to map a route to a view function
@app.get("/")
def index():
    return "<h1>Hello, World!</h1>"


# x = index() #function call

@app.get("/about")
def get_about():
    me = {
        "first_name": "Aldrian",
        "last_name": "Almonte",
        "hobbies": "Riding Motorcycles",
        "active": True
    }
    return me
