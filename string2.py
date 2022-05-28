# Find Valid Anagram 
class Partha(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        elif sorted(s) == sorted(t):
            return True
        else:
            return False
        
ob1 = Partha()
print(ob1.isAnagram(s = "rat", t = "car"))
print(ob1.isAnagram(s = "anagram", t = "nagaram"))