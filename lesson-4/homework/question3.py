

def modify_text(txt):
    vowels = "aeiouAEIOU"  
    result = []
    i = 0
    while i < len(txt):
        result.append(txt[i])
        if (i + 1) % 3 == 0 and i != len(txt) -1 :
            result.append('_')
        if txt[i] in vowels or (len(result) > 1 and result[-2] == '_'):
            if i + 1 < len(txt): 
                result.append(txt[i + 1])
                result.append('_')
                i+=1 
        i+=1              
    return ''.join(result)

txt = "abcabcdabcdeabcdefabcdefg"
print(modify_text(txt))
