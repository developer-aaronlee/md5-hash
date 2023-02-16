import hashlib
from pandas import *

file = read_csv("text_email.csv")
emails = file["user_id"].tolist()
hashed_emails = [hashlib.md5(x.encode()).hexdigest() for x in emails]

df = DataFrame({"hashed_email": hashed_emails})
df.to_csv("md5_encoded.csv", index=False)
