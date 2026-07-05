# 💳 Credit Card Fraud Detection

## 📌 Project Overview

This project is a Machine Learning-based Credit Card Fraud Detection system developed using Python and Scikit-learn. It classifies transactions as either **Legitimate** or **Fraudulent** using a Random Forest Classifier.

The project demonstrates the complete machine learning workflow, including data generation, preprocessing, model training, evaluation, and prediction.

---

## 🚀 Features

- Generate a synthetic credit card transaction dataset
- Data preprocessing and analysis
- Train a Random Forest Classifier
- Evaluate model performance
- Predict fraudulent transactions
- Save and load the trained model using Joblib
- Simple command-line interface for prediction

---

## 📂 Project Structure

```text
Credit_Card_Fraud_Detection/
│
├── dataset/
│   └── creditcard.csv
├── notebook.ipynb
├── train_model.py
├── predict.py
├── fraud_model.pkl
├── feature_names.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Jupyter Notebook

---

## 📦 Required Libraries

Install all required libraries using:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn joblib jupyter
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/abhinayac04-bot/Credit_Card_Fraud_Detection.git
```

### Move into the Project Folder

```bash
cd Credit_Card_Fraud_Detection
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Train the Machine Learning Model

```bash
python train_model.py
```

Example Output:

```text
Model Accuracy: 0.98

Classification Report

Confusion Matrix

Model saved successfully!
```

---

### Predict a Transaction

Run:

```bash
python predict.py
```

The program will ask you to enter 20 feature values.

Example:

```text
Feature_1: 0.5
Feature_2: -1.2
Feature_3: 0.8
...
Feature_20: -0.5
```

Output:

```text
✅ Legitimate Transaction
```

or

```text
🚨 Fraudulent Transaction
```

---

## 📊 Machine Learning Model

- Algorithm: Random Forest Classifier
- Classification Type: Binary Classification
- Features: 20
- Target Variable: Fraud
- Model Saving: Joblib

---

## 📁 Files Description

| File | Description |
|------|-------------|
| notebook.ipynb | Complete project implementation |
| train_model.py | Trains and saves the machine learning model |
| predict.py | Predicts whether a transaction is legitimate or fraudulent |
| fraud_model.pkl | Saved Random Forest model |
| feature_names.pkl | Stores feature names used during prediction |
| dataset/creditcard.csv | Dataset used for training |
| requirements.txt | Python dependencies |
| README.md | Project documentation |

---

## 📈 Sample Output

```text
Model Accuracy: 0.98

Confusion Matrix

[[1952    0]
 [  37   11]]

Model saved successfully!

✅ Legitimate Transaction
```

---

## 🎯 Internship Details

**Company Name:** CODTECH IT SOLUTIONS

**Intern Name:** Abhinaya C

**Intern ID:** CITS6459

**Domain:** Artificial Intelligence

**Project Title:** Credit Card Fraud Detection

**Task Number:** Task 3

---

## 📚 Learning Outcomes

- Data preprocessing using Pandas
- Machine Learning model training
- Binary classification
- Random Forest algorithm
- Model evaluation
- Confusion Matrix
- Classification Report
- Model serialization using Joblib
- Python project development

---

## 📜 License

This project is developed for educational and internship purposes under the CODTECH IT SOLUTIONS Internship Program.

---

## 👩‍💻 Author

**Abhinaya C**

B.Tech Information Technology Student

College of Engineering Thalassery

Intern ID: **CITS6459**