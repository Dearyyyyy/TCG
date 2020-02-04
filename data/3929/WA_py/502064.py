def com(a):
        return a[0][0]
while True:
    n = raw_input()
    if n:
        n=int(n)
        c=[0]*55
        for i in range(0,n,):
            c[i] = raw_input()
            c[i] = c[i].split(' ')
            c[i][0] = c[i][0].split(':')
            a = (int(c[i][0][0])-18) * 60
            a += int(c[i][0][1])
            c[i][0][0] = a

        mp=range(30)
        for i in range(0,30):
            mp[i]=0

        #c.sort(key=com)
        s=0
        for i in range(0,n):
            if(c[i][2]=='AC')and(mp[ord(c[i][1][0])-65]!=-1):
                s+=c[i][0][0]+mp[ord(c[i][1][0])-65]*20
                mp[ord(c[i][1][0])-65]=-1
            elif(mp[ord(c[i][1][0])-65]!=-1):
                mp[ord(c[i][1][0])-65]+=1

        print '%02d:%02d'%(s/60,s%60)
    else:
        break