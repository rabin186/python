def unpack(lists):
    if len(lists) == 0:
        print('')
    elif len(lists) == 1:
        print(lists[0])
    else:
        print(', ' .join(lists[:-1]) + ' and ' + lists[-1] )
grocery = ['Rice', 'Sugar', 'Tea_Leaves']
unpack(grocery)


grocery = []
unpack(grocery)

grocery = ['Rice']
unpack(grocery)

