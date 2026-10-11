import pandas as pd

data = {
    " User ID ": ["101","102","103","101","104","105"],
    " Full Name ": [
        " John Doe ",
        " jane smith ",
        "NULL",
        " John Doe ",
        " Alice ",
        "Bob",
    ],
    " Signup Date ": [
        "2026/01/15",
        "15-02-2026",
        "invalid_date",
        "2026/01/15",
        "2026-03-01",
        "None",
    ],
    "Status": [" ACTIVE ", "active", "pending", " ACTIVE ", "INACTIVE", "active"],
}

df = pd.DataFrame(data)
df.to_csv("raw_sample.csv", index=False)
print("Created 'raw_sample.csv' for testing.")