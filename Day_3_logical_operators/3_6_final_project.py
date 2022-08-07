print("""

##############################################################################

Hi stranger!

Welcome in my game called :
""")

print("""

THE


      88          88               ad88  
  ,d    88          ""              d8"    
  88    88                          88     
MM88MMM 88,dPPYba,  88  ,adPPYba, MM88MMM  
  88    88P'    "8a 88 a8P_____88   88     
  88    88       88 88 8PP"""""""   88     
  88,   88       88 88 "8b,   ,aa   88     
  "Y888 88       88 88  `"Ybbd8"'   88 
""")

print(
"""##############################################################################\n\n\n

                     __.------.                          
                      (__  ___   )                         
                        .)e  )\ /                          
                       /_.------                           
                       _/_    _/                           
                   __.'  / '   `-.__                       
                  / <.--'           `\                     
                 /   \   \c           |                    
                /    /    )  GoT  x    \                   
                |   /\    |c     / \.-  \                  
                \__/  )  /(     (   \   <>'\               
                     / _/ _\-    `-. \/_|_ /<>             
                    / /--/,-\     _ \     <>.`.            
                    \/`--\_._) - /   `-/\    `.\           
                     /        `.     /   )     `\          
                     \      \   \___/----'                 
                     |      /    `(                        
 ___________         \    ./\_   _ \                       
   ______________    /     |  )    '|                      
 __________________ |     /   \     \     ___________a:f   
                   /     |     |____.)                     
                  /      \  a88a\___/88888a.               
                 \_      :)8888888888888888888a.           
                /` `-----'  `Y88888888888888888            
                \____|         `88888888888P'
##############################################################################\n\n\n
""")


story_start = input("Can you steal the stolen treasure that the thief is hiding in his hideout?\n\nWrite Yes or No: ")

if story_start == "Yes" or story_start == "yes":
  print("Well done! I think you can handle this dangerous mission!\n\nAnd very well! Your first idea was perfect! Your began step was to walk around and very carefully check the surroundings and the building itself.")
  
  first_move = input("When u checked all ways aroud the hideout you seen 2 best entries to the building. Window on the first floor and half opened Garage doors behind the building. Which way you prefer ?\n\nWrite Garage or Window: ")
  if first_move == "Window" or first_move == "window":
    print("Great job! Room behind the window was clear and full in dark. Now we can move to the other rooms.")
  
   
    second_move = input("You look around the dark room and there's an open door right in front of you, so you go to it and peek into the adjacent hallway.\nThere's no one in the hallway so you walk in and notice two doors, which one do you go to ?\n\nLeft or Right: ")
    if second_move == "Left" or second_move == "left":
      print("In this door is the another dark room, but at the table you can see small light from candle and paper put on the desk so you come closer to the paper and check him. There is something like a code or any of this. Just five random numbers without logic")

      third_move = input("You'r going from the room with the candle to the next corridor and see the stairs.\nThis staircase leads to the first floor. You are go upstairs until you come across another room, but it is locked with bars.\nYou need a key to unlock it. Do you look for the key in the immediate area or do you go somewhere else ?\n\nKey or Go elsewhere: ")
      if third_move == "key" or third_move == "Key":
        print("You are looking around until you notice a pot by your right foot so you look under it and find a key placed there")
  
        fourth_move = input("You'r unlocked the door and went to the room with the big safe inside. But what now ? How it's possible to open the safe ? There are only two options. Be calm and think what now or searching the room and find the clue.\n\nThinking or Searching: ")
        if fourth_move == "Thinking" or fourth_move == "thinking":
          print("Brilliant! You'r so smart! You pulled a piece of paper out of your pocket that was on the table under the candle and used the five-digit code to open the safe")

          fiveth_move = input("Congratz! You taken the treasure from the thief hideout this will be our last mission! We must out from the thieve den without suspect...\nThere are two options. Go out with the same way how we came here or use straight to fast way out.\n\nSame or Fast: ")
          if fiveth_move == "Fast" or fiveth_move == "fast":
            print("Great! the shortcut paid off, you got out quickly and now you'll just enjoy your acquired wealth!")
          
          elif fiveth_move == "Same" or "same":
              print("God damn. When you went into the room with the window and came out, the thief was waiting for you because noticed that the window was too open. He took treasure and stabbed you in the stomach with a knife. You're dead.")
        
        elif fourth_move == "searching" or fourth_move == "Searching":
          print("When u'r searching the room you was too noisy, thief hear you and very fast run to the room with the safe and cut your throat with the knive. You'r dead")
      
      elif third_move == "Go elsewhere" or third_move == "go elsewhere":
        print("You decided to go elsewhere, but on the first floor all the other doors were also locked, so you decided to go back to the ground floor unfortunately on the stairs you slipped and fell at the end of the fall you hit your head. You're dead.")
    
    elif second_move == "Right" or second_move == "right":
      print("After opening this door you can see stairs which going downstairs so u'r going downstairs and met the guy in the garage. He's instantly taking hammer and smasing you to your head. You'r dead.")
      
  elif first_move == "Garage" or first_move == "garage":
    print("When u went inside someone smash your head with the hammer from behind...You are dead.")
    
elif story_start == "No" or story_start == "no":
  print("Oops...even if you wanted to change your mind about your answer it's too late! One of the thief's companions spotted you and has already echoed that something's up.")





