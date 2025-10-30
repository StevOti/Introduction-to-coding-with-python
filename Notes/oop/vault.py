class Vault:
    def __init__(self, galleons=0, sickels=0, knuts=0):
        self.galleons = galleons
        self.sickels = sickels
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickels} Sickels, {self.knuts} Knuts"
    
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickels = self.sickels + other.sickels
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickels, knuts)

potter = Vault(100, 50, 25)
print(potter)

weasly = Vault(25, 50, 100)
print(weasly)

galleons = potter.galleons + weasly.galleons
sickels = potter.sickels + weasly.sickels
knuts = potter.knuts + weasly.knuts

total = potter + weasly
print(total)

# This is now the implementation of operator overloading
