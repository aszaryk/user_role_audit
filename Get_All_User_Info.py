import sys
import csv
import requests
import xml.etree.ElementTree as ET
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC
from veracode_api_py import VeracodeAPI



def getUserInfo():
    user_type="api"
    user_list = VeracodeAPI().get_users()
    



    for g in range(len(user_list)):
        user_info = VeracodeAPI().get_user(user_list[g]["user_id"])

        for u in range(len(user_info["permissions"])):

            if (format(user_info["permissions"][u]["permission_name"])) == "apiUser":
                csvdata = ("{} | {} | {} | {} | {}".format(user_info["user_id"],user_info["user_name"],user_info["permissions"][u]["permission_name"], user_info["active"], user_info["login_enabled"]))
                
                if user_info["ip_restricted"] == True:
                    csvdata += (" | {}".format(user_info["allowed_ip_addresses"]))
                print (csvdata)
                f = open("csv-user-info.csv", "a", newline='')
                f.write(csvdata+"\n")
                f.close()
 

def main():

    with open('csv-user-info.csv', mode='w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=['User ID | User Name | Account Type | Active | Login Enabled | Allowed IP Addresses'])
        csv_writer.writeheader()
    getUserInfo()


if __name__ == "__main__":
    main()