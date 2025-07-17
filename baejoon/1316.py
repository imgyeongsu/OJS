T = int(input())

group_words = 0
for _ in range(T):
    words = input()
    w = set()
    w.add(words[0])
    is_group = True
    pre_spell = words[0]
    for i in range(1, len(words)):
        spell = words[i]
        if pre_spell == spell:
            continue
        else:
            if spell in w:
                is_group = False
                break
            else:
                w.add(spell)    
            pre_spell = spell
            
    if is_group:
        group_words +=1
        print(words)
print(group_words)
