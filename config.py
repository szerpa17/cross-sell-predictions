import os
cxnstring = ""

if os.getenv("DATABASE_URL"):
    cxnstring = os.environ["CXNSTRING"]
else:
    cxnstring = os.path.join("Database","insurance_data.sqlite")
# cxnstring = os.path.join('Database', 'insurance_data.sqlite')