import pyglet
import time
import sys
import test106 as test


#######Class#######

class House:

    def __init__(self):
        self.score = []
        self.path = []
        self.inventory = []
    
    def prologue(self):
        s = "You slowly open your eyes and wake up on a bed in an empty bedroom.\nYou don't remember anything and you don't know why you are in this room.\nThis room only has a mirror and a nightstand next to the bed. It doesn't have any window but just a door that seems to be locked.\nAnd you see a silver key on the nightstand.\nWhat are you going to do?\n"
        choice1 = "#1 Pick up the key and unlock the door\n"
        choice2 = "#2 Stay and die by starvation\n"
        self.score.append(1)
        self.path.append("Bedroom")
        return s + choice1 + choice2
        
    def hallway(self):
        description = "You enter a long dark hallway, which has three doors: door #1, door #2 and door #3.\nWhich door are you going to choose? Type in the number.\n"
        self.score.append(1)
        self.path.append("Hallway")
        return description       
    
    def room1(self):
        description = "In room 1, you see a chair and a table in the middle of the room. On the table, there is food.\nYou realize that you are very hungry.\nWhat are you going to do? Enter a number.\n"
        choice1 = "#1 Eat the food.\n"
        choice2 = "#2 Leave this room.\n" 
        self.path.append("Room 1")
        self.score.append(1)
        return description + choice1 + choice2
        
    def room1_1(self):
        description = "The food contains poison. However, it's too late. The poison has already spread inside your body.\nAs you grasp for breath, you slowly turn around and see a person standing by the door.\nYou cannot see the person's face because your vision has become blurry.\nAs you collapse to the floor and breathe your last breath, you hear him laugh.\n"
        game_over = ">>Game over.\n"
        self.score.append(1)
        return description + game_over
        
    def room1_2(self):
        description = "You turn around to leave this room.\nHowever the door suddenly shuts and locks itself.\nSince you cannot get out of here, you slowly starve to death."
        game_over = ">>Game over.\n"
        self.score.append(1)
        return description + game_over
        
    def room2(self):
        description = "In room 2, you see two chests in the middle of the room:\nA giant chest full of gold and jewelry.\nThe other chest is smaller. And you don't know what is inside unless you open it.\nWhat are you going to do? Enter a number.\n"
        choice1 = "#1 Eagerly run to the giant chest and open it.\n"
        choice2 = "#2 Hesitantly walk to the small chest and open it.\n"
        self.score.append(1)
        self.path.append("Room 2")
        return description + choice1 + choice2
        
    def room2_1(self):
        description = "You reach the giant chest and open it. Greedily you dig with your hands into the gold coins and jewels, and put them into your pocket.\nSuddenly you feel a sharp striking pain in your right hand.\nYou then realize that there was a snake inside the chest and paralyzed your body with its poison.\nYou have to watch helplessly how the snake crawls around your right arm towards your neck.\nThe snake winds around your neck tight until it chokes you to death.\n"
        game_over = ">>Game over.\n"
        self.score.append(1)
        return description + game_over
        
    def room2_2(self):
        description = "You open the small chest and see a paper inside it.\nThere is something written in red ink:\n>QUICKLY GET OUT OF THIS HOUSE.\nHE WILL COME AFTER YOU AND KILL YOU<\nThen you feel the breath of somebody around your neck.\nAnd a cold knife pressed against your neck.\nHe whispers:\n>>It's too late.<<\nEverything turns dark.\n"
        game_over = ">>Game over.\n"
        self.score.append(1)
        return description + game_over
        
    def room3(self):
        description = "In room 3, you see a wardrobe, a table with a fork, and a chair.\nAs you walk up to the table, you suddenly hear steps in the hallway.\nThese steps seem to approach the room that you are currently in.\nWhat are you going to do? Enter a number.\n"
        choice1 = "#1 Quickly jump to the wardrobe and hide in there.\n"
        choice2 = "#2 Grab the fork and hide under the table.\n"
        choice3 = "#3 You calm yourself down and sit on the chair.\n"
        self.score.append(1)
        self.path.append("Room 3")
        return description + choice1 + choice2 + choice3
        
    def room3_1(self):
        description = "You jump into the wardrobe but leave the doors of the wardrobe ajar,\nso that you can see what is happening outside.\nA man steps into the room.\nHe looks around until his look rests on the wardrobe.\nHe smiles, pulls out the chair and sits on it.\nThen he stares at the wardrobe and waits.\nThen you realize that there is a note attached to the bottom of the wardrobe. It says:\n>You seriously think that I don't know where you are.<\nParalyzed by fear, you don't dare to get out and you starve inside.\n"
        game_over = ">>Game over.\n"
        self.score.append(1) 
        self.inventory.append("Threat Note")
        return description + game_over
        
    def room3_2(self):
        description = "You quickly crawl under the table.\nA man enters the room and sees you under the table.\nHe walks up to the table and drags you out.\nBefore you can scream, he takes out a knife and slices your throat.\nYou feel the blood running out of your throat.\nEverything turns black.\n"
        game_over = ">>Game over.\n"
        self.score.append(1) 
        return description + game_over
        
    def room3_3(self):
        description = "You sit down on the chair.\nA man enters into the room.\nHe looks at you and says:\n>>Oh, you are not even trying.<<\nHe comes up to you, takes out his knife, and stabs you into your chest.\nYou feel sharp pain within you.\nEverything turns black.\n"
        game_over = ">>Game over.\n"
        self.score.append(1)
        return description + game_over
        
        

