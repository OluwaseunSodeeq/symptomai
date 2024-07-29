from flask import Flask, render_template, request, redirect, url_for, flash
import re
# import os
# from dotenv import load_dotenv
# import matplotlib.pyplot as plt
# import random
# import google.generativeai as genai
# from flask_cors import CORS

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

# load_dotenv()
# api_key = os.getenv("GOOGLE_API_KEY")


# genai.configure(api_key=api_key)

# # Initialize Flask app
# app = Flask(__name__)
# CORS(app)

# # Function to get the response from the generative AI model
# def get_gemini_response(input_symptoms, input_prompt):
#     model = genai.GenerativeModel('gemini-pro')
#     response = model.generate_content([input_symptoms, input_prompt])
#     return response.text

# # Function to plot and save the confidence score
# def plot_confidence_score(confidence_score):
#     fig, ax = plt.subplots()
#     ax.barh(['Confidence'], [confidence_score], color='blue')
#     ax.set_xlim(0, 100)
#     ax.set_xlabel('Confidence Score (%)')
#     plt.title('Diagnosis Confidence Score')
#     image_path = 'static/confidence_score.png'
#     plt.savefig(image_path)
#     plt.close()
#     return image_path

# @app.route('/diagnose', methods=['POST'])
# def diagnose():
#     data = request.json
#     input_symptoms = data.get("symptoms")
#     input_prompt = "You are an expert doctor. Diagnose the illness based on the described symptoms."

#     if input_symptoms:
#         # Get the response from the generative model
#         diagnosis = get_gemini_response(input_symptoms, input_prompt)
#         # Generate a random confidence score for demonstration purposes
#         confidence_score = random.uniform(70, 100)
#         # Plot and save the confidence score image
#         confidence_score_image = plot_confidence_score(confidence_score)
#         # Return the diagnosis and the confidence score image path
#         formatted_diagnosis = diagnosis.replace("\n\n", "<br><br>").replace("\n", "<br>").replace("**", "<b>").replace("**", "</b>")
#         # Return the diagnosis and the confidence score image path
#         return jsonify({"diagnosis": formatted_diagnosis, "confidence_score_image": confidence_score_image})
#     else:
#         return jsonify({"error": "Please enter the symptoms"}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

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
