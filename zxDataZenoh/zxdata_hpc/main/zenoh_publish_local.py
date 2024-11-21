import zenoh
custom_config = zenoh.Config.from_file("config.json")

with zenoh.open(config=custom_config) as session:
  for response in session.get('demo/example/**'):
    response = response.ok
    print(f"{response.key_expr} => {response.payload}")