#######Functions#######

mystery = House() #instantiate mystery of type House  

pyglet.lib.load_library('avbin')    #retrieve avbin.dll from the working directory (note: avbin.dll should be present in the working directory)
pyglet.have_avbin=True             #this code tells pyglet that AVBin is present, so that compressed files, such as MP3, can be decompressed and processed through AVBin 
def play_music(filename):
    player = pyglet.media.Player()
    music = pyglet.media.load(filename)
    player.queue(music)    
    player.eos_action = pyglet.media.Player.EOS_LOOP
    player.play()
    
def steady_print(text):            #both of these functions allows slower printing of strings character by character with user-defined speed 
    for character in text:
        sys.stdout.write(character)     
        time.sleep(.05) 
    return ""

def quick_print(text):           
    for character in text:
        sys.stdout.write(character)
        time.sleep(0.01)
    return ""

    
def first_choice(antwort): 
    if antwort == 1:
        v = mystery.hallway()
        mystery.inventory.append("Silver Key")
        return steady_print(v)
    elif antwort == 2:
        game_over = "You stayed in the room and died out of starvation\n"
        return steady_print(game_over) + "Game Over.\n"
    else:
        return "Since you couldn't decide, you played against the rule of the game.\nThe creator of this game decides to punish you for this. So you die.\nGame Over.\n"

def second_choice(antwort):
    if antwort == 1:
        v = mystery.room1()
        return steady_print(v)
    elif antwort == 2:
        v = mystery.room2()
        return steady_print(v)
    elif antwort == 3:
        v = mystery.room3()
        return steady_print(v)
    else:
        return "Since you couldn't decide, you walked straight into the abyss of the hallway, fell and died.\n" + "Game Over.\n"
        
def first_room(antwort):              #what happens in the first room depending on the answer given
    if antwort == 1:
        y = mystery.room1_1()
        mystery.inventory.append("Poisoned food")
        return steady_print(y)
    elif antwort == 2:
        y = mystery.room1_2()
        return steady_print(y)
    else:
        return "Since you couldn't decide, you played against the rule of the game.\nThe creator of this game decides to punish you for this. So you die.\nGame Over.\n"

