from ast import pattern
from cgi import print_arguments, test
from dataclasses import replace
from hashlib import new
import re
from timeit import repeat
from traceback import print_tb


def prompt(sublist,storylist,storyindex):
    global newword
    newword = input("What's your word for {typeofword}".format(typeofword=sublist))
    storylist[storyindex] = newword


string1 = "It was ___(FOOD)___ day at school, and ___(NAME)___ was super ___(ADJECTIVE)___ for lunch. But when she went outside to eat, a ___(NOUN)___ stole her ___(FOOD)___! ___(NAME)___ chased the ___(NOUN)___ all over school. She ___(VERB1)___, ___(VERB2)___, and ___(VERB3)___ through the playground. Then she tripped on her ___(NOUN)___ and the ___(NOUN)___ escaped! Luckily, ___(NAME)___’s friends were willing to share their ___(FOOD)___ with her."
blanks = re.findall(r'___\(.+?\)___',string1)
string1list = string1.split()


test1 = [i for i, s in enumerate(string1list, start=0) if re.search(r'___\(.+?\)___', s)] 
for x in range(0,len(blanks)):
    prompt(blanks[x],string1list,test1[x])

seperator = " "
newstory = seperator.join(string1list)
print(newstory)
