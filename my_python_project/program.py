import emoji
from art import *
import pyjokes

My_joke = pyjokes.get_joke(language="en", category="neutral")
print(My_joke)
print(emoji.emojize(":winking_face_with_tongue:"))
art_1=art("happy")
print(art_1)