num = int(input())

for i in range(num):
    sentence = input()
    if sentence == 'P=NP':
        print('skipped')
    else:
        sentence2 = sentence.split('+')
        print(int(sentence2[0]) + int(sentence2[1]))