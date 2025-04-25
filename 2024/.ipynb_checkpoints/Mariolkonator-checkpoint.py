ends = ['!', '.', '?']
mariolkizmy = {'ą': 'om', 'Ą': "Om", 'w': 'f', 'W': 'F', 'r': 'ł', 'R': 'Ł', 'd': 't', 'D': 'T'}
mariolkizmy_2 = {'c': 'c', 'C': 'C', 's': 's', 'S': 'S', 'r': 'sz', 'R': 'Sz', 'd': 'c', 'D': 'C'}

def seplen(txt):
    wysryw = []
    if txt[-1] not in ends:
        txt = txt + '.'
    for i, char in enumerate(txt):
        if char in mariolkizmy.keys():
            wysryw.append(mariolkizmy[char])
        elif (char == 'Z' or char == 'z') and i > 0:
            if txt[i-1] in mariolkizmy_2.keys():
                wysryw[-1] = mariolkizmy_2[txt[i-1]]
            else:
                wysryw.append('s')
        else:
            wysryw.append(char)
    return ''.join(wysryw)

if __name__ == '__main__':
    #print(seplen('Tekst do wpisania na twardo'))
    #print(seplen(input('Podaj tekst do wyseplenienia:')))
    pass