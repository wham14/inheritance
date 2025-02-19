class Dad:

    def __init__(self, color,dadhobby):
        self.color = color
        self.dadhobby = dadhobby

class Mum:
    def __init__(self, color, mumhobby):
        self.color = color
        self.mumhobby = mumhobby

class Boy(Dad):
    def boyinherit(self):
        print(f"Boys inherit {self.color} and {self.dadhobby}")

my_object = Boy("African descent","Watching football")
my_object.boyinherit()

class Girl(Mum):
    def girlinherit(self):
        print(f"Girls inherit {self.color} and {self.mumhobby}")
my_object = Girl("American descent","Dancing")
my_object.girlinherit()