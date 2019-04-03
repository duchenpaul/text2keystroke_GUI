import toolkit_config

config, profile = toolkit_config.read_config()
# keyboard = Controller()
# configDict = print_config()
# keyList = list(configDict.keys())

sleepTime = float(config['SLEEP_TIME'])
interval = float(config['KEY_PRESS_INTERVAL'])
maxWordCount = int(config['MAX_TEXT_COUNT'])
file_mode_src_file = config['FILE_MODE_SRC_FILE']