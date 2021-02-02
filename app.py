
import numpy as np
import sklearn
from flask import Flask, render_template,request
import pickle#Initialize the flask App
app = Flask(__name__)
model = pickle.load(open('FitBitfinal.pickle', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')
#To use the predict button in our web-app


@app.route('/predict',methods=['POST'])
def predict():
    #For rendering results on HTML GUI
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text='The total calories burnt : {}'.format(output))



if __name__ == "__main__":
    app.run(debug=True)