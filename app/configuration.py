def getConfigValue(key, default=None):
    '''get config value or return default'''
    try:
        import config
        return getattr(config, key)
    except BaseException:
        return default
