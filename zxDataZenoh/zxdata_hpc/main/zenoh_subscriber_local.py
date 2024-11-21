import zenoh, time
def listener(sample):
  print(f"{sample.key_expr} => {sample.payload.decode('utf-8')}")

custom_config = zenoh.Config.from_file("config.json")

with zenoh.open(config=custom_config) as session:
  with session.declare_subscriber('demo/example/**', listener) as subscriber:
    time.sleep(60)
