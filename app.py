from flask import Flask, render_template, request
from flask_cors import CORS
import pickle
import numpy as np
import os
app = Flask(__name__)
CORS(app)
model = pickle.load(open('hr_rf_model.pkl', 'rb'))
# resource_path = os.path.join(app.root_path, '')


@app.route('/')
def begin():
    return render_template('main.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    # res = request.json
    # print(res.values())
    # print(type(res.values()))
    # print()
    # res = []
    # for i in JSONobject {
    #     res_array.push([i, JSONobject[i]])
    # }
    # int_features = [int(x) for x in res.values()]
    int_features = [int(x) for x in request.form.values()]
    # print(int_features)
    int_features[0] = int_features[0]/100
    if(int_features[-1] == 1):
        int_features.append(0)
        int_features.append(0)
    elif(int_features[-1] == 2):
        int_features[-1] = 0
        int_features.append(1)
        int_features.append(0)
    elif(int_features[-1] == 3):
        int_features[-1] = 0
        int_features.append(0)
        int_features.append(1)
    print(int_features)
    final = [np.array(int_features)]
    prediction = model.predict(final)
    if prediction == 1:
        result = "Employee is likely to leave the company."
    elif prediction == 0:
        result = "Employee is likely to continue working for company."
    return render_template('main.html', pred=result)


if __name__ == "__main__":
    app.run()
