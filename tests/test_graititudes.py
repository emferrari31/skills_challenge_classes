from lib.gratitudes import *

"""
Given multiple gratitudes 
We can see a nice list of them 
"""

def test_multiple_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("my cat")
    gratitudes.add("the sun")
    gratitudes.add("my friends")
    result = gratitudes.format()
    assert result == "I am grateful for: my cat, the sun, and my friends."