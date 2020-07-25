import requests


d=requests.get('http://itsthisforthat.com/api.php?text')
print(d.text)