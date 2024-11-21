import zenoh, time

def listener(sample):
  print(f"Received {sample.kind} ('{sample.key_expr}': '{sample.payload.to_string()}')")

custom_config = zenoh.Config.from_file("config.json")

if __name__ == "__main__":
  zenoh.init_log_from_env_or("debug")
  session = zenoh.open(config=custom_config)
  sub = session.declare_subscriber('demo/example/zenoh-rs-pub', listener)
  time.sleep(60)
