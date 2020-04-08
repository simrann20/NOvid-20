import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
ml = pickle.load(open('ml.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = ml.predict(final_features)

    result = prediction[0]

    if (result==1):
        output = 'You do not have CoronaVirus'
    else :
         output = 'You do have Coronavirus'

    return render_template('index.html', prediction_text='{}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = ml.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)