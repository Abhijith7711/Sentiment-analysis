from flask import Flask, request, render_template
import joblib
import re

# Initialize Flask app
app = Flask(__name__)

# Load the vectorizer and model
loaded_vectorizer = joblib.load('tfidf_vectorizer.pkl')
loaded_model = joblib.load('best_svm_model.pkl')

# Define a function to check if the input is in Malayalam
def is_malayalam(text):
    # Regular expression to check for Malayalam characters
    malayalam_pattern = re.compile('[\u0D00-\u0D7F]+')  # Malayalam Unicode range
    return bool(malayalam_pattern.search(text))

# Define home route
@app.route('/')
def home():
    return render_template('index.html')

# Define route to handle predictions
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the review from the form
        new_review = request.form['review']

        # Check if the review is in Malayalam
        if not is_malayalam(new_review):
            error_message = "Please write in Malayalam."
            return render_template('index.html', error_message=error_message, review_text=new_review)

        # Vectorize the review
        new_review_tfidf = loaded_vectorizer.transform([new_review])

        # Predict sentiment
        prediction = loaded_model.predict(new_review_tfidf)

        # Determine sentiment
        sentiment = "Positive" if prediction[0] == 1 else "Negative"

        # Pass the review and prediction result to the frontend
        return render_template('index.html', prediction=sentiment, review_text=new_review)

if __name__ == "__main__":
    app.run(debug=True)
