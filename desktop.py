import os

def finddesktop():

    user=os.environ['USERPROFILE']
    target=f'{user}\Desktop'.replace('''\ ''','''/''')
    try:
        os.chdir(target)
        d=target
    except:pass
    try:
        dire=f'{user}\OneDrive\Desktop'.replace('''\ ''','''/''')
        os.chdir(dire)
        d=dire

    except:pass

    os.chdir(d)

    try:
        os.chdir('animo')
    except:
        os.mkdir('animo')
        os.chdir('animo')
        with open('readme.txt', 'w') as f:
            f.write('''follow me in instagram : https://www.instagram.com/jidukrishnapj/
buy me samoosas  <|`* - *`|>
if u have any doubt plz ask me ''')
    return os.getcwd()
