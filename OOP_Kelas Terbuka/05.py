class Hero:

    def __init__(self,name,health,attackPower,armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def serang(self,lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self)

    def diserang(self,lawan):
        print(self.name + ' diserang ' + lawan.name)

sniper = Hero('sniper',100,10,5)
doni = Hero('doni',100,1100,0)
jox = Hero('jox',1000,2,1)
sniper.serang(jox)
