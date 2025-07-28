from flask import Flask, render_template, request
import numpy as np
import pickle
import pandas as pd

# Load your trained ML model
model = pickle.load(open('payments.pkl', 'rb'))
app = Flask(__name__)

# Home route
@app.route('/')
def about():
    return render_template('index.html')

@app.route('/home')
def about1():
    return render_template('index.html')


# Show prediction form
@app.route("/predict")
def home1():
    return render_template('predict.html')

# Handle prediction
@app.route("/pred", methods=['POST', 'GET'])
def predict():
    try:
        x = [[x for x in request.form.values()]]
        print("Raw input list:", x)

        x = np.array(x)
        print("Input shape:", x.shape)
        print("Numpy array:", x)

        pred = model.predict(x)
        print("Prediction result:", pred[0])

        return render_template('submit.html', prediction_text=str(pred))

    except Exception as e:
        return render_template('submit.html', prediction_text=f"Error: {str(e)}")


if __name__ == '__main__':
    app.run(debug=True)
