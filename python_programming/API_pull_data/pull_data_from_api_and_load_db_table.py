import requests
import json
import cx_Oracle
response_API = requests.get('https://api.covid19india.org/state_district_wise.json')
#print(response_API.status_code)
data = response_API.text
parse_json = json.loads(data)
active_case = parse_json['Andaman and Nicobar Islands']['districtData']['South Andaman']['active']
print("Active cases in South Andaman:", active_case)

'''
conn = cx_Oracle.connect('username/pswd@host:port/servicename')
c = conn.cursor()
c.execute('INSERT INTO json_to_oracle("1","2","3")')
conn.commit()
c.close()
conn.close() 

'''
