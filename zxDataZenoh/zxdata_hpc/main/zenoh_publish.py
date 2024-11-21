import zenoh

custom_config = zenoh.Config.from_file("config.json")

with zenoh.open(config=custom_config) as session:
  session.put('demo/example/hello', 'Hello World!')
