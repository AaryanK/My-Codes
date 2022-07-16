def _file(action):
    if action == 'open':
        _file = open('rawdata.txt')
        return _file
    elif action == 'close':
        try:
            _file.close()
        except:
            pass



f = _file('open')
print([index for index, value in enumerate(f.readlines()) if value == 'eticket\n'])