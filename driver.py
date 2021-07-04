import requests


input_url = input("Enter the url,(https://www.example.com)")
res = requests.post( 
    url = 'http://localhost:5000/predict',
    json = {
        'url':input_url
    })
if(res.status_code == 200):
    print(res.json()['Category'])
elif(res.status_code>=500):
    print("Internal Server error")
else:
    print("Error")