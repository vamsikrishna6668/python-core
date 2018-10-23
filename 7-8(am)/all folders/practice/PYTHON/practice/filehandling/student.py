class college:
    def __init__(self, code, name):
        self.college_code=code
        self.college_name=name
    def __str__(self):
        return ('collegecode={},collegename={}'.format(self.college_code,self.college_name))
