import os

cxnstring = ""

if os.getenv("DATABASE_URL"):
    cxnstring = os.environ["CXNSTRING"]
else:
    cxnstring = os.path.join("insurance_data.sqlite")