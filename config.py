import toolkit_config

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


try:
    config, profile = toolkit_config.read_config()
    sleepTime = float(config['SLEEP_TIME'])
    interval = float(config['KEY_PRESS_INTERVAL'])
    maxWordCount = int(config['MAX_TEXT_COUNT'])
    file_mode_src_file = config['FILE_MODE_SRC_FILE']

    profile = read_profile(profile)
except Exception as e:
    with open('config_sample.ini') as f, open('config.ini', 'w') as conf:
        tmpl = f.read()
        conf.write(tmpl)
    config, profile = toolkit_config.read_config()
    sleepTime = float(config['SLEEP_TIME'])
    interval = float(config['KEY_PRESS_INTERVAL'])
    maxWordCount = int(config['MAX_TEXT_COUNT'])
    file_mode_src_file = config['FILE_MODE_SRC_FILE']

    profile = read_profile(profile)

