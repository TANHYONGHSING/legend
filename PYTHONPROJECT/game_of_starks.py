characters = ["Jon Snow", "Daenerys Targaryen", "Tyrion Lannister", "Arya Stark", "Sansa Stark", "Cersei Lannister"]

#character = "Abu Stark"

"""
if character in characters:
    print('Abu Stark is present !')
else:
    print('Abu Stark is not present')
"""
starkWords = 0
for stark in characters: 
    if "Stark" in stark: 
        starkWords = starkWords +1 
print(starkWords)