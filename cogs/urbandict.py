import requests
import json


url="https://mashape-community-urban-dictionary.p.rapidapi.com/define"

x=input("Enter term : ")

querystring={"term":f"{x}"}

headers = {
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
    'x-rapidapi-key': "4506e5dc85msh57cad0977206ed3p1e19e7jsn0f0af8f6be4e"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)

def definition(m):
    for i in range (0,m):
     d=data['list'][m]['definition'].replace('[','').replace(']','')
     print(d)
def example(n):
    d=data['list'][{n}]['example'].replace('[','').replace(']','')
    return(m)
if __name__ == "__main__":
    definition(3)
#print(data)
#print(data['list'][0]['definition'].replace('[','').replace(']',''))
#print(data['list'][1]['definition'].replace('[','').replace(']',''))
#print(data['list'][0]['example'].replace('[','').replace(']',''))
#print(data['list'][1]['example'].replace('[','').replace(']',''))