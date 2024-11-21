import zenoh,time

custom_config = zenoh.Config.from_file("config.json")

if __name__ == "__main__":
  zenoh.init_log_from_env_or("debug")
  session = zenoh.open(config=custom_config)
  key = 'zxdata/display1'
  key2 = 'zxdata/display2'
  pub = session.declare_publisher(key)
  pub2 = session.declare_publisher(key2)

  count = 0
  while True:
    command = input("For brakes, press 1, for lights press 2: ")
    if command.isdigit() and int(command) == 1:
      print(f"Sending braking command ...")
    if command.isdigit() and int(command) == 2:
      print(f"Sending lights command ...")
    pub.put("commmand" + str(command))
    time.sleep(0.1)
