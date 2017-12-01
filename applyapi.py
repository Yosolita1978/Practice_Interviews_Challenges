import requests
import json

URL = "https://contact.plaid.com/jobs"

resume = "https://docs.google.com/document/d/14RnFmA-boPkvC_rZW3hmxUJFJLFq-NwEObbjvRjK978/edit?usp=sharing"

links = ["https://www.linkedin.com/in/crissrodriguez/", "http://yosola.co/", "https://github.com/Yosolita1978", "https://twitter.com/yosola"]

cristina = {'name': "Cristina Rodriguez", 'email': "yosola@gmail.com", 'resume': resume, 'links': links}



r = requests.post(URL, json=cristina)
print (r.text)