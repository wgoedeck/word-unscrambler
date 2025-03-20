# word-unscrambler
This program will input a scrambled word and return a proper spell-checked word, e.g., "lisnad" becomes "island."

### Description of program <a class="anchor" id="description"></a>

This program will input a scrambled word and return a proper spell-checked word. 

To use this algorithm, pyspellchecker must be installed, i.e., "pip install pyspellchecker" by the command prompt (c.f., https://pypi.org/project/pyspellchecker/).

The principle function, "permutations," is recursive, calling itself until a word under construction is complete, then the word is spell-checked. The "permutations" function also requires an initial string that will contain the built-up word, "word," to be tested, and a set, "word_set," that will contain any proper words discovered by the algorithm and when finished, returned by the function. 

All permutations of the input scrambled letters are checked. The "permutations" function starts by selecting the first letter of the scrambled letters given to it as a set. A set will cull repeat letters, e.g., "parallel" reduces to "parle," and "mississippi" reduces to "misp."

Once a letter of the set is selected, the scrambled letters, "letters," are checked for the first occurrence of the letter, which is then noted as "index." These two arguments are sent to the function "prune_letters," which will return the letters minus the indexed letter, e.g., with index = 0, pointing to the letter 'e,' prune_letters("eht", 0) returns "ht." the string variable "word" will append the indexed letter, 'e.'

The remaining letters, "ht" will then be sent back through the permutations function, and the process repeated, with "word" then appending the letter 'h' to become "eh" and the function "prune_word" will return 't.' Another iteration through the "permutations" function will return only the remaining 't,' and the next iteration will append this 't' to "word," which will become "eht." Since all the letters are used, the word is spell-checked; in this particular case it is not a true word. 

The next iteration will generate the word cluster "eth" which is supposedly a proper word, which is then appended into word_set. 

An example illustrate the process. Consider the scrambled word "eht." When the print statements are uncommented, the output is: 

    Enter a scrambled word: eht
    e
    eh
    eht
    not a word: eht 

    et
    eth
    good word: eth, added to word_set
    word_set: {'eth'}

    h
    he
    het
    not a word: het

    ht
    hte
    not a word: hte

    t
    te
    teh
    not a word: teh

    th
    the
    good word: the, added to word_set
    word_set: {'eth', 'the'}

    {'eth', 'the'}
    
Notice how the words are built by one letter at a time, and when the word has used up all the input letters, it is checked for spelling. The recursion function allows all the permutations to be checked, and when a proper word is found, it is added to the set, "word_set." In this example, "eth" and "the" are proper words. 
