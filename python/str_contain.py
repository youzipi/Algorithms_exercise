#coding=utf-8
"""
������s1,s2���ж�s2�Ƿ���s1��ѭ����λ���ַ����д���
"""

s1 = 'abcd'
s2 = 'da'
s3 = 'bbc'
def contain1(s,ss):
    length = len(s)
    for i in range(length):
        temp = s[i:]+s[:i]
        if ss in temp:
            print temp
            return True
    return False
    
def contain2(s,ss):
    length = len(s)
    temp = s+s
    if ss in temp:
        print temp
        return True
    return False

print contain1(s1,s2)
print contain1(s1,s3)
print contain2(s1,s2)
print contain2(s1,s3)
    
    