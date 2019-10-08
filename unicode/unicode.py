s1 = 'hello'
s2 = '猫'

with open("ascii", 'w', encoding="ascii") as f:
    f.write(s1)
    try:
        f.write(s2)
    except:
        pass

with open("utf16", 'w', encoding="utf-16") as f:
    f.write(s1)
    f.write(s2)

with open("utf32", 'w', encoding="utf-32") as f:
    f.write(s1)
    f.write(s2)

with open("utf8", 'w', encoding="utf-8") as f:
    f.write(s1)
    f.write(s2)
