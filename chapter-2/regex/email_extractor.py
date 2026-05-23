import re

text = """
Contact emails:
sushant@gmail.com
admin@yahoo.com
test@proton.me
"""

emails = re.findall(r"\S+@\S+", text)

print("Emails found:")

for email in emails:
    print(email)
