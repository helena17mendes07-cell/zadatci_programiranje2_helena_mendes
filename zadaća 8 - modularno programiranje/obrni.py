def obrni(s):
    if s=="":
        return ""
    else:
        return s[-1] + obrni(s[:-1])
