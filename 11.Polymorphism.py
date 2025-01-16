# You seen polymorphism before look at here : 
print(2 + 2)
print('2' + '2')
print()
# the same + do 2 different works, it can sum 2 int and also can concatinate '2' and '2'

# now look at here :

class Shark:
    
    def swim(self):
        print('Shark can swim.')

    def swim_back(self):
        print('Shark can not swim back!')

    def skeleton(self):
        print('Shark have a big skeleton!')

class ClownFish:
    
    def swim(self):
        print('ClownFish can swim.')

    def swim_back(self):
        print('ClownFish can not swim back!')

    def skeleton(self):
        print('ClownFish have a big skeleton!')

def poly_morphism(fish):
    fish.swim()
    fish.swim_back()
    fish.skeleton()

shark1 = Shark()
clownfish1 = ClownFish()

poly_morphism(shark1)
print()
poly_morphism(clownfish1)
print()

for fish in (shark1, clownfish1):
    fish.swim()
    fish.swim_back()
    fish.skeleton()
# as you see same function do 2 different things, let's make more polymorphism

# ----------------------------------------------------------------

class Dog :
    
    def sound(self):
        print('Hop Hop, Hop Hop')
    
class Cat:
    
    def sound(self):
        print('Miew Miew, Miew Miew')

def what_it_say(animal_type):
    animal_type.sound()

dog1 = Dog()
cat1 = Cat()

what_it_say(dog1)
what_it_say(cat1)

# this is polymorphism, we have a function but with different inputs we get different outputs

    
    
    
    
    
    
    
    
