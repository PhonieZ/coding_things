def findbond():
    counter=0
    right_entries=0
    daniel = ["daniel","craig","daniel craig","dan"]
    pierce = ["pierce","brosnan","pierce brosnan"]
    roger = ["roger","moore","roger moore","rog"]
    sean = ["sean","connery","sean connery","conner"]
    valid = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    while counter<=2:
        actor_name=input("Name an actor : ")
        message = ""
        actor_name = actor_name.lower()
        if any(daniel in actor_name for daniel in daniel)  == True and all(c in valid for c in actor_name) == True:
            actor_name = daniel[0].capitalize()+" "+daniel[1].capitalize()
            message = actor_name+" was Bond in Skyfall"
            right_entries += 1
            counter += 1
        elif any(pierce in actor_name for pierce in pierce) == True and all(c in valid for c in actor_name) == True:
            actor_name = pierce[0].capitalize()+" "+pierce[1].capitalize()
            message = actor_name+" was Bond in Die Another Day"
            right_entries += 1
            counter += 1
        elif any(roger in actor_name for roger in roger) == True and all(c in valid for c in actor_name) == True :
            actor_name = roger[0].capitalize()+" "+roger[1].capitalize()
            message = actor_name+" was Bond in Moonraker"
            right_entries += 1
            counter += 1
        elif any(sean in actor_name for sean in sean) == True and all(c in valid for c in actor_name) == True :
            actor_name = sean[0].capitalize()+" "+sean[1].capitalize()
            message = actor_name+" was Bond From Russia With Love"
            right_entries += 1
            counter += 1
        elif all(c in valid for c in actor_name) == True:
            message = "No Record Found Or Might Not Have Played As Bond"
            counter += 1
        elif any(valid not in actor_name for valid in valid) == True:
            message = "Invalid Characters"
        else:
            print("what")
        print(message)
    print("You got "+str(right_entries)+" right answers  out of 3 tries.")

findbond()
