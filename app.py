# import numpy as np

from flask import Flask, jsonify, render_template
import os
import sqlite3
import joblib
from sklearn.neighbors import KNeighborsClassifier
from config import cxnstring

# #################################################
# # Database Setup
# #################################################
# insurance_info = os.path.join('Database', 'insurance_data.sqlite')


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','') or 'sqlite:///db.insurance_data'

#################################################
# Flask Routes
#################################################

@app.route("/")
def home_page():
    # """List all available api routes."""
    # return (
    #     f"Available Routes:<br/>"
    #     f"/api/v1.0/testing_data<br/>"
    #     f"/api/v1.0/original_testing_data"
    # )

    return render_template("layout.html")

# Route returns all cleaned test data
@app.route("/api/v1.0/testing_data")
def testing_data():
    # conn = sqlite3.connect(app)
    conn = sqlite3.connect(cxnstring)

    # Create our session (link) from Python to the DB
    test_data = conn.execute("SELECT * FROM test_data;")

    """Return a list"""
    test_data_array = []

    for row in test_data:
        test_data_array.append({'id': row[0],
                                'gender': row[1],
                                'age': row[2],
                                'driving license': row[3],
                                'region code': row[4],
                                'previously insured': row[5],
                                'vehicle age': row[6],
                                'vehicle damage': row[7],
                                'annual premium': row[8],
                                'policy sales_channel': row[9],
                                'vintage': row[10]})

    conn.close

    return jsonify(test_data_array)

# Route returns all pre-cleaned test data
@app.route("/api/v1.0/original_testing_data")
def original_test_data():
    conn = sqlite3.connect(cxnstring)

    # Create our session (link) from Python to the DB
    test_data = conn.execute("SELECT * FROM original_test_data_vals;")

    """Return a list"""
    test_data_array = []

    for row in test_data:
        test_data_array.append({'id': row[0],
                                'gender': row[1],
                                'age': row[2],
                                'driving license': row[3],
                                'region code': row[4],
                                'previously insured': row[5],
                                'vehicle age': row[6],
                                'vehicle damage': row[7],
                                'annual premium': row[8],
                                'policy sales_channel': row[9],
                                'vintage': row[10]})

    conn.close

    return jsonify(test_data_array)

# Route returns test data for a specific customer ID
@app.route("/api/v1.0/<customer_id>")
def user_specific_data(customer_id):
    # Transform input to int
    c_id = int(customer_id)

    conn = sqlite3.connect(cxnstring)

    # Create our session (link) from Python to the DB
    test_data = conn.execute(
        f"SELECT * FROM original_test_data_vals WHERE id = {c_id};")

    """Return a list"""
    customer_data = []

    for row in test_data:
        customer_data.append({'id': row[0],
                              'gender': row[1],
                              'age': row[2],
                              'driving license': row[3],
                              'region code': row[4],
                              'previously insured': row[5],
                              'vehicle age': row[6],
                              'vehicle damage': row[7],
                              'annual premium': row[8],
                              'policy sales channel': row[9],
                              'vintage': row[10]})

    conn.close

    return jsonify(customer_data)

# Route returns prediction for a specific customer ID
@app.route("/api/v1.0/prediction/<customer_id>")
def customer_prediction(customer_id):
    # Transform input to int
    try:
        c_id = int(customer_id)

        conn = sqlite3.connect(cxnstring)

        # Create our session (link) from Python to the DB
        test_data = conn.execute(
            f"SELECT * FROM test_data WHERE id = {c_id};")

        """Return a list"""
        customer_test_data = []

        for row in test_data:
                customer_test_data = [row[1],
                                    row[2],
                                    row[3],
                                    row[4],
                                    row[5],
                                    row[6],
                                    row[7],
                                    row[8],
                                    row[9],
                                    row[10]]

        conn.close

        # Load the model from the file
        knn_from_joblib = joblib.load('Model/recommender_model.pkl')

        x_test = customer_test_data
        # x_test = customer_test_data.reshape(-1, 1)

        # Use the loaded model to make predictions
        prediction = knn_from_joblib.predict([x_test])

        result = ''
        if (prediction[0]).tolist() == 0:
            result = 'Customer is not interested in purchasing car insurance.'
        else:
            result = 'Customer is interested in purchasing car insurance.'

        return {'customer ID': c_id,
                'prediction': result}

    except ValueError:
        return {'ID Value Error': 'ID not found in test data',
                'Next Steps': 'Please enter an ID value that ranges from 381110 to 508146'}

# Route returns prediction for user inputted values
@app.route("/api/v1.0/user_prediction/<val_1>-<val_2>-<val_3>-<val_4>-<val_5>-<val_6>-<val_7>-<val_8>-<val_9>-<val_10>")
def user_prediction(val_1, val_2, val_3, val_4, val_5, val_6, val_7, val_8, val_9, val_10):
    # Transform input to int
    try:
        gender = int(val_1)
        age = int(val_2)
        driving_license = int(val_3)
        region_code = float(val_4)
        previously_insured = int(val_5)
        vehicle_age = int(val_6)
        vehicle_damage = int(val_7)
        annual_premium = float(val_8)
        policy_sales_channel = float(val_9)
        vintage = int(val_10)

        """Create a list"""
        user_test_data = []

        user_test_data = [gender,
                    age,
                    driving_license,
                    region_code,
                    previously_insured,
                    vehicle_age,
                    vehicle_damage,
                    annual_premium,
                    policy_sales_channel,
                    vintage]

        # Load the model from the file
        knn_from_joblib = joblib.load('Model/recommender_model.pkl')

        x_test = user_test_data

        # Use the loaded model to make predictions
        prediction = knn_from_joblib.predict([x_test])

        result = ''
        if (prediction[0]).tolist() == 0:
            result = 'Customer not interested'
        else:
            result = 'Customer is interested'

        return {'prediction': result}

    except ValueError:
        return {'Data type entry error': 'Values entered were not recognized',
                'Accepted values': {'gender' : 'Male: 0, Female: 1',
                                    'age' : "Number value representing the customer's age",
                                    'drivers license' : 'Customer does not have DL: 0, Customer already has DL: 1',
                                    'region code' : "Number value representing the customer's region" ,
                                    'previously insured' : "Customer doesn't have Car Insurance: 0, Customer already has Car Insurance: 1",
                                    'vehicle age' : "Number value representing the customer's car age",
                                    'vehicle damage' : "Customer didn't get his/her vehicle damaged in the past: 0, Customer got his/her vehicle damaged in the past.: 1",
                                    'annual premium' : "The amount customer needs to pay as premium in the year",
                                    'policy sales channel' : "Anonymized Code for the channel of outreaching to the customer ie. Different Agents, Over Mail, Over Phone, In Person, etc.",
                                    'vintage' : 'Number of Days customer has been associated with the company'}}


if __name__ == '__main__':
    app.run(debug=True)
