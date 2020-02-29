class Course:
    def __init__(self, data):
        self.dir = data['dir']
        self.name = data['name']
        self.prof = data['prof']
        self.params = []
        for param in data['params']:
            self.params.append(data[param])
        self.dates = data['dates']
