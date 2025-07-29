birthday = {'Ram':'April 10','Hari':'May 5','Sita':'Feb 9'}

while True:
    print('Enter a name: (blank to quit)')
    name = input('>').capitalize()

    if name == '':
        break

    elif name in birthday:
        print(f'{name} has a birthday on {birthday[name]}')

    else:
        print('No information found in our database for ' + name)


