
from jClass import jClass

class ClassFileLoader():

    @staticmethod
    def load(fPath):
        with open(fPath,'rb') as f:
            return jClass(f.read())