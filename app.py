from flask import Flask, request, url_for, render_template, redirect, jsonify
import pandas as pd

app = Flask(__name__)


@app.route("/")
def index():
    #Home page
    return render_template("index.html")

@app.route("/predict")
def predict():
    return render_template("predict.html")

@app.route('/predictinput', methods = ['POST'])
def predictinput():
    features = [x for x in request.form.values()]
    pred = features[0]
    model_used = features[-1]
    return render_template('predict.html',prediction='Expected PER will be {} using {}'.format(pred, model_used))

if __name__ == "__main__":
    app.run(debug=True)