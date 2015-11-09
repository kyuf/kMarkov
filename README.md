#kMarkov

kMarkov uses Markov chaining to generate random text based on a given
.txt file. The user will be prompted for a .txt file, prefix length,
and the number of words to be generated. The prefix length sets the
number of sequential words used to determine the next word to be
generated. Longer prefix lengths will produce more sensible sentences
but may also start to resemble sentences in the source text. It is up
to the user to determine what prefix length best suits his/her needs.
kMarkov is written using Python 3.4

Current Features
--------

*Markov text generation
*Reads in .txt files
*User sets prefix length and number of words generated

Instructions
--------

Enter the following in your command line

    python3 markov_generator.py

Enter the name of the source .txt file (ie. text.txt)

    text.txt

Enter an integer prefix length

    2

Enter the number of words to be generated

    20
    
The program will then display the randomly generated text
