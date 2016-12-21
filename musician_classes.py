class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print self.sounds[i % len(self.sounds)]
        print

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Bassist, self).__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Guitarist, self).__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print "Be with you in a moment"
        print "Twoning, sproing, splang"

class Drummer(Musician):
    def __init__(self):
        super(Drummer, self).__init__(["Bang", "Smash", "BamBam"])
    
    def count_up(self, upper):
        print "Ready!" + ",".join([str(idx) for idx in range(1,upper+1)])
        
    def combust(self):
        print "Oh dear me, it appears I've burst into flames."
        

class Band(object):
    def __init__(self, members = []):
        self.members = members
    
    def hire(self,member):
        self.members.append(member)
    
    def fire(self,member):
        self.members.remove(member)
        
    def play_solos(self,duration):
        #need to figure out how to check if there is a drummer class in my band
        crew = [str(type(each)) for each in self.members]
#        for musician in self.members:
#            musician.solo(duration)
