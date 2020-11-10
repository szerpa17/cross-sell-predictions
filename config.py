import os

if os.getenv("DATABASE_URL"):
    cxnstring = os.environ["CXNSTRING"]
else:
    cxnstring = os.path.join('Database', 'insurance_data.sqlite')