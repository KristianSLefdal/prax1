phonebook = {'Noroff': '38 00 00 00' ,'Playstation': '56 99 93 10' , 'Apple': '23 00 00 00' , 'IBM':'49 00 00 00', 'DELL':'99 00 00 00'}
print(phonebook)

search_dict = input('company reasearch: ')

if search_dict in phonebook:
	print(phonebook[search_dict])

for k, v in phonebook.items():
	print(k)
	
