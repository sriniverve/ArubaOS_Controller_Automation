import src.libs.deviceLib as dLib
import json
import os

f = open("/Users/skilladi/Documents/PyCharm Projects/ArubaOS_Controller_Automation/src/config/controller_details.json", "r")
ip_list = json.loads(f.read())

MM = ip_list[0]["MobilityMaster"]["IP"]
CONTROLLER1 = ip_list[1]["Controller1"]["IP"]
CONTROLLER2 = ip_list[2]["Controller2"]["IP"]
CONTROLLER3 = ip_list[3]["Controller3"]["IP"]
CONTROLLER4 = ip_list[4]["Controller4"]["IP"]
f.close()


def main():
    cookie = dLib.device_login(CONTROLLER1)
    if cookie is not None:
        get_vlan_url = f"configuration/object/vlan_name_id?config_path=%2Fmd&UIDARUBA={cookie}"
        vlan_config = getConfigOutput(CONTROLLER1, get_vlan_url, cookie)
        print(vlan_config)
        dLib.device_logout(CONTROLLER1)

if __name__ == '__main__':
    main()
