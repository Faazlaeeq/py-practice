class SpaceCraft: #spacecraft ki prent class
    def __init__(self,name): #spacecraft ka constructor
        self.name=name #name ki property
        self.fuel_capacity=100 #fuel capacity ki property
        self.currentfuel=80 #current fuel ki property
    def refuel(self,amount): #refuel function
        if(amount<self.fuel_capacity and amount<(self.fuel_capacity-self.currentfuel)): #agar amount fuel capacity se kam hai aur current fuel capacity se bhi kam hai
            self.currentfuel+=amount
        else: #warna exception throw kardo
            raise Exception("Invalid fuel amount")
    def launch(self): #launch function
        if(self.currentfuel>=80): #agar current fuel 80 se zyada hai
            print(f"{self.name} SpaceCraft launched successfully") #print kardo
        else: #warna exception throw kardo
            raise Exception("Insufficent Fuel")
class Rocket(SpaceCraft): #rocket spacecraft ki  child class hai
    def __init__(self,payload_cap): #rocket ka constructor
        super().__init__()  #space craft class ka constructor call kara
        self.payload_capacity=payload_cap #payload capacity ki property
    def add_payload(self,weight_in_tons): #add payload function
        if(weight_in_tons<=self.payload_capacity): #agar weight in tons payload capacity se kam hai
            print("Weight Added") #print kardo
        else: #warna exception throw kardo
            raise Exception("Payload weight limit exceeded")
        
class Shuttle(SpaceCraft): #shuttle spacecraft ki child class hai
    def __init__(self,passenger_cap): #shuttle ka constructor
        super().__init__() #spacecraft class ka constructor call kara
        self.passenger_capacity=passenger_cap #passenger capacity ki property
    def board_passenger(self,number): #board passenger function
        if(number<=self.passenger_capacity): #agar number passenger capacity se kam hai
            print(f"{number} Passengers added on board") #print kardo
        else: #warna exception throw kardo
            raise Exception("Passenger on board limit exceeded")
        

class Astronaut: #astronaut class
    def __init__(self,name,rank,exprience_years,weight): #astronaut ka constructor
        self.name=name
        self.rank=rank
        self.exprience_years=exprience_years
        self.weight=weight
    def assign_to_mission(self,mission): #assign to mission function
        self.mission=mission 
    def display_details(self): #display details function
        print(f"Name:{self.name}\nRank:{self.rank}\nExperience:{self.exprience_years}\nCurrent Mission:{self.mission}")
    
class Mission: #mission class
    def __init__(self,mission_name,spaceCraft:SpaceCraft,crew:list[Astronaut]): #mission ka constructor is kay paramter mein datatype define ki hai parameters ki 
        self.mission_name=mission_name
        self.spaceCraft:SpaceCraft=spaceCraft
        self.crew=crew
    def add_crew(self,astronaut:Astronaut): #add crew function
        if(type(self.spaceCraft)==Rocket): #agar spacecraft rocket ka object hai
            try:
                self.spaceCraft.add_payload(astronaut.weight/1000) #astronaut ki weight ko 1000 se divide karke add payload function call kara kynkay weight tons mein hai
                self.crew.append(astronaut) #crew list mein astronaut ko append kara
            except Exception as e: #agar koi exception aayi
                print(e)
        elif(type(self.spaceCraft)==Shuttle): #agar spacecraft shuttle ka object hai
            try:
                self.crew.append(astronaut) 
                self.spaceCraft.board_passenger(self.crew.__len__()) #crew list ki length ko board passenger function mein pass kara
            except Exception as e: #agar koi exception aayi
                print(e)
        else: #warna exception throw kardo
            raise Exception("Unexpected input")

smallRocket=Rocket(20) #rocket ka object banaya
largeRocket=Rocket(80) #rocket ka object banaya

smallShuttle=Shuttle(2) #shuttle ka object banaya
largeShuttle=Shuttle(15) #shuttle ka object banaya

#astronaut kay obejcts banaye
as01=Astronaut("John","Worker",2,70) 
as02 = Astronaut("Alice", "Commander", 10, 75) 
as03 = Astronaut("Bob", "Engineer", 5, 80)
as04 = Astronaut("Charlie", "Scientist", 7, 85)
as05 = Astronaut("Diana", "Pilot", 3, 90)

mission01= Mission("Mars Mission",smallRocket,smallShuttle,[as01,as02,as03]) #mission ka object banaya

# Test refueling
print("Test refueling:")
smallRocket.refuel(10)
print(smallRocket.currentfuel)  # Expected: 90

# Test exceeding capacity
print("\nTest exceeding capacity:")
try:
    smallRocket.refuel(50)
except Exception as e:
    print(e)  # Expected: "Invalid fuel amount"

# Test launch
print("\nTest launch:")
try:
    smallRocket.launch()
except Exception as e:
    print(e)  # Expected: "Rocket SpaceCraft launched successfully"

# Testing launch with insufficient fuel
print("\nTesting launch with insufficient fuel:")
smallRocket.currentfuel = 50
try:
    smallRocket.launch()
except Exception as e:
    print(e)  # Expected: "Insufficient Fuel"

# Testing add payload
print("\nTesting add payload:")
try:
    smallRocket.add_payload(10)
except Exception as e:
    print(e)  # Expected: "Weight Added"

# Testing add payload exceeding limit
print("\nTesting add payload exceeding limit:")
try:
    smallRocket.add_payload(30)
except Exception as e:
    print(e)  # Expected: "Payload weight limit exceeded"

# Testing add passenger
print("\nTesting add passenger:")
try:
    smallShuttle.board_passenger(5)
except Exception as e:
    print(e)  # Expected: "5 Passengers added on board"

# Testing add passenger exceeding limit
print("\nTesting add passenger exceeding limit:")
try:
    smallShuttle.board_passenger(15)
except Exception as e:
    print(e)  # Expected: "Passenger on board limit exceeded"

# Assign astronaut to mission and display details
print("\nAssign astronaut to mission and display details:")
as01.assign_to_mission("Mars Mission")
as01.display_details()
# Expected:
# Name: John
# Rank: Worker
# Experience: 2
# Current Mission: Mars Mission

# Add crew to mission
print("\nAdd crew to mission:")
mission01.add_crew(as05)
# Expected: "Weight Added"

# Add crew exceeding payload limit
print("\nAdd crew exceeding payload limit:")
as06 = Astronaut("Eve", "Engineer", 6, 30000)
mission01.add_crew(as06)
# Expected: "Payload weight limit exceeded"

# Add crew to shuttle mission
print("\nAdd crew to shuttle mission:")
mission02 = Mission("Lunar Mission", smallShuttle, None, [])
mission02.add_crew(as02)
# Expected: "2 Passengers added on board"

# Add crew exceeding passenger limit
print("\nAdd crew exceeding passenger limit:")
try:
    
    mission02.add_crew(as03)
    mission02.add_crew(as01)
    mission02.add_crew(as05)
except Exception as e:
    print(e)  # Expected: "Passenger on board limit exceeded"
