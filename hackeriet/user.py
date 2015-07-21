import os

class UsersRoot(object):
    def __init__(self, basepath):
        self.__basepath = basepath
    def user(self, name):
        return User(self.__basepath, name)
    def all(self):
        bp = self.__basepath
        for x in os.listdir(bp):
            user_dir = os.path.join(bp, x)
            if os.path.isdir(user_dir):
                yield User(user_dir, x)

class User(object):
    def __init__(self, basepath, name):
        self.__basepath = basepath
        self.__name = name
    @property
    def name(self):
        return self.__name
    def fullpath(self, path):
        return os.path.join(self.__basepath, path)
    def path_exists(self, path):
        return os.path.exists(os.path.join(self.__basepath, path))
    def ensure_dir(self, path):
        fullpath = os.path.join(self.__basepath, path)
        if not os.path.exists(fullpath):
            os.makedirs(fullpath)
    def listdir(self, path):
        return os.listdir(os.path.join(self.__basepath, path))

def root(basepath):
    return UsersRoot(basepath)
