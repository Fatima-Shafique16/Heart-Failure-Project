from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the updated Logistic Regression model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')  # your HTML form file

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect form inputs and convert to correct type
        age = float(request.form['age'])
        anaemia = int(request.form['anaemia'])
        cpk = float(request.form['creatinine_phosphokinase'])
        diabetes = int(request.form['diabetes'])
        ejection_fraction = float(request.form['ejection_fraction'])
        high_blood_pressure = int(request.form['high_blood_pressure'])
        platelets = float(request.form['platelets'])
        serum_creatinine = float(request.form['serum_creatinine'])
        serum_sodium = float(request.form['serum_sodium'])
        sex = int(request.form['sex'])
        smoking = int(request.form['smoking'])
        time = float(request.form['time'])

        # Make sure order matches training dataset
        features = [age, anaemia, cpk, diabetes, ejection_fraction,
                    high_blood_pressure, platelets, serum_creatinine,
                    serum_sodium, sex, smoking, time]

        final_features = np.array([features])

        # Predict probability
        probability = model.predict_proba(final_features)[0][1] * 100  # death probability

        # Set threshold (you can adjust this)
        probability_threshold = 0.3  # 30%
        if probability >= probability_threshold:
            result = f"⚠️ High Risk – Death Event ({probability:.2f}% probability)"
        else:
            result = f"✅ Low Risk – No Death Event ({probability:.2f}% probability)"

        return render_template('index.html', prediction_text=result)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)
