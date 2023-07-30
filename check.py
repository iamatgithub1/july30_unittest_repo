import json
import os
print(os.getcwd())
print(os.getcwd() + "\data_source\org_hrm_test_data.json")
cwd = os.getcwd()
json_file_path = cwd + "\\data_source\\org_hrm_test_data.json"
with open(json_file_path) as json_file:
    data_dict2 = json.load(json_file)
password = data_dict2.get("login_credentials").get("correct_password")
print(password)
print(data_dict2.get("login_credentials").get("incorrect_password"))
print(data_dict2.get("employee_info"))
print(data_dict2.get("employee_info").get("f_name"))
