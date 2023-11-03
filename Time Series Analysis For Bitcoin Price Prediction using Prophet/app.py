import numpy as пр
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
#flask app
app = Flask(__name__)
#loading the saved model
m = pickle.load(open('fbcrypto.pkl', 'rb'))
@app.route ('/', methods=['GET'])
def index () :
    return render_template ('index.html') #rendering html
@app.route ('/Bitcoin',methods=['POST', 'GET'])
def prediction(): # route which will take you to the prediction page
    return render_template ('index.html')
future = m. make_future_dataframe (periods = 365)
forecast = m. predict (future)
print(forecast)
@app.route('/predict',methods=['POST'])
def y_predict():
    if request.method == "POST":
        ds = request.form["Date"]
        print(ds)
        ds=str(ds)
        print(ds)
        next_day=ds
        print (next_day)
        prediction=forecast[forecast['ds'] == next_day]['yhat'].item()
        prediction=round (prediction, 2)
        print(prediction)
        return render_template( 'index.html', prediction_text="Bitcoin Price on selected date is $ {} Cents".format(prediction))
    return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True)
