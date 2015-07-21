class Archiver(object):
    def __init__(self, basedir):
        self.__basedir = basedir
    def path(self, user, service_name):
        return os.path.join(self.__basedir, user, service_name)
    def ensure_basedir(self):
        if not os.path.exists(self.__basedir):
            os.makedirs(self.__basedir)
    @property
    def basedir(self):
        return self.__basedir
