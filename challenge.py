import itertools
from itertools import combinations
wordslist = {'call','me','ball','tall', 'i', 'am'}
letters = {
    2: ['a','b','c'],
    3: ['d','e','f'],
    4: ['g','h','i'],
    5: ['j','k','l'],
    6: ['m','n','o'],
    7: ['p','q','r','s'],
    8: ['t','u','v'],
    9: ['w','x','y','z']
}
alph_num_dict = {'a': '2', 'b': '2', 'c': '2',\
 'd': '3', 'e': '3', 'f': '3',\
 'g': '4', 'h': '4', 'i': '4',\
 'j': '5', 'k': '5', 'l': '5',\
 'm': '6', 'n': '6', 'o': '6',\
 'p': '7', 'q': '7', 'r': '7', 's': '7',\
 't':'8','u': '8', 'w': '9', 'v': '8',\
 'w': '9', 'x': '9', 'y': '9', 'z': '9'}
def dictionary(wlist):
    s7 = []
    s8 = []
    g1 = ''
    for p1 in wlist:
        s7.append(list(alph_to_num(p1)))
    for p2 in s7:
        g1 = ''
        for n1 in range(0,len(p2)):
            g1 = g1 + p2[n1]
        s8.append(str(g1)) 
    return s8
def perm1(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return[lst]
    else:
        l = []
        for d in range(len(lst)):
            x = lst[d]
            xs = lst[:d] + lst[d+1:]
            for r in perm1(xs):
                l.append([x]+r)
        return l
def alph_to_num(phone):
    for index in range(len(phone)):
        p = phone[index]

        if p in alph_num_dict:
            yield alph_num_dict[p]
        else:
            yield p
number = input("Enter the number as a String: ")
def findwords(number):
    letter_combi = set(''.join(w) for w in itertools.product(*[letters[int(n)] for n in number]))
    letter_combi_ls = list(letter_combi)
    s = []
    for p in letter_combi_ls:
        subword = set(p[c:n] for c,n in itertools.product(range(0,(len(p))),range(1,(len(p)+1))))
        s.append(subword) 
    s4 = []
    for s1 in s:
        if s1&wordslist!=set([]):
            s4.append(s1&wordslist)
    s5 = [];
    for a1 in s4:
        s5.append(list(a1));
    s6 = []
    for a2 in s5:
        s6.append(a2[0])
    s6 = set(s6)
    s6 = list(s6)
    s7 = []
    g1 = ''
    s8 = []
    sorted(s6, key=lambda x: len(s6))

    for p1 in s6:
        s7.append(list(alph_to_num(p1)))
    for p2 in s7:
        g1 = ''
        for n1 in range(0,len(p2)):
            g1 = g1 + p2[n1]
        s8.append(str(g1)) 
    wlist = list(wordslist)
    s9 = dictionary(wlist)
    s10 = []
    s11 = []
    s16 = perm1(s6)
    for d2 in s16:
        for k2 in range(1,len(d2)+1):
            combwords = [''.join(k) for k in itertools.combinations([d2[n6] for n6 in range(0,len(d2))],k2)]
            s10.append(combwords)
    for d3 in s10:
        d4 = dictionary(d3)
        s11.append(d4)
    s12 = []
    s20 = []
    s40 = []
    for m3 in s11:
        for h3 in range(0,len(m3)):
            if(m3[h3]==number):
                need1 = s11.index(m3)
                need2 = h3
                s20.append(s10[need1][need2])
    s40 = set(s20)
    print(s40)

findwords(number)


