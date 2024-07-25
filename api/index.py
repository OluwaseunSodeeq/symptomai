from flask import Flask, render_template, request, redirect, url_for, flash
import re

app = Flask(__name__)
app.secret_key = "secret"  # Replace with a secure key

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/signIn", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])

def signIn():
    if request.method == "POST":
        isValid = True
        print("Form submitted!")

        full_name = request.form["full-name"]
        email = request.form["email"]
        password = request.form["password"]

        print(f"Full Name: {full_name}, Email: {email}, Password: {password}")

        # Full Name validation
        if len(full_name) < 3:
            flash('Full Name must be at least 3 characters long', "name-error")
            isValid = False
            print("Full Name error")

        # Email validation
        if not email.endswith('.com'):
            flash('Email must end with .com', 'email-error')
            isValid = False 
            print("Email error")

        # Password validation
        password_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[\W_]).{1,}$')
        if not password_pattern.match(password):
            flash('Password must contain at least one lowercase letter, one uppercase letter, and one special character.', 'password-error')
            isValid = False
            print("Password error")
        if isValid:
            flash('Signup successful!', 'success')
            print("Validation passed. Redirecting to chatbox.")
            user_values = {
                'full_name': full_name,
                'email': email
            }
            return redirect(url_for('chatbox', **user_values))
        else:
            print("Validation failed. Reloading sign-in page.")

    return render_template("signin.html")

@app.route("/chatbox")
def chatbox():
    full_name = request.args.get('full_name')
    email = request.args.get('email')
    print(f"Chatbox accessed with Full Name: {full_name}, Email: {email}")
    return render_template("chatbox.html", full_name=full_name, email=email)

if __name__ == '__main__':
    app.run(debug=True)





# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'Hello, World!'

# @app.route('/about')
# def about():
#     return 'About'