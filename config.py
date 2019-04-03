import toolkit_config

config, profile = toolkit_config.read_config()

def read_profile(profile):
    configDictList = []
    for k, v in profile.items():
        configDictList.append({v['TITLE']: v['TEXT']})
    return configDictList


def query_profile(profile, key):
    for i in profile:
        for k, v in i.items():
            if k == key:
                return v

sleepTime = float(config['SLEEP_TIME'])
interval = float(config['KEY_PRESS_INTERVAL'])
maxWordCount = int(config['MAX_TEXT_COUNT'])
file_mode_src_file = config['FILE_MODE_SRC_FILE']

profile = read_profile(profile)



print(profile)
# print([list(i.keys())[0] for i in profile])
print(query_profile(profile, 'name'))