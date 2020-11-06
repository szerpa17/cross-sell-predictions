# import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
 

# #################################################
# # Database Setup
# #################################################
engine = create_engine("Output/sqlite:///insurance_data.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
test_data = Base.classes.test_data
orig_test_vals = Base.classes.original_test_data_vals

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
        f"/api/v1.0/passengers"
    )


@app.route("/api/v1.0/testing_data")
def names():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all test_data
    results = session.query(test_data.name).all()

    session.close()

    # # Convert list of tuples into normal list
    all_test_data = list(np.ravel(results))

    return jsonify(all_test_data)


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
