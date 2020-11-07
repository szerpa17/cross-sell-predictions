# import numpy as np

from flask import Flask, jsonify, render_template
import os
import sqlite3
import joblib

# #################################################
# # Database Setup
# #################################################
insurance_info = os.path.join('Database', 'insurance_data.sqlite')


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


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

    return render_template("home/layout.html")


@app.route("/api/v1.0/testing_data")
def testing_data():
    conn = sqlite3.connect(insurance_info)

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


@app.route("/api/v1.0/original_testing_data")
def original_test_data():
    conn = sqlite3.connect(insurance_info)

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


@app.route("/api/v1.0/<customer_id>")
def user_specific_data(customer_id):
    # Transform input to int
    c_id = int(customer_id)

    conn = sqlite3.connect(insurance_info)

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
                              'policy sales_channel': row[9],
                              'vintage': row[10]})

    conn.close

    return jsonify(customer_data)


@app.route("/api/v1.0/prediction/<customer_id>")
def customer_prediction(customer_id):
    # Transform input to int
    c_id = int(customer_id)

    conn = sqlite3.connect(insurance_info)

    # Create our session (link) from Python to the DB
    test_data = conn.execute(
        f"SELECT * FROM test_data WHERE id = {c_id};")

    """Return a list"""
    customer_test_data = []

    for row in test_data:
        customer_test_data=[row[1],
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
    knn_from_joblib = joblib.load('recommender_model.pkl')

    x_test = customer_test_data
    # x_test = customer_test_data.reshape(-1, 1)

    # Use the loaded model to make predictions
    prediction = knn_from_joblib.predict([x_test])

    # return jsonify(prediction)
    # return jsonify(prediction)
    return {'prediction': (prediction[0]).tolist()}


if __name__ == '__main__':
    app.run(debug=True)
