spelldict = {}
spelldict["Cantrips"] = [
    {
        'name':'test',
        'disc':'test',
        'damage':'test'
    },
    {
        'name':'test2',
        'disc':'test2',
        'damage':'test2'
    }
]

print(spelldict['Cantrips'][0]['name'])

for c in spelldict['Cantrips']:
    print(c['name'])