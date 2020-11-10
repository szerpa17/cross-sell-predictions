import os

if os.getenv("DATABASE_URL"):
    cxstring = os.environ["CXNSTRING"]
else:
    cxnstring = os.path.join('Database', 'insurance_data.sqlite')