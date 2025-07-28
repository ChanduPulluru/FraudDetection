# 💳 Payment Fraud Detection System using ML & Flask

This project implements a **Machine Learning-based fraud detection system** using Python. It detects suspicious or fraudulent transactions and serves the predictions through a **Flask-based web API** and **interactive frontend**.

> 🔍 **Goal**: Classify transactions as "Fraudulent" or "Genuine" using supervised ML techniques.

---

## 🚀 Features

- 🧠 Machine Learning model training (Logistic Regression / LGBM)
- 📊 Exploratory Data Analysis & visualization in Jupyter Notebook
- 🔧 Flask backend to serve ML predictions via API
- 🖥️ HTML/CSS web interface for user interaction
- 📁 Modular folder structure for scalability
- ✅ Live model inference on new data

---

## 🧠 Tech Stack

| Layer           | Tools/Tech Used                      |
|----------------|---------------------------------------|
| Language        | Python                               |
| ML Libraries    | Scikit-learn, LightGBM, Pandas, NumPy|
| Visualization   | Matplotlib, Seaborn                  |
| Frontend        | HTML, CSS                            |
| Backend         | Flask                                |
| Notebook        | Jupyter (.ipynb)                     |

- **Deployment**: Locally hosted via `localhost:5000`
---

## 🗂️ Project Structure
├── Data/ # Dataset files
│ └── [Your dataset.csv]
│
├── training/ # Jupyter Notebooks for EDA, modeling
│ ├── fraud_detection_model.ipynb
│ └── model_utils.py
│
├── training_lbm/ # LightGBM-based alternate training
│ └── [models, notebooks]
│
├── Flask/ # Backend Flask API
│ ├── app.py # Main server
│ ├── model.pkl # Trained ML model
│ ├── templates/
│ │ └── index.html # Frontend UI
│ └── static/
│ └── style.css # Frontend CSS
│
├── README.md # Project documentation


---

## 🚀 How to Run the Project Locally

### ✅ Step 1: Clone the repository
'''bash
git clone https://github.com/ChanduPulluru/FraudDetection.git
cd FraudDetection

### ✅ Step 2: 
python -m venv venv
source venv/bin/activate    

### ✅ Step 3
cd Flask
python app.py

### ✅ Step 4: Open your browser
Visit http://localhost:5000 to test the fraud detection form!

## 🙋‍♂️ Author

**Chandu Pulluru**  
📍 VIT-AP University  
🔗 [LinkedIn](https://www.linkedin.com/in/chandu-pulluru-92249728b/)
