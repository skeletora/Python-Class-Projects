
#This is my choose your own adventure game

print ("Hello!  Welcome to a choose your own adventure!")


#This gets the players name

player_name = input ("""

"Tell me, oh great adventurer, what is your name?" """)


#Greet the player

print ("""

Hello there %s!  'Tis a pleasure to meet you.""" % (player_name))


#begin playing

print ("""

"Well %s, I'm sorry to say that you have been forced to go into a dark,
abandoned house by your friends.  You are currently in the foyer.  A
hallway stretched out in front of you.  You decide to walk into the
living room.  There are pieces of rotting furniture laying scattered
about and the wallpaper is scratched, faded, and peeling from the walls.
You see there are two doors in the back, one on the left and one on the
right.  Your friends dared you to stay in here for one hour, so you
decide you might as well explore." """ % (player_name))


#Choice location

chose_location = input ("""

"You have two options as to where you want to go, excluding leaving
because you want to win the dare.  Do you go through the door on the
right or the door on the left?"
(Say left or right) """)








#left door

if chose_location.lower() == "left":

    print ("""

You head toward the door on the left side of the living room, walking
carefully to avoid stepping in one of the numerous holes in the floor.""")


    print ("""

You reach the door and it takes several attempts to open.  Eventually,
it gives a loud screech and part of the door comes off as it swings into
the room.  You find yourself in what appears to be a workshop.  There is
a worktable off in the far right corner and there are the rusted
carcasses of ancient tools hanging on the walls and littering the floor.
A rat runs past you as you step into the room.  You head into the center
of the room, watching where you step for fear of falling through the floor
or stepping on the rusty remains of one of the tools laying on the ground.""")


    print ("""

You suddenly hear a loud banging noise coming from the room above the one
you're in.  You're suppose to be alone.  The noise gets louder.""")


    #Investigate noise

    choice_investigate = input ("""

"Do you go see what is causing the noise?" (Yes or No) """)


    #Yes investigate noise

    if choice_investigate.lower() == "yes" or choice_investigate.lower() == "y":

        print ("""

Taking a deep breath, you turn and head out of the room, grabbing a not so
horribly rusty hammer off of the floor.  You quietly and carefully slink
through the living room and head into the hallway.  There are no windows
in the hallway, making it very dark.  You try a light switch but nothing
happens.  As you proceed further, you can dimly see water stained portraits,
whose occupants glare down on you as you pass.  You eventually come up to a
rotted out staircase. """)


        print ("""

You cautiously put your foot on the first step that doesn't look too rotten
and slowly put your weight on it.  When it doesn't give, you continue the
procedure until you reach the top.  You find yourself in a dusty hallway
with numerous holes in the floor and sections of the wall missing.  You
listen for the banging sound.  Instead you hear quiet sobbing coming from the
room two doors away.  You walk over to the room the sound is coming from and
stand in front of the door.""")



        #open the door?

        choice_open_door = input ("""

"This is your final chance.  Do you open the door?" """)



        #Yes open door

        if choice_open_door.lower() == "yes" or choice_open_door.lower() ==  "y":

            print ("""

You reach for the doorknob.  As you turn it and push, the door gives a screech.
You see a figure hunched up in the center of the room.  It looks like a little
girl.  She stops crying when she hears you approach.  "Hello?" you tentatively
say.  The girl sits up.  "Hello."  You hear the little girl say.  "Do you want
to play?" she says, turning toward you.  You step back in shock.  Blood covers
the girls face and a large cut can be seen on her forehead.""")



            #Runaway

            choice_runaway = input ("""

"Do you run away? """)



            #Yes runaway

            if choice_runaway.lower() == "yes" or choice_runaway.lower() == "y":

                print ("""

You turn and sprint out of the room.  You head toward the staircase and take
them as fast as you can, not caring about their age.  One of the boards breaks
but you somehow managed to not get stuck.  When you reached the bottom, You
sprinted down the hall toward the front door.  You grabbed the doorknob, but
then stopped.""")



                #Leave house

                choice_leave_house = input ("""

"You could leave now, but then you would lose the bet.  Do you leave?" """)



                #Yes leave house

                if choice_leave_house.lower() == "yes" or choice_leave_house.lower() == "y":

                    print ("""

You twist the knob and through open the door.  As you fly out the door, you
hear very quietly, "I just wanted to play."  You run down to the street toward
your friend's car.  "Hey %s, it hasn't been an hour.  Pay up.  $50."  You
dig into your pocket and toss him the money.  "Now get out of here!" you shout.
Your friends turn and look at you as you drive away.  "I'm never going in there
again!" """ % (player_name))



                #No leave house
                elif choice_leave_house.lower() == "no" or "n":
                    print ("""
No!  You can't leave.  You have $50 at stake.  It was just a little girl.  What harm could she do?
"Unfortunatly for you, those were your last thoughts.  As you finished thinking that, you heard
whispered behind you, 'I always loved chase.'  " """)
                        
                           


            #No run away
            elif choice_runaway.lower() == "no" or "n":
                print("""
The girl is hurt.  You decide to stay and try to help her. "Do you want to play?" she says a bit
more forcefully.  "Let me take you to the hospital," you say.  "No!  I want to
play!" she screams, stomping.""")




                #Play
                choice_play = input ("""
Do you play with the girl to try to calm her? """)



                #Yes play
                if choice_play.lower() == "yes" or choice_play.lower() == "y":
                    print ("""
How about this," you say calmly, "I'll play with you for a little bit and then you let
me take you to the hopital."  The girl's face lights up.  "Okay" she says, "I want to
play hide and seek.  You hide first and I'll try to find you!" "Okay.  What are you
counting too?"  "Twenty. Ready, set, . . . GO!!!" she shouted.  You turn and hurry
out of the room.  You can hear her slowly counting behind you.  You decide to go back
to that workshop.  You'll hide under the table in there.""")
                    
                    print ("""
You finally get in there and crouch under the table.  You had just gotten situated when
you feel something next to you.  "Found you." she whispered as you felt her hands
wrapped around your neck.""")
                    
                    print ("""
When the hour was up and you didn't come out of the house, your friends tried to go in.
They couldn't open the doors or windows.  They eventually called the police.  Your body
was never found. """)



                #No play
                elif choice_play.lower() == "no" or "n":
                    print ("""
You suddenly get very angry and annoyed with the girl.  "No!  We're not playing!  You
are coming with me to the hospital to get your injuries checked out!"  The girl's eyes
grow moist.  "You're so mean.  And you're no fun!" she says and promptly disappears.
You step back surprised.  "There is no way that just happened," you say.  You walk in
a daze out of the room and go into the living room.

When the hour is up, you head out to your friend's car.  "Well damn, you actually did
it!  I owe you fifty bucks."  You get in the car and drive away.""")



        #No open door

        elif choice_open_door.lower() == "no" or "n":

            print ("""

On second thought, you decide it's a bad idea to investigate weird noises in an

old house.""")



            #Return to room
            choice_return_to_room = input ("""
"Well, since you've decided that investigating the noise was a bad idea, do you
want to go back to the room you were in?" """)



            #Yes return to room
            if choice_return_to_room.lower() == "yes" or choice_return_to_room.lower() == "y":
                print ("""
You decide it would be best to return to the workshop.  When you arrive there, you see a
little girl standing there.  She turns and looks at you.  You step back in shock.  Blood covers
the girls face and a large cut can be seen on her forehead. "Do you want to play?" """)


                 #Play
                choice_play = input ("""
"Do you play with the girl?" """)


                #Yes play
                if choice_play.lower() == "yes" or choice_play.lower() == "y":
                    print ("""
The girl's face lights up.  "Okay" she says, "I want to
play hide and seek.  You hide first and I'll try to find you!" "Okay.  What are you
counting too?"  "Twenty. Ready, set, . . . GO!!!" she shouted.  You turn and hurry
out of the room.  You can hear her slowly counting behind you.  You decide to go back
to the staircase.  You'll hide in the little gap under the stairs.""")
                    
                    print ("""
You finally get in there and crouch under the stairs.  You had just gotten situated when
you feel something next to you.  "Found you." she whispered as you felt her hands
wrapped around your neck.""")
                    
                    print ("""
When the hour was up and you didn't come out of the house, your friends tried to go in.
They couldn't open the doors or windows.  They eventually called the police.  Your body
was never found. """)




            #No return to room
            elif choice_return_to_room.lower() == "no" or "n":
                print ("""
Whatever is making that sound probably heard you open the door.  You decide its
not safe to go back.""")



                #leave house
                choice_leave_house = input ("""
"Do you leave the house?  You'll lose the bet." """)



                #Yes leave house
                if choice_leave_house.lower() == "yes" or choice_leave_house.lower() == "y":
                    print ("""
You quietly head back down stairs.  You walk down the hall toward the front door.  You twist
the knob and throw open the door.  As you fly out the door, you hear very quietly,
"I just wanted to play."  You run down to the street toward your friend's car.  "Hey %s, it
hasn't been an hour.  Pay up.  $50."  You dig into your pocket and toss him the money.
"Now get out of here!" you shout.  Your friends turn and look at you as you drive away.
"I'm never going in there again!" """ % (player_name))



                #No leave house
                elif choice_leave_house.lower() == "no" or "n":
                    print ("""
No!  You can't leave.  You have $50 at stake.  It was just some funny noises, what could possibly
be in here that would be super dangerous. "Unfortunatly for you, those were your last thoughts.
As you finished thinking that, you heard whispered behind you, 'I want to play.'

When the hour was up and you didn't come out of the house, your friends tried to go in. They
couldn't open the doors or windows.  They eventually called the police.  Your body was never found." """)


                

