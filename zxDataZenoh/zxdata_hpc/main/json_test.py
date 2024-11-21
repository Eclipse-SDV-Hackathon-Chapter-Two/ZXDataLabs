import json

zxdata = "{\"command\": \"move\", \"data\":\"test\"}"

parsed_data = json.loads(zxdata)
print(parsed_data)
if parsed_data['command'] == "move":
  print("Moving ...")
