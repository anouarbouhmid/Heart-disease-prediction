#Install Libraries
from flask import Flask, request, jsonify
import traceback, pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler,QuantileTransformer

import numpy as np
app = Flask('prediction')

@app.route('/prediction', methods=['POST'])
def predict_cancer():
    if lr:
        try:
            json_ = request.json
            print(json_)
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=rnd_columns, fill_value=0)
            predict = list(lr.predict(QuantileTransformer().fit_transform(query)))
            return jsonify({'prediction': str(predict)})
        except:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Model not good')
        return ('Model is not good')


if __name__ == '__main__':
    port = 2222 
    lr = pickle.load(open('randomfs.pkl','rb'))
    print ('Model loaded')
    rnd_columns = pickle.load(open('rnd_columns.pkl','rb'))
    print ('Model columns loaded')
    app.run(port=port, debug=True)
	