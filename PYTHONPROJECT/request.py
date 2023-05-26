import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()

#print(json)


with open('dollar.txt', mode="w") as file:
    file.write(str(json))

dollar_spam = open('dollar.txt' , 'r')
print(dollar_spam.read())
dollar_spam.close()
