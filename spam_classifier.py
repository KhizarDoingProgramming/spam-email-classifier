import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import subprocess, os, urllib.request

def prompt(text):
    res = subprocess.run(["zenity", "--entry", "--title=Spam Detector", f"--text={text}", "--width=400"], 
                         capture_output=True, text=True)
    return res.stdout.strip()

def alert(msg, icon="info"):
    subprocess.run(["zenity", f"--{icon}", "--title=Analysis Result", f"--text={msg}", "--width=400"])

def main():
    data_file = "spam.csv"
    if not os.path.exists(data_file):
        url = "https://raw.githubusercontent.com/mohitgupta-1O1/Kaggle-SMS-Spam-Collection-Dataset-/master/spam.csv"
        urllib.request.urlretrieve(url, data_file)

    df = pd.read_csv(data_file, encoding='latin-1')[['v1', 'v2']]
    
    model = make_pipeline(CountVectorizer(stop_words='english'), MultinomialNB())
    model.fit(df['v2'], df['v1'])

    while True:
        user_input = prompt("Enter the email/message content to scan:")
        if not user_input: 
            break
            
        prediction = model.predict([user_input])[0]
        confidence = np.max(model.predict_proba([user_input])) * 100
        
        icon = "info" if prediction == "ham" else "warning"
        status = "SAFE (HAM)" if prediction == "ham" else "SPAM DETECTED"
        
        alert(f"RESULT: {status}\nConfidence: {confidence:.2f}%", icon=icon)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
