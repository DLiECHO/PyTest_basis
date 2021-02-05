class parents():
    def __init__(self,v1):
        self.v1 = v1

class son(parents):
    def __init__(self,v2):
        self.v2 = v2
        super().__init__(v2)

s = son(2)
print(s.v1)
print(s.v2)