# Malayalam Movie Review Sentiment Analysis 🎬

This is a Flask web application that performs sentiment analysis on Malayalam movie reviews. The system predicts whether a given movie review is **positive** or **negative** based on the text provided by the user. The System Works on Support Vector Machine.

Dataset used:[Dataset](https://www.sciencedirect.com/science/article/pii/S2352340923005528?via%3Dihub)

## Features
- Accepts input in Malayalam language for movie reviews.
- Predicts the sentiment as Positive or Negative.
- Includes a user-friendly interface.
## Technologies Used
- **Machine Learning**: Support Vector Machine (SVM), TF-IDF Vectorization
- **Frontend**: HTML, CSS, Bootstrap
- **Libraries**: `joblib`, `sklearn`, `numpy`,`pandas`,`matplotlib`
- **Framework**: Flask

## How It Works
1. The user inputs a Malayalam movie review in the text area.
2. The system detects whether the input is in Malayalam or another language.
3. If the input is in Malayalam, the text is vectorized using **TF-IDF**, and sentiment analysis is performed using a pre-trained **SVM model**.
4. The predicted sentiment (**Positive** or **Negative**) is then displayed to the user.

