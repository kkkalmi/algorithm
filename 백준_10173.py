while True:
    s = input()
    if s == 'EOI': break
    s = s.lower()
    if 'nemo' in s:
        print('Found')
    else:
        print('Missing')
