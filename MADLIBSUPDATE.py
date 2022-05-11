from ast import pattern
from cgi import print_arguments, test
from dataclasses import replace
from hashlib import new
import re
from timeit import repeat
from traceback import print_tb



story = "It was ___(FOOD)___ day at school, and ___(NAME)___ was super ___(ADJECTIVE)___ for lunch. But when she went outside to eat, a ___(NOUN)___ stole her ___(FOOD)___ ! ___(NAME)___ chased the ___(NOUN)___ all over school. She ___(VERB1)___, ___(VERB2)___, and ___(VERB3)___ through the playground. Then she tripped on her ___(NOUN)___ and the ___(NOUN)___ escaped! Luckily, ___(NAME)___’s friends were willing to share their ___(FOOD)___ with her."



blanks = re.findall(r'(\(.+?\))',story)
blanks = list(set(blanks))
print(blanks)
story_list = story.split()



def prompt(blanks,story_list):
    global new_word
    new_word = input("What's your word for {word_type}".format(word_type=blanks))
    story_index = [i for i, s in enumerate(story_list, start=0) if re.search("{}".format(blanks), s)] #index for the 
    print(story_index)
    for story_indexes in story_index:
        story_list[story_indexes] = new_word
        print(new_word)

for x in range(0,len(blanks)):
    prompt(blanks[x],story_list)


seperator = " "
newstory = seperator.join(story_list)
print(newstory)
