import cle

class Project:
    
    loader: cle.Loader
    def __init__(self, filename):
        self.filename = filename
        self.loader = cle.Loader(filename)