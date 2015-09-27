import random

# Create randomized sickness function
sickdict = {'Flu':10, 'Cold':5, 'Ebola':20, 'Measles':20, 'Allergies': 0}
def sickness():
    global sickdict
    sick = random.choice(sickdict.keys())
    sickname = sick
    sickpower = sickdict[sick]
    del sickdict[sick]
    return sickname, sickpower

class Person():
    # Define person object
    def __init__(self, name, sleep, clean, flu_shot, vaccinated):
        self.name = name
        self.sleep = sleep
        self.clean = clean
        self.flu_shot = flu_shot
        self.vaccinated = vaccinated
        self.hp = ()

class Infected():
    def __init__(self):
        self.sn = ()
        self.sp = ()

# Create infection battle function

# Main game control

name = raw_input("Enter your name: ")
sleep = raw_input("How many hours of sleep do you get a night? ")
clean = raw_input("Do you regularly wash your hands? Y or N")
flu_shot = raw_input("Do you get an annual flu shot? Y or N ")
vaccinated = raw_input("Were you vaccinated as a child? Y or N")

# Add up health points
sleep = int(sleep)
if clean.upper() == 'Y':
    clean_hp = 20
else:
    clean_hp = 0

if flu_shot.upper() == 'Y':
    flu_shot_hp = 10
else:
    flu_shot_hp = 0

if vaccinated.upper() == 'Y':
    vaccinated_hp = 20
else:
    vaccinated_hp = 0


# Total up all health points
hp = sleep + clean_hp + flu_shot_hp + vaccinated_hp

player = Person(name, sleep, clean_hp, flu_shot_hp, vaccinated_hp)
infected = Infected()

# Assign player total of all health points
player.hp = hp

print "Your starting health is %s " % player.hp
print ''

# Scenario 1
print "You are on a bus and the person next to you is clearly sick. Do you:"
print "Move away from them. Enter A\nDo nothing and hope that you don't get sick. Enter B:"
scene1 = raw_input("Enter your choice: ")
if scene1.upper() == 'A':
    player.hp += 5
else:
    player.hp -= 5

illness = sickness()
infected.sn = illness[0]
infected.sp = illness[1]

player.hp = player.hp - infected.sp
print "You were exposed to: %s " % illness[0]
print "Your health points went down " + str(illness[1]) + " points"
if player.hp < 0:
    print "You have %s health points. Get some rest and try again." % player.hp
    quit()
print ''
print "You have %s health points." % player.hp
print ''
cont = raw_input("Hit Enter to continue")

# Scenario 2
print ''
print ''
print "You get to work and by the time you've reached your office you have touched 10 different surfaces. Do you:"
print "Wash your hands before starting work. Enter A:\nUse antibacterial at your desk. Enter B:\nNeither because you are confident in your health. Enter C:"
scene2 = raw_input("Enter you choice: ")
if scene2.upper() == 'A':
    player.hp += 5
elif scene2.upper() == 'B':
    player.hp += 10
elif scene2.upper() == 'C':
    pass
else:
    pass

illness = sickness()
infected.sn = illness[0]
infected.sp = illness[1]

player.hp = player.hp - infected.sp
print "You were exposed to: %s " % illness[0]
print "Your health points went down " + str(illness[1]) + " points"
print ''
if player.hp < 0:
    print "You have %s health points. Get some rest and try again." % player.hp
    quit()
print ''
print "You have %s health points." % player.hp
print ''
cont = raw_input("Hit Enter to continue")

# Scenario 3
print ''
print ''
print "Your co-worker is sick and you will be working in close proximity to them. Do you:"
print "Say you're not feeling well and go home to avoid being around them? Enter A:\nWear a mask while working with them and wash your hands often. Enter B:"
scene3 = raw_input("Enter you choice: ")
if scene3.upper() == 'A':
    player.hp += 5
elif scene3.upper() == 'B':
    player.hp -= 5
else:
    pass

illness = sickness()
infected.sn = illness[0]
infected.sp = illness[1]

player.hp = player.hp - infected.sp
print "You were exposed to: %s " % illness[0]
print "Your health points went down " + str(illness[1]) + " points"
print ''
print "You survived a day at work! Your health points are %s " % player.hp
print ''
# I could have created a dictionary for the questions?
#questions = {"question1":{"question text":answer value, "question text": answer value}
#            "question2":{"question text": answer value, "question text": answer value}}
# Create a 3 iteration loop and called a function for each Scenario
