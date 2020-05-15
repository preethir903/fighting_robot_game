import random
import argparse


class Robot():
    '''
    Generic robot class- some of this code is built using the tutorial specified in the README as a template
    param: str name 
    '''
    __counter = 0 #class attribute: number of times one has used this class 
    __critical_health_level = 0.1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    _class_info = 'Generic Robot' #added class info 

    def __init__(self, name = None): #added none clause to init 
        if name: 
            self.__name = name
        else:
            self.__name = "No Name"
        self.health_level = 0.5 
    
    @classmethod #added class method
    def about(cls):
        print("This class is about " + cls._class_info + "!")   

    @staticmethod #added counting method 
    def counting(): #number of times this class has been used
        return self.__counter
 
    @property
    def name(self):
        return self.__name
 
    @name.setter
    def name(self, name):
        self.__name = name
 
    def __str__(self): #editted 
        return "Hi, I'm " + self.name + " Robot"
        
    def __lt__(self, other): #added magic methods
        return self.health_level < other.health_level
    
    def __gt__(self, other):
        return self.health_level > other.health_level
    
    def __eq__(self, other):
        return self.health_level == other.health_level
    
    @property
    def needs_a_nurse(self): 
        if self.health_level < self.__critical_health_level: 
            return True
        else:
            return False
 
 
class NursingRobot(Robot):
    
    _class_info = "Nursing Robot" #added class info
    
    def __init__(self, name= "Nurse"):
        super().__init__(name)
        self.healing_power = random.uniform(0.8, 1)
         
    def heal(self, robo): 
        if robo.health_level > self.healing_power:
            print(self.name + " not strong enough to heal " + robo.name)
        else:
            robo.health_level = random.uniform(robo.health_level, self.healing_power)
            print(robo.name + " has been healed by " + self.name + "!")
            
    def heal_myself(self): #added new function to heal self 
        self.heal(self, self)
        
    
class FightingRobot(Robot):
     
    __maximum_damage = 0.2
    _class_info = "Fighting Robot"
  
    def __init__(self, name="Fighter"):
        super().__init__(name)
        max_dam = FightingRobot.__maximum_damage
        self.fighting_power = random.uniform(max_dam, 1) #editted 
 
    def attack(self, other): #editted - new functions, block and attack back 
        if isinstance(other, FightingRobot) or isinstance(other, FightingNurseRobot): 
            chance_of_block = random.uniform(0, 1)
            if chance_of_block > 0.2:  
                other.health_level = other.health_level * self.fighting_power
            else: 
                #the other robot blocks the attack- NEW
                print(other.name + ' blocked ' +  self.name + "'s" + ' attack!')
                if chance_of_block < 0.05: 
                    #robot scratches back also - NEW
                    print(other.name + ' scratched '+ self.name + '!')
                    self.health_level = self.health_level * other.fighting_power * 0.3
        else: 
            other.health_level = other.health_level * self.fighting_power
            print(self.name + " successfully attacked!")


class FightingNurseRobot(NursingRobot, FightingRobot):
    '''
    Cleaned up class and removed additional functionalities 
    '''
    _class_info = "Fighting Nurse Robot"
    
    def __init__(self, name):
        super().__init__(name)


#From now on, all this code is new (outside the tutorial)
class ChaosRobot(FightingNurseRobot): 
    '''
    THISIS A NEW CLASS - NOVEL CODE - Chaos robot randomly helps or heals
    '''
    _class_info = "Chaos Robot"
    
    def __init__(self, name):
        super().__init__(name)
        
    def do_chaos(self, you_robot, opponent): 
        self.chaos_chance = random.uniform(0, 1)
        if self.chaos_chance < 0.5: #do nothing
            print('Chaos robot is chilling!')
        elif self.chaos_chance > 0.5 and self.chaos_chance < 0.6: #heal opponent
            self.heal(opponent) 
            print("Chaos robot healed your opponent!")
        elif self.chaos_chance > 0.6 and self.chaos_chance < 0.7: #heal you 
            self.heal(you_robot)  
            print("Chaos robot healed you!")
        elif self.chaos_chance > 0.7 and self.chaos_chance < 0.8: #attack opponent
            self.attack(opponent) 
            print("Chaos robot attacked you!")
        elif self.chaos_chance > 0.8 and self.chaos_chance < 0.9: #attack you 
            self.attack(you_robot)  
            print("Chaos robot attacked you!")
        else: #random action- singing
            print('Chaos robot starting singing Michael Jackson!') 


def main():
    player_name = str(input("What do you want to name your robot? "))
    fn2 = FightingNurseRobot(player_name)
    print(fn2)
    change_name = str(input("Do you want to change your name? Enter 'No' or a new name: ")).lower()
    if change_name != 'no': 
        fn2.name = change_name
        print(fn2)
    opponent_name = str(input("Choose your opponent's name: "))
    fn1 = FightingNurseRobot(opponent_name)
    print("I'm your opponent, " + opponent_name)
    print("Let's play!")
    chaos_robot = ChaosRobot('Chaos')
    print('By the way... there\'s also a chaos robot who likes to do things, so watch out!')

    quit = False 
    while not quit: 
        player_action = str(input("Press F to fight and H to heal and Q to quit. "))
        if player_action.lower() == 'q': 
            break
        print(opponent_name + " attacked you!")
        fn1.attack(fn2)
        if player_action.lower() == 'f': 
            print('You attacked ' + opponent_name + '!')
            fn2.attack(fn1)
        elif player_action.lower() == 'h': 
            fn2.heal(fn2)
        chaos_robot.do_chaos(fn2, fn1)
        
        print('Your health level is ' + str(round(fn2.health_level,3)) + '. ' + 'Your opponent\'s health level is ' + str(round(fn1.health_level,3)))
        if fn1.health_level < 0.005 and fn1.health_level < fn2.health_level: 
            print("You win! Good job " + player_name)
            return True  
        elif fn2.health_level < 0.005 and fn1.health_level > fn2.health_level: 
            print("Aw, you lost! Beter luck next time.")
            quit = True 
        elif fn2.needs_a_nurse: 
            print("Health level critical. Please heal yourself!")
        else: 
            quit = False 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Enter user name.')
    parser.add_argument('--name', help='enter a string wtih your name')
    args = parser.parse_args()
    if args.name: 
        print("Welcome to the fighting robot game " + args.name + "!")
    else: 
        print("Welcome to the fighting robot game!")
    main()
