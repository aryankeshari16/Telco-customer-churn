from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load model and column names
model = joblib.load('model/churn_model.pkl')
feature_columns = joblib.load('model/feature_columns.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = {
            'InternetService': request.form['InternetService'],
            'MonthlyCharges': float(request.form['MonthlyCharges']),
            'Contract': request.form['Contract'],
            'tenure': int(request.form['tenure']),
            'TotalCharges': float(request.form['TotalCharges']),
            'PaymentMethod': request.form['StreamingTV'],
            'TechSupport': request.form['TechSupport']
        }

        input_df = pd.DataFrame([input_data])
        input_encoded = pd.get_dummies(input_df)
        input_encoded = input_encoded.reindex(columns=feature_columns, fill_value=0)

        prediction = model.predict(input_encoded)[0]
        result = "Customer is likely to CHURN." if prediction == 1 else "Customer is NOT likely to churn."

        return render_template('index.html', prediction_text=result)

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
