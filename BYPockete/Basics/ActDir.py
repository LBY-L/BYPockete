import os
def ActDir():
    ActDirecory = os.path.dirname(os.path.abspath(__file__))
    ActDir = ActDirecory.replace("Basics", "")
    return ActDir