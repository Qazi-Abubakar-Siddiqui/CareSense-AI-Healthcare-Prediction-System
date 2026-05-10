# 🏥 CareSense AI — Intelligent Healthcare Prediction System

> Predicting Patient Risk Before It Becomes Critical.

---

# 📌 Project Overview

CareSense AI is an AI-powered healthcare intelligence system developed to assist hospitals and healthcare professionals in predicting patient risks using Machine Learning and real-time analytics.

The system analyzes patient clinical vitals and predicts:

✅ Emergency Risk Level  
✅ ICU Admission Requirement  
✅ Readmission Probability  

The platform also includes:

- 🌐 Modern Interactive Frontend Dashboard
- 🧠 Machine Learning Prediction Models
- ⚙️ Flask REST API Backend
- 🗄️ MySQL Database Integration
- 📊 Power BI Real-Time Visualizations
- 📈 Dynamic Dashboard Analytics

---

# 🚨 Problem Statement

Hospitals often face challenges in identifying critically unstable patients early enough for effective intervention.

Traditional monitoring systems:
- lack predictive intelligence
- cannot provide automated risk analysis
- do not visualize healthcare analytics efficiently

CareSense AI solves this by using Machine Learning models trained on healthcare datasets to provide intelligent clinical predictions and live dashboard analytics.

---

# 🎯 Project Objectives

- Predict emergency severity levels
- Detect ICU admission requirements
- Estimate patient readmission probability
- Store patient healthcare records dynamically
- Visualize healthcare insights using Power BI
- Build an intelligent AI healthcare dashboard

---

# 🧠 AI Features

## ✅ Emergency Risk Prediction
Predicts whether a patient condition is:
- Low Risk
- Moderate Risk
- High Risk

---

## ✅ ICU Admission Prediction
Determines if ICU admission may be required based on:
- Vitals
- Oxygen level
- Blood pressure
- Respiratory indicators

---

## ✅ Readmission Probability
Calculates the probability of patient readmission using AI classification models.

---

# 🏗️ System Architecture

```text
Frontend Dashboard
        ↓
Flask API Backend
        ↓
Machine Learning Models
        ↓
MySQL Database
        ↓
Power BI Dashboard Visualizations
```

---

# 💻 Technologies Used

## 🌐 Frontend
- HTML5
- CSS3
- JavaScript
- Font Awesome
- Responsive UI Design

---

## ⚙️ Backend
- Python
- Flask
- Flask-CORS

---

## 🧠 Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Joblib

---

## 🗄️ Database
- MySQL
- MySQL Workbench

---

## 📊 Visualization
- Microsoft Power BI

---

# 🧪 Clinical Parameters Used

The AI system analyzes:

| Parameter | Description |
|---|---|
| HR | Heart Rate |
| BP_Systolic | Systolic Blood Pressure |
| BP_Diastolic | Diastolic Blood Pressure |
| Temp | Body Temperature |
| SpO2 | Oxygen Saturation |
| RR | Respiratory Rate |
| Age | Patient Age |
| Stay | Hospital Stay Duration |
| PrevAdm | Previous Admissions |

---

# 🤖 Machine Learning Models

The project contains three trained AI models:

| Model | Purpose |
|---|---|
| emergency_model.joblib | Emergency Risk Prediction |
| icu_model.joblib | ICU Admission Prediction |
| readmission_model.joblib | Readmission Probability |

A scaler model is also used:

```text
scaler.joblib
```

---

# 🗄️ Database Features

The system dynamically stores:

✅ Patient Details  
✅ Clinical Vitals  
✅ AI Prediction Results  
✅ ICU Recommendations  
✅ Readmission Probabilities  

New entries are automatically added into the database and reflected inside Power BI dashboards.

---

# 📊 Power BI Dashboard Features

The Power BI dashboard provides:

✅ Total Patients Analytics  
✅ High Risk Case Monitoring  
✅ Emergency Distribution  
✅ Readmission Insights  
✅ Live Database Visualization  
✅ Dynamic Healthcare Reporting  

---

# 🌟 Frontend Features

- Modern Medical Dashboard UI
- AI Clinical Assessment Reports
- Real-Time Prediction Display
- Responsive Design
- Animated Medical Interface
- PDF Report Download
- AI Doctor Remarks
- Interactive Healthcare Cards

---

# 📁 Repository Includes

## 📄 Source Files
- `app.py`
- `FrontEnd.html`

---

## 🧠 AI Models
- `emergency_model.joblib`
- `icu_model.joblib`
- `readmission_model.joblib`
- `scaler.joblib`

---

## 📓 Notebook
- `CareSense_Ai_Model_Training.ipynb`

---

## 🗄️ Dataset
- `Master_Healthcare_Dataset.csv`

---

## 📊 Power BI
- `caresense_Ai.pbix`

---

## 🎥 Demo Files
- `Backend Code.mp4`
- `CareSense_AI-PowerBi Dashboard.mp4`

---

## 🖼️ Screenshots
- `CareSense_AI-FrontEnd.png`

---

## 📄 Documentation
- `Healthcare Prediction Project Documentation.pdf`

---

## ⚙️ Dependencies
- `requirements.txt`

---

# 🚀 How To Run The Project

## 1️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

## 2️⃣ Start MySQL Server

Ensure MySQL Workbench/XAMPP MySQL service is running.

---

## 3️⃣ Run Flask Backend

```bash
python app.py
```

Backend runs on:

```text
http://127.0.0.1:5000
```

---

## 4️⃣ Open Frontend

Open:

```text
FrontEnd.html
```

inside your browser.

---

## 5️⃣ Run Power BI Dashboard

Open:

```text
caresense_Ai.pbix
```

Then click:

```text
Home → Refresh
```

to fetch latest database records.

---

# 🔄 Real-Time Workflow

```text
Patient Inputs Data
        ↓
Frontend Sends Request
        ↓
Flask Backend Processes Data
        ↓
AI Models Generate Predictions
        ↓
Results Stored In MySQL
        ↓
Power BI Fetches Updated Records
        ↓
Dashboard Visualizations Update
```

---

# 📈 Future Improvements

- User Authentication
- Doctor Login System
- Cloud Deployment
- Live IoT Patient Monitoring
- SMS/Email Alerts
- Advanced AI Models
- Real-Time Hospital Integration
- Multi-Hospital Analytics

---

# 👨‍💻 Developer

## Qazi Abubakar Siddiqui

BS Information Technology  
Bahria University Lahore Campus

---

# 📜 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository  
🍴 Fork the project  
📢 Share with others  

---

# 🏥 CareSense AI

> Intelligent Clinical Intelligence for Smarter Healthcare Decisions.
