def anagram(A):
    if(A==None):
        return
    else:
        dict={}
        for i in range(len(A)):
            word=''.join(sorted(A[i]))
            if(word not in dict):
                dict[word]=[i+1]
            else:
                dict[word].append(i + 1)
        return dict

A=['act','dog','god','cat','atc']
print(anagram(A))