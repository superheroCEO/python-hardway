class ParserError(Exception):
    pass
This is how you make your own ParserError exception class you can throw. Next we need the Sentence object we'll create:

1
2
3
4
5
6
7
class Sentence(object):

    def __init__(self, subject, verb, obj):
        # remember we take ('noun','princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]
...some if it anyway....

