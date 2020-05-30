import requests
import json


def device_login(deviceIP):
    login_url = f"https://{deviceIP}:4343/v1/api/login"
    with open("/Users/skilladi/Documents/PyCharm Projects/ArubaOS_Controller_Automation/src/config/credentials.json", "r") as f:
        credentials = json.loads(f.read())

    try:
        response = requests.post(login_url, verify=False, timeout=5,
                                 data=f"username={credentials['username']}&password={credentials['password']}")
        try:
            if response["_global_result"]["status"] == "1":
                print(response["_global_result"]["status_str"])
                return None
            elif response["_global_result"]["status"] == "0":
                print(response["_global_result"]["status_str"])
                return response["_global_result"]["UIDARUBA"]
            else:
                print("Unknown status of the login")
        except Exception as e:
            print(e)

    except Exception as e:
        print("Did not receive any response from the server. Please check the reachability")
        print(e)
        return None


def device_logout(deviceIP, cookie):
    logout_url = f"https://{deviceIP}:4343/v1/api/logout"

    try:
        response = requests.post(logout_url, verify=False, timeout=5)
        return True

    except Exception as e:
        print("Did not receive any response from the server. Please check the reachability")
        print(e)
        return False

def getConfigOutput(deviceIP, url, cookie):
    cookie = dict(SESSION= cookie)
    getConfigUrl = "https//{deviceIP}:4343/v1/{url}"

    try:
        return requests.get(getConfigUrl, verify=False, cookies=cookie, timeout=5)
    except Exception as e:
        print("Did not receive any response from the server. Please check the reachability")
        print(e)
        return None