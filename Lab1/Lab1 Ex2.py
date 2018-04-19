def string_check(test):
    if len(test) < 2:
        print('String is too short, Please try another!')
    else:
        print(len(test))
        for i in test[:1]:
            print('+1\n')
            print(test[i])
        #for g in test[1:]
            #print('-1\n')
            #print(test[g])'''

print('Enter a string\n')

sen = str(input())

string_check(sen)

