import  requests

target_url ="http://192.168.187.134/dvwa/login.php"
data_dict = {"username": "admin", "password": "password", "Login": "submit"}
response = requests.post(target_url, data=data_dict)
print(response.content)
