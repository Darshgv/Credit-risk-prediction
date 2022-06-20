#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 16:09:07 2022

@author: Darshu
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 14:56:07 2022

@author: Darshu
"""

from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)

pickle_in = open("logreg.pkl","rb")
logreg=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome to credit risk "

@app.route('/predict',methods=["Get"])
def predict_credit_risk_authentication1():
    
    """Let's predict the fault detection
    This is using docstrings for specifications.
    ---
    parameters:  
        - name: f1
          in: query
          type: number
          required: true
        - name: f2
          in: query
          type: number
          required: true
        - name: f3
          in: query
          type: number
          required: true
        - name: f4
          in: query
          type: number
          required: true
        - name: f5
          in: query
          type: number
          required: true
        - name: f6
          in: query
          type: number
          required: true
        - name: f6
          in: query
          type: number
          required: true
        - name: f7
          in: query
          type: number
          required: true
        - name: f8
          in: query
          type: number
          required: true
        - name: f9
          in: query
          type: number
          required: true
        - name: f10
          in: query
          type: number
          required: true
        - name: f11
          in: query
          type: number
          required: true
    responses:
        200:
            description: The output values
        
    """
    f1=request.args.get("f1")
    f2=request.args.get("f2")
    f3=request.args.get("f3")
    f4=request.args.get("f4")
    f5=request.args.get("f5")
    f6=request.args.get("f6")
    f7=request.args.get("f7")
    f8=request.args.get("f8")
    f9=request.args.get("f9")
    f10=request.args.get("f10")
    f11=request.args.get("f11")
   
    
    prediction=logreg.predict([[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11]])
    print(prediction)
    return "The prediction is "+str(prediction)

@app.route('/predict_file',methods=["POST"])
def predict_credit_risk_authentication2():
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    df_test=pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction=classifier.predict(df_test)
    
    return str(list(prediction))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8002)