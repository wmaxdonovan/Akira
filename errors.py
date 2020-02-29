class InvalidSource(Exception):
    def __init(self, src):
        self.msg = 'INVALID SOURCE ERROR: the file, ' + src + ' does not exist.'