#No to investigate noise    
    elif choice_investigate.lower() == "no" or "n":

        print ("""

You're not sure what's making the noise, but it probably isn't good.  You
decide to stay here with the tools and hope that whatever it is doesn't
bother you.  And if it does come downstairs, you have a bunch of rusty tools
to beat it off with.""")



        #Find weapon
        choice_find_weapon = input ("""
"But it might be best to find a semidecent weapon.  Do you pick out a weapon?" """)



        #Yes find weapon
        if choice_find_weapon.lower() == "yes" or choice_find_weapon.lower() == "y":
            print ("""
It takes some digging, but you eventually find a not completely rusted hammer that seems stable enough.
You straighten yourself out and turn around. You jump in shock.  A little girl is standing there.
Blood covers the girls face and a large cut can be seen on her forehead. "Do you want to play?"
she says. """)



            #Runaway
            choice_runaway = input ("""
"Do you run away? """)



            #Yes runaway

            if choice_runaway.lower() == "yes" or choice_runaway.lower() == "y":

                print ("""
You forget about your weapon and sprint out of the room, knocking the girl out of the way. You slick
through the living room.   When you get to the hallway, you sprint toward the front door.  You grabbed
the doorknob, but then stop.""")



                #Leave house
                choice_leave_house = input ("""
"You could leave now, but then you would lose the bet.  Do you leave?" """)



                #Yes leave house

                if choice_leave_house.lower() == "yes" or choice_leave_house.lower() == "y":

                    print ("""
You twist the knob and through open the door.  As you fly out the door, you
hear very quietly, "I just wanted to play."  You run down to the street toward
your friend's car.  "Hey %s, it hasn't been an hour.  Pay up.  $50."  You
dig into your pocket and toss him the money.  "Now get out of here!" you shout.
Your friends turn and look at you as you drive away.  "I'm never going in there
again!" """ % (player_name))



                #No leave house
                elif choice_leave_house.lower() == "no" or "n":
                    print ("""
No!  You can't leave.  You have $50 at stake.  It was just a little girl.  What harm could she do?
"Unfortunatly for you, those were your last thoughts.  As you finished thinking that, you heard
whispered behind you, 'I always loved chase.'

Your body was never found." """)



        #No find weapon
        elif choice_find_weapon.lower() == "no" or "n":
            print ("""
You don't need a weapon.  You're perfectly safe!  You dig around in the room to see what you can find.
You straighten yourself out and turn around. You jump in shock.  A little girl is standing there.
Blood covers the girls face and a large cut can be seen on her forehead. "Do you want to play?" she says. """)



            #Runaway
            choice_runaway = input ("""
"Do you run away? """)



            #Yes runaway
            if choice_runaway.lower() == "yes" or choice_runaway.lower() == "y":
                
                print ("""
You sprint out of the room, pushing the girl out of the way.  You slink through the
living room.  When you get to the hallway, you sprint toward the front door.  You grabbed the
doorknob, but then stopped.""")



                #Leave house

                choice_leave_house = input ("""
"You could leave now, but then you would lose the bet.  Do you leave?" """)



                #Yes leave house

                if choice_leave_house.lower() == "yes" or choice_leave_house.lower() == "y":

                    print ("""
You twist the knob and through open the door.  As you fly out the door, you
hear very quietly, "I just wanted to play."  You run down to the street toward
your friend's car.  "Hey %s, it hasn't been an hour.  Pay up.  $50."  You
dig into your pocket and toss him the money.  "Now get out of here!" you shout.
Your friends turn and look at you as you drive away.  "I'm never going in there
again!" """ % (player_name))



                #No leave house
                elif choice_leave_house.lower() == "no" or "n":
                    print ("""
No!  You can't leave.  You have $50 at stake.  It was just a little girl.  What harm could she do?
"Unfortunatly for you, those were your last thoughts.  As you finished thinking that, you heard
whispered behind you, 'I always loved chase.'

Your body was never found." """)




             #No runaway
            if choice_runaway == "no" or "n":
                #Play
                choice_play = input ("""
"Do you play with the girl?" """)


                #Yes play
                if choice_play.lower() == "yes" or choice_play.lower() == "y":
                    print ("""
The girl's face lights up.  "Okay" she says, "I want to
play hide and seek.  You hide first and I'll try to find you!" "Okay.  What are you
counting too?"  "Twenty. Ready, set, . . . GO!!!" she shouted.  You turn and hurry
out of the room.  You can hear her slowly counting behind you.  You decide to go back
to the staircase.  You'll hide in the little gap under the stairs.""")
                    
                    print ("""
You finally get in there and crouch under the stairs.  You had just gotten situated when
you feel something next to you.  "Found you." she whispered as you felt her hands
wrapped around your neck.""")
                    
                    print ("""
When the hour was up and you didn't come out of the house, your friends tried to go in.
They couldn't open the doors or windows.  They eventually called the police.  Your body
was never found. """)



                #No play
                elif choice_play.lower() == "no" or "n":
                    print ("""
You suddenly get very angry and annoyed with the girl.  "No!  We're not playing!"  The girl's
eyes grow moist.  "You're so mean.  And you're no fun!" she says and promptly disappears.
You step back surprised.  "There is no way that just happened," you say.  You walk in
a daze out of the room and go into the living room.

When the hour is up, you head out to your friend's car.  "Well damn, you actually did
it!  I owe you fifty bucks."  You get in the car and drive away.""")








    









