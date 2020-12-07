def ConcatERemove(s,t,k):
    st = list(s)
    tt = list(t)
    num = 0
    col = 0
    while (col < len(s)):
        if col < len(t):
           if st[col] != tt[col]:
               st[col] = " "
               num = num + 1
        else:
            st[col] = " "
            num = num + 1
        col = col + 1
    col = 0
    while (col < len(t)):
        if st[col] == " ":
            st[col] = tt[col]
            num = num + 1
        col = col + 1
    if int(k) >= num:
        return "sim"
    else:
        return "nao"

s = input("Insira a string inicial       ")
t = input("Insira a string desejada      ")
k = input("insira o numero de movimentos ")

retorno = ConcatERemove(s,t,k)
print (retorno)
