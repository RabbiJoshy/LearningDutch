import pandas as pd
import math
from googletrans import Translator
import os

df = pd.read_xml('Dutch/en-nl.xml')

from chatgpt_wrapper import ChatGPT

bot = ChatGPT()
response = bot.ask("write a sentence in dutch using the words 'redden' and 'wakker' with an english translation")

print(response)