#right door    

if chose_location.lower() == "right":

    print ("""

You head toward the door on the right side of the living room, walking
carefully to avoid stepping in one of the numerous holes in the floor.""")

    print ("""

You reach the door and it takes several attempts to open.  Eventually,
it gives a loud screech and part of the door comes off as it swings into
the room.  You find yourself in what looks like a play room.  A rotting
doll house sits in the far right corner.  A collapsed dresser in the far
left.  Chunks of what looks like dolls are scattered throughout the room.""")


    print ("""
You suddenly hear a loud banging noise coming from upstairs.  You're
suppose to be alone.  The noise gets louder.""")




    #Investigate noise

    choice_investigate = input ("""

"Do you go see what is causing the noise?" (Yes or No) """)




    #Yes investigate noise

    if choice_investigate.lower() == "yes" or choice_investigate.lower() == "y":

        print ("""

Taking a deep breath, you turn and head out of the room.  You quietly and carefully slink
through the living room and head into the hallway.  There are no windows
in the hallway, making it very dark.  You try a light switch but nothing
happens.  As you proceed further, you can dimly see water stained portraits,
whose occupants glare down on you as you pass.  You eventually come up to a
rotted out staircase. """)


        print ("""

You cautiously put your foot on the first step that doesn't look too rotten
and slowly put your weight on it.  When it doesn't give, you continue the
procedure until you reach the top.  You find yourself in a dusty hallway
with numerous holes in the floor and sections of the wall missing.  You
listen for the banging sound.  Instead you hear quiet sobbing coming from the
room two doors away.  You walk over to the room the sound is coming from and
stand in front of the door.""")



        #open the door?

        choice_open_door = input ("""

"This is your final chance.  Do you open the door?" """)



        #Yes open door

        if choice_open_door.lower() == "yes" or choice_open_door.lower() ==  "y":

            print ("""

You reach for the doorknob.  As you turn it and push, the door gives a screech.
You see a figure hunched up in the center of the room.  It looks like a little
girl.  She stops crying when she hears you approach.  "Hello?" you tentatively
say.  The girl sits up.  "Hello."  You hear the little girl say.  "Do you want
to play?" she says, turning toward you.  """)



            #Runaway

            choice_runaway = input ("""

"Do you run away? """)



            #Yes runaway

            if choice_runaway.lower() == "yes" or choice_runaway.lower() == "y":

                print ("""

You turn and sprint out of the room.  You head toward the staircase and take
them as fast as you can, not caring about their age.  One of the boards breaks
but you somehow managed to not get stuck.  When you reached the bottom, You
sprinted down the hall toward the front door.  You grabbed the doorknob, but
then stopped.""")



                #Leave house

                choice_leave_house = input ("""

"You could leave now, but then you would lose the bet.  Do you leave?" """)



                #Yes leave house

                if choice_leave_house.lower() == "yes" or choice_leave_house.lower() == "y":

                    print ("""

You twist the knob and through open the door.  As you fly out the door, you
hear very quietly, "I just wanted to play."  You run down to the street toward
your friend's car.  "Hey %s, it hasn't been an hour.  Pay up.  $50."  You
dig into your pocket and toss him the money.  "Now get out of here!" you shout.
Your friends turn and look at you as you drive away.  "I'm never going in there
again!" """ % (player_name))



                #No leave house
                elif choice_leave_house.lower() == "no" or "n":
                    print ("""
No!  You can't leave.  You have $50 at stake.  It was just a little girl.  What harm could she do?
"Unfortunatly for you, those were your last thoughts.  As you finished thinking that, you heard
whispered behind you, 'I always loved chase.'

Your body was never found." """)
                        
                           


            #No run away
            elif choice_runaway.lower() == "no" or "n":
                print("""
The girl is hurt.  You decide to stay and try to help her. "Do you want to play?" she says a bit
more forcefully.  "Let me take you to the hospital," you say.  "No!  I want to
play!" she screams, stomping.""")



                #Play
                choice_play = input ("""
Do you play with the girl to try to calm her? """)



                #Yes play
                if choice_play.lower() == "yes" or choice_play.lower() == "y":
                    print ("""
How about this," you say calmly, "I'll play with you for a little bit and then you let
me take you to the hopital."  The girl's face lights up.  "Okay" she says, "I want to
play hide and seek.  You hide first and I'll try to find you!" "Okay.  What are you
counting too?"  "Twenty. Ready, set, . . . GO!!!" she shouted.  You turn and hurry
out of the room.  You can hear her slowly counting behind you.  You decide to go back
to that workshop.  You'll hide under the table in there.""")
                    
                    print ("""
You finally get in there and crouch under the table.  You had just gotten situated when
you feel something next to you.  "Found you." she whispered as you felt her hands
wrapped around your neck.""")
                    
                    print ("""
When the hour was up and you didn't come out of the house, your friends tried to go in.
They couldn't open the doors or windows.  They eventually called the police.  Your body
was never found. """)


                #No play
                elif choice_play.lower() == "no" or "n":
                    print ("""
You suddenly get very angry and annoyed with the girl.  "No!  We're not playing!  You
are coming with me to the hospital to get your injuries checked out!"  The girl's eyes
grow moist.  "You're so mean.  And you're no fun!" she says and promptly disappears.
You step back surprised.  "There is no way that just happened," you say.  You walk in
a daze out of the room and go into the living room.

When the hour is up, you head out to your friend's car.  "Well damn, you actually did
it!  I owe you fifty bucks."  You get in the car and drive away.""")



        #No open door

        elif choice_open_door.lower() == "no" or "n":

            print ("""

On second thought, you decide it's a bad idea to investigate weird noises in an
old house.""")



            #Return to room
            choice_return_to_room = input ("""
"Well, since you've decided that investigating the noise was a bad idea, do you
want to go back to the room you were in?" """)



            #Yes return to room
            if choice_return_to_room.lower() == "yes" or choice_return_to_room.lower() == "y":
                print ("""
You decide it would be best to return to the play room.  When you arrive there, you see a
little girl in there.  She turns and looks at you.   """)


                 #Play
                choice_play = input ("""
"Do you play with the girl?" """)


                #Yes play
                if choice_play.lower() == "yes" or choice_play.lower() == "y":
                    print ("""
The girl's face lights up.  "Okay" she says, "I want to
play hide and seek.  You hide first and I'll try to find you!" "Okay.  What are you
counting too?"  "Twenty. Ready, set, . . . GO!!!" she shouted.  You turn and hurry
out of the room.  You can hear her slowly counting behind you.  You decide to go back
to the staircase.  You'll hide in the little gap under the stairs.""")
                    
                    print ("""
You finally get in there and crouch under the stairs.  You had just gotten situated when
you feel something next to you.  "Found you." she whispered as you felt her hands
wrapped around your neck.""")
                    
                    print ("""
When the hour was up and you didn't come out of the house, your friends tried to go in.
They couldn't open the doors or windows.  They eventually called the police.  Your body
was never found. """)



                #No play
                elif choice_play.lower() == "no" or "n":
                    print ("""
You suddenly get very angry and annoyed with the girl.  "No!  We're not playing!"  The girl's
eyes grow moist.  "You're so mean.  And you're no fun!" she says and promptly disappears.
You step back surprised.  "There is no way that just happened," you say.  You walk in
a daze out of the room and go into the living room.

When the hour is up, you head out to your friend's car.  "Well damn, you actually did
it!  I owe you fifty bucks."  You get in the car and drive away.""")


            #No return to room
            elif choice_return_to_room.lower() == "no" or "n": 
                print ("""
There is nothing in there to keep you safe.  And, whatever is making that noise probably heard
you break the door.""")


                #leave house
                choice_leave_house = input ("""
"Do you leave the house?  You'll lose the bet." """)



                #Yes leave house
                if choice_leave_house.lower() == "yes" or choice_leave_house.lower() == "y":
                    print ("""
You quietly head back down stairs.  You walk down the hall toward the front door.  You twist
the knob and throw open the door.  As you fly out the door, you hear very quietly,
"I just wanted to play."  You run down to the street toward your friend's car.  "Hey %s, it
hasn't been an hour.  Pay up.  $50."  You dig into your pocket and toss him the money.
"Now get out of here!" you shout.  Your friends turn and look at you as you drive away.
"I'm never going in there again!" """ % (player_name))



                #No leave house
                elif choice_leave_house.lower() == "no" or "n":
                    print ("""
No!  You can't leave.  You have $50 at stake.  It was just some funny noises, what could possibly
be in here that would be super dangerous. "Unfortunatly for you, those were your last thoughts.
As you finished thinking that, you heard whispered behind you, 'I want to play.'

When the hour was up and you didn't come out of the house, your friends tried to go in. They
couldn't open the doors or windows.  They eventually called the police.  Your body was never found." """)



    #No to investigate noise    

    elif choice_investigate.lower() == "no" or "n":

        print ("""

You're not sure what's making the noise, but it probably isn't good.""")



        #Find weapon
        choice_find_weapon = input ("""
"You decide it might be best to find a semidecent weapon.  Do you pick out a weapon?" """)



        #Yes find weapon
        if choice_find_weapon.lower() == "yes" or choice_find_weapon.lower() == "y":
            print ("""
It takes some digging, but you eventually find a sceptre that seems solid enough.  You straighten
yourself out and turn around. You jump in shock.  A little girl is standing there.  Blood covers
the girls face and a large cut can be seen on her forehead. "Do you want to play?" she says. """)



            #Runaway
            choice_runaway = input ("""
"Do you run away? """)



            #Yes runaway
            if choice_runaway.lower() == "yes" or choice_runaway.lower() == "y":
                
                print ("""
You forget about your weapon and sprint out of the room, pushing the girl out of the way.  You slink through the
living room.  When you get to the hallway, you sprint toward the front door.  You grabbed the
doorknob, but then stopped.""")



                #Leave house

                choice_leave_house = input ("""
"You could leave now, but then you would lose the bet.  Do you leave?" """)



                #Yes leave house

                if choice_leave_house.lower() == "yes" or choice_leave_house.lower() == "y":

                    print ("""
You twist the knob and through open the door.  As you fly out the door, you
hear very quietly, "I just wanted to play."  You run down to the street toward
your friend's car.  "Hey %s, it hasn't been an hour.  Pay up.  $50."  You
dig into your pocket and toss him the money.  "Now get out of here!" you shout.
Your friends turn and look at you as you drive away.  "I'm never going in there
again!" """ % (player_name))



                #No leave house
                elif choice_leave_house.lower() == "no" or "n":
                    print ("""
No!  You can't leave.  You have $50 at stake.  It was just a little girl.  What harm could she do?
"Unfortunatly for you, those were your last thoughts.  As you finished thinking that, you heard
whispered behind you, 'I always loved chase.'

Your body was never found." """)

                    
        #No find weapon
        elif choice_find_weapon.lower() == "no" or "n":
            print ("""
You don't need a weapon.  You're perfectly safe!  You dig around in the room to see what you can find.
You straighten yourself out and turn around. You jump in shock.  A little girl is standing there.
Blood covers the girls face and a large cut can be seen on her forehead. "Do you want to play?" she says. """)



            #Runaway
            choice_runaway = input ("""
"Do you run away? """)



            #Yes runaway
            if choice_runaway.lower() == "yes" or choice_runaway.lower() == "y":
                
                print ("""
You sprint out of the room, pushing the girl out of the way.  You slink through the
living room.  When you get to the hallway, you sprint toward the front door.  You grabbed the
doorknob, but then stopped.""")



                #Leave house

                choice_leave_house = input ("""
"You could leave now, but then you would lose the bet.  Do you leave?" """)



                #Yes leave house

                if choice_leave_house.lower() == "yes" or choice_leave_house.lower() == "y":

                    print ("""
You twist the knob and through open the door.  As you fly out the door, you
hear very quietly, "I just wanted to play."  You run down to the street toward
your friend's car.  "Hey %s, it hasn't been an hour.  Pay up.  $50."  You
dig into your pocket and toss him the money.  "Now get out of here!" you shout.
Your friends turn and look at you as you drive away.  "I'm never going in there
again!" """ % (player_name))



                #No leave house
                elif choice_leave_house.lower() == "no" or "n":
                    print ("""
No!  You can't leave.  You have $50 at stake.  It was just a little girl.  What harm could she do?
"Unfortunatly for you, those were your last thoughts.  As you finished thinking that, you heard
whispered behind you, 'I always loved chase.'

Your body was never found." """)


            #No runaway
            if choice_runaway == "no" or "n":
                #Play
                choice_play = input ("""
"Do you play with the girl?" """)


                #Yes play
                if choice_play.lower() == "yes" or choice_play.lower() == "y":
                    print ("""
The girl's face lights up.  "Okay" she says, "I want to
play hide and seek.  You hide first and I'll try to find you!" "Okay.  What are you
counting too?"  "Twenty. Ready, set, . . . GO!!!" she shouted.  You turn and hurry
out of the room.  You can hear her slowly counting behind you.  You decide to go back
to the staircase.  You'll hide in the little gap under the stairs.""")
                    
                    print ("""
You finally get in there and crouch under the stairs.  You had just gotten situated when
you feel something next to you.  "Found you." she whispered as you felt her hands
wrapped around your neck.""")
                    
                    print ("""
When the hour was up and you didn't come out of the house, your friends tried to go in.
They couldn't open the doors or windows.  They eventually called the police.  Your body
was never found. """)



                #No play
                elif choice_play.lower() == "no" or "n":
                    print ("""
You suddenly get very angry and annoyed with the girl.  "No!  We're not playing!"  The girl's
eyes grow moist.  "You're so mean.  And you're no fun!" she says and promptly disappears.
You step back surprised.  "There is no way that just happened," you say.  You walk in
a daze out of the room and go into the living room.

When the hour is up, you head out to your friend's car.  "Well damn, you actually did
it!  I owe you fifty bucks."  You get in the car and drive away.""")


