from itertools import combinations

def solution(P, Q):
    letters = {}
    dist_let = []
    for i in range(len(P)):
        if P[i] not in letters:
            letters[P[i]] = set()
        letters[P[i]].add(Q[i])
        if Q[i] not in letters:
            letters[Q[i]] = set()
        letters[Q[i]].add(P[i])
        
    for key in letters.keys():
        dist_let.append(key)

    for i in range(1, len(letters) +1):
        for let_comb in combinations(letters, i):
            let_range = set()
            for letter in let_comb:
                let_range.update(letters[letter])
                let_range.add(letter)
            need_to_cover = set()
            for key, value in letters.items():
                if key not in let_comb:
                    need_to_cover.update(value)
            if set(let_comb).issuperset(need_to_cover):
                return i

                
    #literki z key muszą byc w stanie pokryc wszystkie values
    #dla wszystkich key ktore nie sa w kombinacji zrobic połączony set z values i puscic na to test isuper
    

print(solution('aaadb', 'bbbdc'))
print(solution('abcdef', 'fabcde'))
print(solution('ab', 'de'))