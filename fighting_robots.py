import random
import argparse

 
class Robot():
     
    __illegal_names = {"Henry", "Oscar"}
    __crucial_health_level = 0.6
 
    def __init__(self, name):
        self.name = name  
        self.health_level = random.random()
 
    @property
    def name(self):
        return self.__name
 
    @name.setter
    def name(self, name):
        if name in Robot.__illegal_names:
            self.__name = "Marvin"
        else:
            self.__name = name
 
    def __str__(self):
        return self.name + ", Robot"
 
    def __add__(self, other):
        first = self.name.split("-")[0]
        second = other.name.split("-")[0]
        return type(self)(first + "-" + second)
     
    def needs_a_nurse(self):
        if self.health_level < Robot.__crucial_health_level:
            return True
        else:
            return False
 
    def say_hi(self):
        print("Hi, I am " + self.name)
        print("My health level is: " + str(self.health_level))
 
 
class NursingRobot(Robot):
 
    def __init__(self, name="Hubert", healing_power=None):
        super().__init__(name)
        if healing_power:
            self.healing_power = healing_power
        else:
            self.healing_power = random.uniform(0.8, 1)
    
    def say_hi(self):
        print("I am a nurse robot " + self.name)
 
    def say_hi_to_doc(self):
        Robot.say_hi(self)
 
    def heal(self, robo):
        if robo.health_level > self.healing_power:
            print(self.name + " not strong enough to heal " + robo.name)
        else:
            robo.health_level = random.uniform(robo.health_level, self.healing_power)
            print(robo.name + " has been healed by " + self.name + "!")


class FightingRobot(Robot):
     
    __maximum_damage = 0.2
  
    def __init__(self, name="Hubert", fighting_power=None):
        super().__init__(name)
        if fighting_power:
            self.fighting_power = fighting_power
        else:
            max_dam = FightingRobot.__maximum_damage
            self.fighting_power = random.uniform(max_dam, 1)
     
    def say_hi(self):
        print("I am the fighting Robot " + self.name)
 
    def attack(self, other):
        other.health_level = \
                    other.health_level * self.fighting_power
        #if isinstance(other, FightingRobot):
            # the other robot fights back
        #    self.health_level = \
        #            self.health_level * other.fighting_power


class FightingNurseRobot(NursingRobot, FightingRobot):
    
    def __init__(self, name, mode="nursing"):
        super().__init__(name)
        self.mode = mode    # alternatively "fighting"

    def say_hi(self):
        if self.mode == "fighting":
            FightingRobot.say_hi(self)
        elif self.mode == "nursing":
            NursingRobot.say_hi(self)
        else:
            Robot.say_hi(self)      



def main():
    player_name = str(input("What do you want to name your robot? "))
    opponent_name = str(input("Choose your opponent name: "))
    fn2 = FightingNurseRobot(player_name)
    fn2.say_hi()
    fn1 = FightingNurseRobot(opponent_name, mode="fighting")
    print("I'm your opponent, " + opponent_name)
    print("Let's play!")
    

    quit = False 
    while not quit: 
        player_action = str(input("Press F to fight and H to heal and Q to quit. "))
        if player_action.lower() == 'q': 
            break
        print(opponent_name + " attacked you!")
        fn1.attack(fn2)
        if player_action.lower() == 'f': 
            fn2.attack(fn1)
            print('You attacked ' + opponent_name + '!')
        elif player_action.lower() == 'h': 
            fn2.heal(fn2)
            print('You healed yourself!')
        print('Your health level is ' + str(round(fn2.health_level,3)))
        print('Your opponent\'s health level is ' + str(round(fn1.health_level,3)))
        if fn1.health_level < 0.005 and fn1.health_level < fn2.health_level: 
            print("You win! Good job " + player_name)
            return True  
        elif fn2.health_level < 0.005 and fn1.health_level > fn2.health_level: 
            print("Aw, you lost! Beter luck next time.")
            quit = True 
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