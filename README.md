# Spam Email Classifier

A lightweight, native Linux spam detection tool built with Python and Scikit-learn. It uses a Naive Bayes classifier to identify spam messages and provides a simple GUI using Zenity.

## Features
- Naive Bayes model for high-accuracy text classification.
- Pipeline-based text processing and vectorization.
- Native Linux dialogs for input and alerts.
- Automatic dataset downloading.

## Requirements
- Python 3.x
- `zenity` (usually pre-installed on Linux)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/spam-email-classifier.git
   cd spam-email-classifier
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the script using Python:
```bash
python spam_classifier.py
```

## Dataset
The project uses the SMS Spam Collection Dataset. It will be automatically downloaded on the first run if it's not present.
