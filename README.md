# 🛡️ Spam Email Classifier

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)

A professional, lightweight, and native Linux spam detection tool. Built with **Python** and **Scikit-learn**, it utilizes a **Multinomial Naive Bayes** classifier to identify spam messages with high precision.

---

## ✨ Features

- 🧠 **AI-Powered**: Uses advanced machine learning (Naive Bayes) for accurate text classification.
- 🐧 **Native Linux UI**: Uses `zenity` for sleek, system-integrated input and alert dialogs.
- 🚀 **Fast & Efficient**: Minimal dependencies and optimized pipeline-based processing.
- 📦 **Zero Config**: Automatically downloads and prepares the dataset on the first run.

## 🛠️ Requirements

- **Python 3.x**
- **Zenity** (Standard on most Linux distributions like Ubuntu, Fedora, Debian)

## 🚀 Quick Start

### 1. Clone & Enter
```bash
git clone git@github.com:KhizardoingProgramming/spam-email-classifier.git
cd spam-email-classifier
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Detector
```bash
python spam_classifier.py
```

## 📊 How it Works

The system uses a `CountVectorizer` to transform email text into a frequency matrix, which is then fed into a `MultinomialNB` model. This classic ML approach is exceptionally effective for text-based spam detection.

## 📁 Project Structure

- `spam_classifier.py`: The main application logic and UI.
- `requirements.txt`: Project dependencies.
- `spam.csv`: The SMS Spam Collection dataset (auto-downloaded).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
*Created by [KhizardoingProgramming](https://github.com/KhizardoingProgramming)*
