import requests
import random

URL = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSfh4xiVkpZZ9pbiVuFwjFmwxBobhKZtdqIdjB81rbcSY6QuZw/formResponse'

def ruc():
    # Generate a random code point within the Unicode range
    # Unicode ranges can vary, so let's pick a common range for characters
    # You can adjust the range if you need characters from different sections
    random_code_point = random.randint(0x0000, 0x10FFFF)
    return chr(random_code_point)

while True:
    name: str = ruc + ruc + ruc
    job: str = ruc + ruc + ruc + ruc + ruc
    birth: int = random.randint(-2000, 2000)
    content: str = ruc + ruc + ruc + ruc + ruc + ruc + ruc + ruc + ruc + ruc + ruc + ruc + ruc + ruc + ruc + ruc + ruc + ruc + ruc + ruc + ruc + ruc + ruc + ruc + ruc + ruc + ruc + ruc + ruc + ruc + ruc + ruc + ruc + ruc + ruc

    DATA = {
	"entry.1458837562": name,
	"entry.114924327": job,
	"entry.877915436": str(birth),
	"entry.1190079061": content,
    }
    
    print(DATA)
    res = requests.post(URL, DATA)
    print(res.status_code, res.reason)

