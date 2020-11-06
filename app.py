# import numpy as np

from flask import Flask, jsonify
import os
import sqlite3

# #################################################
# # Database Setup
# #################################################
insurance_info = os.path.join('Database','insurance_data.sqlite')


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/testing_data<br/>"
        # f"/api/v1.0/passengers"
    )


@app.route("/api/v1.0/testing_data")
def names():
    conn = sqlite3.connect(insurance_info)

    # Create our session (link) from Python to the DB
    test_data = conn.execute("SELECT * FROM test_data;")

    """Return a list"""
    # Query all test_data
    test_data_array = []

    for row in test_data:
            test_data_array.append({'id': row[0] , 
                                    'gender': row[1] ,
                                    'age': row[2],
                                    'driving license': row[3],
                                    'region code': row[4],
                                    'previously insured': row[5] ,
                                    'vehicle age': row[6],
                                    'vehicle damage': row[7],
                                    'annual premium': row[8],
                                    'policy sales_channel': row[9],
                                    'vintage': row[10] })

    conn.close

    return jsonify(test_data_array)


# @app.route("/api/v1.0/passengers")
# def passengers():
    # Create our session (link) from Python to the DB
    # session = Session(engine)

    # """Return a list of passenger data including the name, age, and sex of each passenger"""
    # # Query all passengers
    # results = session.query(Passenger.name, Passenger.age, Passenger.sex).all()

    # session.close()

    # # Create a dictionary from the row data and append to a list of all_passengers
    # all_passengers = []
    # for name, age, sex in results:
    #     passenger_dict = {}
    #     passenger_dict["name"] = name
    #     passenger_dict["age"] = age
    #     passenger_dict["sex"] = sex
    #     all_passengers.append(passenger_dict)

    # return jsonify(all_passengers)


if __name__ == '__main__':
    app.run(debug=True)
