# Manny Pagan
# Sept 24th Python Course
# Assignment 7
# Due: Oct 22nd

new_friends = []
friends = ['Rita', 'Sen', 'Johanis']

class Person:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def get_older(self):
        self.age = self.age + 1
        return self.age

    def about_me(self, name):
        self.name = name
        if self.name is 'Manny':
            print("Hello! I'm Manny and I'm " + str(self.age) + " years old.")
        elif self.name is 'Dale' or 'Stacey':
            print("Hello! I'm " + self.name + " and I'm " + str(self.age) + " years old.")

    def make_friend(self):
        if self.name == 'Dale':
            if 'Rita' not in new_friends:
                new_friends.append('Rita')
            if 'Sen' not in new_friends:
                new_friends.append('Sen')
        elif self.name == 'Stacey':
            new_friends.remove('Rita')
            new_friends.remove('Sen')
            if 'Johanis' not in new_friends:
                new_friends.append('Johanis')
        else:
            pass
        return new_friends

    def talk_about_friends(self):
        print(self.name + "'s friends: ------")
        if new_friends == []:
            print("I don't have any friends yet")
        else:
            for i in new_friends:
                print(i + " is a friend of mine")
        return new_friends

    def all_friends_get_older(self):
        person1.get_older()
        person2.get_older()
        person3.get_older()
        person1.about_me('Dale')
        person2.about_me('Stacey')
        person3.about_me('Manny')


# LEAVE THIS CODE AS IS ---------

person1 = Person('Dale')
person2 = Person('Stacey')
person3 = Person('Manny')
all_friends = [person1, person2, person3]

print()
print("PART 1:")
print()
person1.about_me('Dale')
person2.about_me('Stacey')
print()
person1.get_older()
person1.about_me('Dale')
person1.talk_about_friends()
person1.make_friend()
person1.make_friend()
person1.talk_about_friends()
person1.get_older()
person1.about_me('Dale')
print()
for i in range(10):
    person2.get_older()
person2.about_me('Stacey')
person2.make_friend()
for i in range(15):
    person3.get_older()
person2.talk_about_friends()
print()
person3.about_me('Manny')
print()
print("--------")
print()
print("PART 2:")
print()
print()
person1.all_friends_get_older()
print("--------")
person1.all_friends_get_older()
print("--------")
person1.all_friends_get_older()
print("--------")