def isSubsequence(s, t):
    if len(s) > len(t): return False
    if len(s) == 0: return True
    subsequence = 0
    for i in range(0, len(t)):
        if subsequence <= len(s) - 1:
            print(s[subsequence])
            if s[subsequence] == t[i]:
                subsequence += 1
    return subsequence == len(s)

print(isSubsequence("ab", "baab"))