def second_room(antwort):              #what happens in the second room depending on the answer given
    if antwort == 1:
        y = mystery.room2_1()
        mystery.inventory.append("Gold and Jewels")
        return steady_print(y)
    elif antwort == 2:
        y = mystery.room2_2()
        mystery.inventory.append("Note")
        return steady_print(y)
    else:
        return "Since you couldn't decide, you played against the rule of the game.\nThe creator of this game decides to punish you for this. So you die.\nGame Over.\n"
        
def third_room(antwort):                #what happens in the third room depending on the answer given
    if antwort == 1:
        y = mystery.room3_1()
        return steady_print(y)
    elif antwort == 2:
        y = mystery.room3_2()
        mystery.inventory.append("Fork")
        return steady_print(y)
    elif antwort == 3:
        y = mystery.room3_3()
        return steady_print(y)
    else:
        return "Since you couldn't decide, you played against the rule of the game.\nThe creator of this game decides to punish you for this. So you die.\nGame Over.\n"
 


###################################################################################################################
###################################################################################################################
print quick_print("We are going to play this little game.")
print quick_print("However there is ONE rule: You have to CHOOSE.\nOtherwise you die :)")
time.sleep(1)
print quick_print("As long as you understand this, you are going to be fine.\nAre you ready?")
start = raw_input("If you are, press enter.")
b = "Then let's get started :)."
print quick_print(b)

time.sleep(2)
print "------------------------------------------------THE MYSTERY HOUSE------------------------------------------------"
time.sleep(1)
play_music('pulse.mp3') 

###Prologue
d = mystery.prologue()
print steady_print(d)  
###First Decision
amrum = int(raw_input(">>"))   #Get out or starve.  
print steady_print(first_choice(amrum))
###Second Decision
if amrum == 1:
    door = int(raw_input(">>"))    #Door1/2/3? 
    print steady_print(second_choice(door))
else:
    print ""
###Third Decision              #Depending on which door the player chose, the player has to input a few different choices. 
try: 
    if door == 1:                  
        answer1 = int(raw_input(">>")) 
        print steady_print(first_room(answer1))   #what happens in the first room
    elif door == 2:
        answer2 = int(raw_input(">>"))
        print steady_print(second_room(answer2))  #what happens in the second room
    elif door == 3:
        answer3 = int(raw_input(">>")) 
        print steady_print(third_room(answer3))   #what happens in the third room
    else:
        print ""
except Exception:
    print ""

time.sleep(2)    

####Summarize Game Stats####
inventory_list = sorted(mystery.inventory, key = lambda item: len(item), reverse = True)  
score_list = [score*2 for score in mystery.score]

total_score = int(reduce(lambda x, y: x + y, score_list))
scorelist = str(score_list)
path = str(mystery.path)
inventory = str(inventory_list)

game_statement = "Game Stats:\nYour Total Game Score:\n%d\nList of Scores:\n%s\nYour Path through the House:\n%s\nYour Inventory:\n%s\n" % (total_score, scorelist, path, inventory)
print quick_print(game_statement)

print "\n"
print "----------------------------End of the Game-----------------------------------------"
print "\n"
print "\n"
time.sleep(2)

print "Now to the Test Cases:"
print "------------------Start of Test Cases(it is going to take some time)------------------"
#Testing for first_room function:
test.testEqual(type(first_room(1)), type(""))    
#Testing for second_room function:    
test.testEqual(second_room(5), "Since you couldn't decide, you played against the rule of the game.\nThe creator of this game decides to punish you for this. So you die.\nGame Over.\n")        
#Testing for steady_print function:
lovelz = "Fischer Fritz fischt frische Fische."
test.testEqual(steady_print(lovelz), "")
test.testEqual(type(steady_print(lovelz)), type("")) 
#Testing for second_choice function: 
test.testEqual(second_choice(1), "")
print "------------------End of Test Cases------------------" 

print quick_print("Hope you enjoyed the game :)")
