from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib
import mysql.connector

app = Flask(__name__)
CORS(app)

# =========================================
# MYSQL CONNECTION
# =========================================

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Qazi.siddiqui.9012",
    database="caresense_ai"
)

print("MySQL Connected Successfully!")

# =========================================
# LOAD AI MODELS
# =========================================

try:
    emergency_model = joblib.load("emergency_model.joblib")
    icu_model = joblib.load("icu_model.joblib")
    readmission_model = joblib.load("readmission_model.joblib")
    scaler = joblib.load("scaler.joblib")

    print("AI Models Loaded Successfully!")

except Exception as e:
    print("Model Loading Error:", e)

# =========================================
# HOME ROUTE
# =========================================

@app.route('/')
def home():
    return jsonify({
        "message": "CareSense AI Backend Running Successfully"
    })

# =========================================
# DASHBOARD ANALYTICS API
# =========================================
@app.route('/dashboard', methods=['GET'])
def dashboard():
    try:
        if not db.is_connected():
            db.reconnect()
            
        dashboard_cursor = db.cursor(dictionary=True)

        # just need the count of total patients
        dashboard_cursor.execute("SELECT COUNT(*) AS total FROM patients")
        total = dashboard_cursor.fetchone()['total'] or 0

        dashboard_cursor.close()

        return jsonify({
            "total_patients": total
        })

    except Exception as e:
        print("Dashboard API Error:", str(e))
        return jsonify({"error": str(e)}), 500
# =========================================
# PREDICTION API
# =========================================

@app.route('/predict', methods=['POST'])
def predict():

    try:

        data = request.json

        cols = [
            "HR",
            "BP_Systolic",
            "BP_Diastolic",
            "Temp",
            "SpO2",
            "RR",
            "Age",
            "Stay",
            "PrevAdm"
        ]

        raw_features = pd.DataFrame([[

            float(data['HR']),
            float(data['BP_Systolic']),
            float(data['BP_Diastolic']),
            float(data['Temp']),
            float(data['SpO2']),
            float(data['RR']),
            float(data['Age']),
            float(data['Stay']),
            float(data['PrevAdm'])

        ]], columns=cols)

        features_scaled = scaler.transform(raw_features)

        # AI Predictions
        emergency_pred = int(
            emergency_model.predict(raw_features)[0]
        )

        icu_pred = int(
            icu_model.predict(features_scaled)[0]
        )

        readmission_prob = float(
            readmission_model.predict_proba(raw_features)[0][1] * 100
        )

        # Reconnect if disconnected
        if not db.is_connected():
            db.reconnect()

        insert_cursor = db.cursor()

        sql = """
        INSERT INTO patients (
            Full_Patient_Name,
            Patient_ID,
            HR,
            BP_Systolic,
            BP_Diastolic,
            Temp,
            SpO2,
            RR,
            Age,
            Stay,
            PrevAdm,
            Emergency_Level,
            ICU_Required,
            Readmission_Probability
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (

            str(data['Full_Patient_Name']),
            str(data['Patient_ID']),
            int(data['HR']),
            int(data['BP_Systolic']),
            int(data['BP_Diastolic']),
            float(data['Temp']),
            int(data['SpO2']),
            int(data['RR']),
            int(data['Age']),
            int(data['Stay']),
            int(data['PrevAdm']),
            emergency_pred,
            icu_pred,
            round(readmission_prob, 2)

        )

        insert_cursor.execute(sql, values)

        db.commit()

        insert_cursor.close()

        return jsonify({

            "success": True,
            "emergency": emergency_pred,
            "icu": icu_pred,
            "readmission_prob": round(readmission_prob, 2)

        })

    except Exception as e:

        print("CRITICAL ERROR:", str(e))

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

# =========================================
# SEARCH PATIENT
# =========================================

@app.route('/patient/<patient_id>', methods=['GET'])
def get_patient(patient_id):

    try:

        search_cursor = db.cursor(dictionary=True)

        query = "SELECT * FROM patients WHERE Patient_ID = %s"

        search_cursor.execute(query, (patient_id,))

        result = search_cursor.fetchall()

        search_cursor.close()

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500

# =========================================
# SERVER START
# =========================================

if __name__ == '__main__':

    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000
    )