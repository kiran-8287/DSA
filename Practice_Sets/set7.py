#1 Valid Anagram

#Method:
    # Use a Hash Map: Count the frequency of each character in string s. Decrease the counts
    # while scanning string t. If all counts return to zero, then the strings are anagrams.

#Constraints: Assume the strings consist of lowercase English letters.

class HashTable:
    def __init__(self):
        self.arr = []
        for i in range(26):
            self.arr.append(0)
    
    #hash_function(char) = (ord(char) - ord('a')) % 26
    def insert(self,char):
        idx = (ord(char) - ord('a')) % 26
        self.arr[idx] +=1

    def erase(self,char):
        idx = (ord(char) - ord('a')) % 26
        self.arr[idx] -=1
    
    def isempty(self):
        for i in self.arr:
            if(i != 0):
                return False
        return True


def validAnagram(s , t):
    map = HashTable()
    for i in s:
        map.insert(i)
    
    for j in t:
        map.erase(j)
    
    if(map.isempty()):
        return True
    return False

print(validAnagram("anagram", "nagaram"))
print(validAnagram("rat","car"))


#collision handling map
class HashMap:
    def __init__(self,s):
        self.size = len(s)
        self.keys = [None]*self.size
        self.values = [0]*self.size
        self.occupied = [False]*self.size

    def hash_func(self, c):
        return (ord(c) - ord('a'))%self.size

    def insert(self, c):
        idx = self.hash_func(c)
        start_idx = idx
        while(self.occupied[idx] == True and self.keys[idx] != c):
            idx = (idx+1)%self.size
            if(idx == start_idx):
                print("HashTable is full")
                return
        
        if(self.occupied[idx] == False):
            self.occupied[idx] = True
            self.keys[idx] = c
            self.values[idx] = 1
        else:
            self.values[idx] +=1

    def decrement(self, c):
        idx = self.hash_func(c)
        start_idx = idx
        while(self.occupied[idx] == True):
            if(self.keys[idx] == c):
                self.values[idx] -=1
                break
            idx = (idx + 1)%self.size
            if(idx == start_idx):
                break

    def all_zero(self):
        for i in range(self.size):
            if(self.occupied[i] == True):
                if(self.values[i] != 0):
                    return False
        return True
        


def is_anagram(s, t):
    if(len(s) != len(t)):
        return False
    map = HashMap(s)
    for i in s:
        map.insert(i)
    
    for j in t:
        map.decrement(j)
    
    return map.all_zero()


print(is_anagram("anagram", "nagaram"))
print(is_anagram("rat", "car"))


#2 Group Anagrams
class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = [value]
    
class HashMap:
    def __init__(self,words):
        self.size = len(words)
        self.arr = [None]*self.size

    def hash_function(self,word):
        idx = 0
        for char in word:
            idx = (idx*31 + (ord(char)-ord('a')))%self.size
        return idx
    
    def insert(self, word):
        idx = self.hash_function(word)
        key = ''.join(sorted(word))
        start_idx = idx
        
        #search
        while(self.arr[idx] != None and self.arr[idx].key != key):
            idx = (idx+1)%self.size
            if(idx == start_idx):
                print("Map is Full")
                return
        
        #got it
        if(self.arr[idx] == None):
            self.arr[idx] = Node(key,word)
        else:
            self.arr[idx].value.append(word)
    
    def search(self,word):
        idx = self.hash_function(word)
        key = ''.join(sorted(word))
        start_idx = idx
        
        while(self.arr[idx] != None):
            if(self.arr[idx].key == key):
                return True
            idx = (idx+1)%self.size
            if(idx == start_idx):
                return False
        return False
    
    def display(self):
        all_words = []
        for words in self.arr:
            if words != None:
                print(words.value)
                all_words.append(words.value)
        print(all_words)

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
h = HashMap(words)
for word in words:
    h.insert(word)

h.display()