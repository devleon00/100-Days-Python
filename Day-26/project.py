
from black import out
import pandas

data = pandas.read_csv('./nato_phonetics.csv')
dict_letters = {row.letter: row.code for (index, row) in  data.iterrows()}

user = input('Enter a word: ')
output = [dict_letters[name] for name in user.upper()]
print(output)
