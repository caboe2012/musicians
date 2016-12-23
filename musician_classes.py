#uses Python2
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
    
    def member_list(self):
        for member in self.members:
            print member
    
    def hire(self,member):
        self.members.append(member)
    
    def fire(self,member):
        self.members.remove(member)
    
    def play_solos(self, drummer_count, duration):
        # Getting the class name of an instance in python!  Huzzah!
        # wrong way ->   str(type("instance")) 
        # right way! ->  type("instance").__name__
        crew = [type(each).__name__ for each in self.members]
        if "Drummer" in crew:
            idx = crew.index("Drummer")
            self.members[idx].count_up(drummer_count)
            for each in self.members:
                each.solo(duration)
        else:
            print "We totally gotta git a drummer or we'll never be able to play our solos!"


# Instantiate Musicians
tom = Guitarist()
dick = Bassist()
harry = Drummer()

# Demo spontaneous combustion method of drummer
harry.combust()

# Demo count method of the drummer class
harry.count_up(5)

# Instantiate Band class
rhcp = Band()

# Show empty band list
rhcp.members

# Hire Guitarist and Bassist
rhcp.hire(tom)
rhcp.hire(dick)

# Try and play solos without a drummer
rhcp.play_solos(4,6)

# hire a drummer
rhcp.hire(harry)

# let the hits roll!
rhcp.play_solos(4,6)