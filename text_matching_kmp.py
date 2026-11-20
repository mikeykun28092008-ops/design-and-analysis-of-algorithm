def kmp_search(text, pattern):
    if pattern=="": return list(range(len(text)+1))
    lps=[0]*len(pattern); j=0
    for i in range(1,len(pattern)):
        while j and pattern[i]!=pattern[j]: j=lps[j-1]
        if pattern[i]==pattern[j]: j+=1; lps[i]=j
    matches=[]; i=j=0
    while i<len(text):
        if text[i]==pattern[j]: i+=1; j+=1
        if j==len(pattern): matches.append(i-j); j=lps[j-1]
        elif i<len(text) and text[i]!=pattern[j]:
            if j: j=lps[j-1]
            else: i+=1
    return matches

if __name__ == "__main__":
    print(kmp_search("ABABDABACDABABCABAB","ABABCABAB"))
