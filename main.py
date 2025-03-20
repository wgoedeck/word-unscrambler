import sys
from spellchecker import SpellChecker
spell = SpellChecker()

'''Returns all letters sent to subroutine minus the indexed letter, e.g., letters ="eht"
    and index = 0, so "ht" is returned as pruned_letters.
'''
def prune_letters(letters, index):
    pruned_letters = []
    for i in range(len(letters)):
        if i != index:
            pruned_letters.append(letters[i])
    return pruned_letters

'''Recursive algorithm that accepts scrambled letters, and a string: word, and 
a set: word_set. What's returned are any permutations of the scrambled letters
that form an English spell-checked word in the word_set. 

Uses a python set rather than a list; this will reduce the permutations needed 
by listing only one occurence for each letter, e.g., "parallel" reduces to 
"parle," and "mississippi" reduces to "misp."

word, and word_set are persistant variables that are recursively passed to 
the permutations function, and thus are initialized in main. 
'''
def permutations(letters, word, word_set):
    # Choose a letter in the scrambled word, then build off the other letters.
    for letter in set(letters):
        # Build word, letter by letter.
        new_word = word + letter
        '''Uncomment print statement to see functionality'''
        #print(new_word)
        
        # Find index of first occurence of letter in letters.
        index = letters.index(letter)
        # Call prune_letters to cull scrambled word of particular letter.
        pruned_letters = prune_letters(letters, index)
        
        # When all letters of the scrambled word are used, check the spelling of 
        # the permutated letters to see if indeed it is a word, if so, add it to 
        # the word_set set.
        if pruned_letters == []:
            # Check to see word already in word_set; word_set will contain 
            # all proper words confirmed by spellchecking. 
            if new_word not in word_set:
                # Identify those words that may be misspelled.
                misspelled = spell.unknown([new_word])
                
                # If actual word, add to word_set.
                if not misspelled:
                    word_set.add(new_word)
                    '''Uncomment print statement to see functionality'''
                    #print("good word: {}, added to word_set".format(new_word))
                    #print("word_set: {}\n".format(word_set))
                else: 
                    '''Uncomment print statement to see functionality'''
                    #print("not a word: {}\n".format(new_word))
                    pass
                    
        else: # Letters not used up; continue to recurse the function.
            permutations(pruned_letters, new_word, word_set)

    return word_set

def main(args):
    # Initialize the word string and create a set, rather than a list.
    word = ""
    word_set = set()
    
    # Input the scrambled word. 
    input_var = input("Enter a scrambled word: ")
    #print ("you entered " + input_var) 
    scrambled_word = input_var

    # Call the recursive routine. 
    word_set = permutations(scrambled_word, word, word_set)
    
    print(word_set)
        
    return 0

if __name__ == '__main__':
    spell = SpellChecker()
    try:
        sys.exit(main(sys.argv))
    except: 
        pass  
