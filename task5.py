#Soldier Ryan has an AK47
# Soldiers can fire ("tigi-tigitishh").
# Guns can fire bullets.
# Guns can fill bullets - increase the number of bullets(reloads)
#
# Create class Act_of_Shooting, which will inheritates from class Soldier, class Guns.
# Where soldier will fire from a gun and reload, and fire one more time.
class Soldiers():
    def __init__(self):
        self.name = "Ryan"


class Guns(Soldiers):
    def __init__(self):
        Soldiers.__init__(self)
        self.bullets = 3

    def fire(self):
        name = self.name
        print(name, ' started firing! Be careful! Watch out! Dont get killed!!')
        while self.bullets:
            print("tigi-tigitishh")
            self.bullets -= 1
        self.reload()

    def reload(self):
        self.bullets = 10

class Act_of_Shooting(Guns):
    def __init__(self):
        Guns.__init__(self)
        Soldiers.__init__(self)

    def start(self):
        Guns.fire(self)
        Guns.reload(self)
        Guns.fire(self)

game = Act_of_Shooting()
game.start()


