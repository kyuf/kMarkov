'''
Markov Generator
'''
import random
import re
import os    

#prefix class
class Prefix:
    def __init__(self, suffix, next_prefix):
        self.suffix = [suffix]
        self.next_prefix = [next_prefix]
        
    def add_suffix(self, suffix, next_prefix):
        self.suffix.append(suffix)
        self.next_prefix.append(next_prefix)
    
    def pick_random_suffix(self):
        r = random.randrange(len(self.suffix))
        return self.suffix[r], self.next_prefix[r]

#text class
class TextData:
    #on intialization, create dictionary of prefixes
    #key: prefix, value: list of suffixes
    def __init__(self, words, p_len):
        if len(words) <= 2:
            raise ValueError('Need at least 3 words')
        self.words = words
        self.p_len = p_len
        self.prefix_dict = {}
        #iterate through word list and extract slices equal to p_len
        prefix = ' '.join(words[0:p_len])
        for i in range(1, len(self.words) - self.p_len + 1):
            next_prefix = ' '.join(words[i:i+self.p_len])
            if prefix in self.prefix_dict:
                self.prefix_dict[prefix].add_suffix(
                    self.words[i+self.p_len-1], next_prefix
                    )
            else:
                self.prefix_dict[prefix] = Prefix(
                    self.words[i+self.p_len-1], next_prefix
                    )
            prefix = next_prefix
        
        self.pick_random_prefix()
        self.choose_suffix()
    
    #pick a random prefix
    def pick_random_prefix(self):
        self.prefix = random.choice(list(self.prefix_dict.keys()))
    
    #choose a random suffix from list stored under current prefix
    def choose_suffix(self):
        self.suffix, self.next_prefix = self.prefix_dict[self.prefix].pick_random_suffix()
    
    #update prefix by removing first word and attaching suffix
    def update_prefix(self):
        self.prefix = self.next_prefix
        #pick a new random prefix if no suffix available
        while self.prefix not in self.prefix_dict:
            self.pick_random_prefix()
        self.choose_suffix()
    
    #generate text
    def generate(self, num):
        generated_text = []
        for i in range(num):
            generated_text.append(self.suffix)
            self.update_prefix()
        print('')
        print(' '.join(generated_text))
    
    #set prefix, used for testing
    def set_prefix(self, prefix):
        self.prefix = prefix
    
    #set suffix, used for testing
    def set_suffix(self, suffix):
        self.suffix = suffix
    
    def get_suffix(self):
        return self.suffix
    
    def get_prefix_dict(self):
        return self.prefix_dict
    
    def get_prefix(self):
        return self.prefix

def main():
    os.system('clear')
    
    print('This is a Markov Generator\n')
    
    #prompt user for text file
    while True:
        file_name = input('Enter .txt file name (ie. text.txt): ')
        #check if file has .txt ending
        if re.search('\.txt$', file_name) == None:
            print('Must enter .txt file')
        else:
            try:
                #read text file and create word list
                with open(file_name, 'r') as f:
                    words = [word for line in f for word in line.split()]
                #check if file has more than one word
                if len(words) < 2:
                    print('File must contain at least 2 words')
                else:
                    break
            except:
                print('File name not found')
    
    #prompt user for prefix length
    while True:
        p_len = input('Enter prefix length: ')
        #prefix length must be an integer
        try:
            p_len = int(p_len)
        except:
            print('Prefix length must be an integer')
            continue
        #check if length is within bounds
        if p_len < 1 or p_len >= len(words):
            print('Prefix length must be greater than 0 and less than the number of words in text')
        else:
            break
    
    #prompt user for number of words to generate
    while True:
        n_gen = input('Enter number of words to generate: ')
        try:
            n_gen = int(n_gen)
            break
        except:
            print('Number must be an integer')
    
    text = TextData(words, p_len)
    
    text.generate(n_gen)

if __name__ == '__main__':
    main()
