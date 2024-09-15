#lidia pasiecznik
#hw task2
player = False
while player == False:
    print("\t|-------------------------------|")
    print("\t|16/09/24                       |")
    print("\t|                               |")
    print("\t| 1. calendar                   |")
    print("\t| 2. tasks                      |")
    print("\t| 3. reminders                  |")
    print("\t| 4. upcoming events            |")
    print("\t| 5. add event                  |")
    print("\t| 6. add task                   |")
    print("\t|-------------------------------|")
    print("\t|                               |")
    option = input("\t| choose option : ")
    if option == "1":
        print("\t|september\t\t\t|")
        print("\t|  M  T  W  TH F  S  Su\t\t|")
        print("\t|\t             1\t\t| ")
        print("\t|  2  3  4  5  6  7  8\t\t| ")
        print("\t|  9  10 11 12 13 14 15\t\t|")
        print("\t|  16 17 18 19 20 21 22\t\t|")
        print("\t|  23 24 25 26 27 28 29\t\t|")
        print("\t|  30\t\t\t\t|")
        print("\t|-------------------------------|")
    if option == "2":
        print("\t| TASKS\t\t\t\t|")
        print("\t| 1, finish homework\t\t|")
        print("\t| 2, study\t\t\t|")
        print("\t|-------------------------------|")
    if option == "3":
        print("\t| REMINDERS\t\t\t|")
        print("\t| 1, lidia's bday on the 22 oct\t|")
        print("\t| 2, team party in a week 28 sep|")
        print("\t|-------------------------------|")
    if option == "4":
        print("\t| 1, soccer part\t\t|")
        
    if option == "5":
        print("\t| add event ¬", "or to exit press E")
        addEvent = input("\t| 1.")
        if addEvent == "E":
            player == False
    if option == "6":
        print("\t| add task ¬", "or to exit press E")
        addEvent = input("\t| 1.")
        if addEvent == "E":
            player == False
        
        
    
   
    