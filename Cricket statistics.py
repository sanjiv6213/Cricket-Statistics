import mysql.connector as my
def db():
    print('\t\t\t\tStatistics Of A Player')
    #To Create a new team or to continue with exisiting team
    print('Enter:\n1. To create new Teamname\n2. To continue with exisiting Teamname')
    while True:
        try:
            hel=int(input('Enter your choice 1 or 2:'))
            if hel==1:
                hell=input('Enter Team Name:')
                mycon=my.connect(host='localhost',user='root',passwd='root') 
                cursor=mycon.cursor()
                while True:
                    try:
                        cursor.execute('Create database {}'.format(hell))
                        break
                    except:
                        print('Database already exist,Please try again')
                        deb()
                        break
                mycon=my.connect(host='localhost',user='root',passwd='root',database=hell)
                cursor=mycon.cursor()
                break
            elif hel==2:
                hell=input('Enter Team Name:')
                while True:
                    try:
                        mycon=my.connect(host='localhost',user='root',passwd='root',database=hell)
                        cursor=mycon.cursor()
                        break
                    except:
                        print('No such database exist,Try again')
                        db()
                        break
            else:
                print('Enter only 1 or 2')
                continue
            break
        except:
            print('Enter only integers 1 or 2')
            continue
    def prg():
        def r(k):
            cursor.execute(k)
        def c():
            cursor.execute('commit')
        while True:
                        while True:
                            try:
                                hs='create table name(name varchar(50))'
                                r(hs)
                                c()
                                break
                            except:
                                break
                        #To View or  create a player's statistics of a team
                        print("Press:\n1.To View details of a Player,\n2.To Create a new statistics for a Player,\n3.Exit")
                        while True:
                            try:
                                ss=int(input("Enter 1 or 2 or 3:"))
                                if ss not in [1,2,3]:
                                    print("Enter only 1 or 2 or 3")
                                    continue
                                else:
                                    break
                            except:
                                print("Enter only 1 or 2 or 3 ")
                                continue
                        if ss==3:
                            break
                        elif int(ss) in [1,2]:
                            def cre():
                              #To create a new player's statistics
                              print('->\tBatting statistics(1)  \n\tBowling statistics(2)')
                              while True:
                                  try:
                                      ll=int(input(('->Enter your choice 1 or 2:')))
                                      il=str(ll)
                                      if il.isdigit:
                                          ill=int(il)
                                          if ill in (1,2):
                                              break
                                          else:
                                              print('Invalid Input')
                                              print('Try Again!!!')
                                              print('Give only 1 or 2')
                                      else:
                                          print('Invalid Input')
                                          print('Try Again!!!')
                                          print('Give only 1 or 2')
                                  except:
                                   print('Invalid Input')
                                   print('Try Again!!!')
                                   print('Give only 1 or 2')
                                   continue
                              r('select name from name')
                              asx=cursor.fetchall()
                              def bat():
                                           #To create  batting statistics for a new player
                                           mmm=input('->Name of the Player:')
                                           m=mmm.lower()
                                           nam='insert into name values("{}")'.format(m)
                                           r(nam)
                                           c()
                                           m=str(m)+'bat'
                                           if ll==1:
                                               while True:
                                                   try:
                                                      r('select * from {}'.format(m))
                                                      print('This name already exist in batting stats')
                                                      print('Try again')
                                                      break
                                                   except:
                                                       while True:
                                                        try:
                                                         n=int(input("->How many match's input you need to upload?:"))
                                                         nn=str(n)
                                                         if nn.isdigit and n>0:
                                                             nnn=int(nn)
                                                             break
                                                         else:
                                                             print('Invalid input,give only positive integers')
                                                             continue
                                                        except:
                                                             print('Invalid Input')
                                                             print('Try Again!!!')
                                                             print('Give only positive integers(numbers)')
                                                             continue
                                                       r('create table {}(Sno int,date varchar(90),runs int,Teambattingfirstorsecond varchar(30),OutorNotout varchar(10),NoofBallsfaced int,Strikerate varchar(30),OpponentTeamName varchar(50),WinorLoss varchar(50))'.format(m,))
                                                       lst=[0]
                                                       for mn in range(n):
                                                           print("->Enter details of ",mn+1,"match")
                                                           lst.append((lst[-1]+1))
                                                           w=lst[-1]
                                                           while True:
                                                               try:
                                                                a=int(input("  *(1)Score in the Match:"))
                                                                aa=str(a)
                                                                if aa.isdigit and a>=0:
                                                                    aaa=int(aa)
                                                                    break
                                                                else:
                                                                    print('Invalid Input,Give only positive integers')
                                                                    continue
                                                               except:
                                                                    print('Invalid Input')
                                                                    print('Try Again!!!')
                                                                    print('Give only positive integers(numbers)')
                                                                    continue
                                                           while True:
                                                               try:
                                                                nj=input("  *(2)Team batting first(f) or second(s):")
                                                                if nj=='f' or nj=='F':
                                                                   x='first batting'
                                                                elif nj=='s' or nj=='S':
                                                                   x='second batting'
                                                                else:
                                                                   print("Invalid Input")
                                                                   print('Try Again!!!')
                                                                   print('Give only f or s')
                                                                   continue
                                                               except:
                                                                   continue
                                                               if nj in ('f','s','F','S'):
                                                                   break
                                                           while True:
                                                               try:
                                                                y=input("  *(3)Batsman OUT(o) or NOT OUT(n):")
                                                                if y=='o' or y=='O':
                                                                   t='out'
                                                                elif y=='n' or y=='N':
                                                                   t='not out'
                                                                else:
                                                                   print('Invalid Input')
                                                                   print('Try Again!!!')
                                                                   print('Give only o or n')
                                                               except:
                                                                   continue
                                                               if y in ('o','n','O','N'):
                                                                   break
                                                           while True:
                                                               try:
                                                                g=int(input("  *(4)Enter no of balls faced by the player:"))
                                                                gg=str(g)
                                                                if gg.isdigit and g>0:
                                                                    ggg=int(gg)
                                                                    break
                                                                else:
                                                                    print('Invalid input, Give only positive inetgers')
                                                                    continue
                                                               except:
                                                                    print('Invalid Input')
                                                                    print('Try Again!!!')
                                                                    print('Give only positive integers(numbers)')
                                                                    continue
                                                           z=(a/g)*100
                                                           ss=input("  *(5)Opponent Team Name:")
                                                           if ss.islower():
                                                               s=ss
                                                           else:
                                                               s=ss.lower()
                                                           while True:
                                                               try:
                                                                h=input("  *(6)Match Won(w) or Loss(l):")
                                                                if h=='w' or h=='W':
                                                                   hh='win'
                                                                elif h=='l' or h=='L':
                                                                   hh='loss'
                                                                else:
                                                                   print('Invalid Input')
                                                                   print('Try Again!!!')
                                                                   print('Give only w or l')
                                                               except:
                                                                   continue
                                                               if h in ('w','l','W','L'):
                                                                   break
                                                           while True:
                                                               try:
                                                                   zx=int(input("  *(4)Enter which year was the match played:"))
                                                                   er=str(zx)
                                                                   if len(er)==4 and er[0]!='0':
                                                                       break
                                                                   else:
                                                                       print('Invalid Input')
                                                                       print('Try Again!!!')
                                                                       print('Enter the entire year')
                                                                       continue
                                                               except:
                                                                   print('Invalid Input')
                                                                   print('Try Again!!!')
                                                                   print('Enter the entire year')
                                                                   continue
                                                           zx=str(zx)
                                                           while True:
                                                               try:
                                                                   xy=int(input("  *(5)Which month was the match played(Enter in number):"))
                                                                   if xy in (1,2,3,4,5,6,7,8,9,10,11,12):
                                                                       re=str(xy)
                                                                       if len(re)==1:
                                                                           rew='0'+re
                                                                           break
                                                                       else:
                                                                           rew=xy
                                                                           break
                                                                   else:
                                                                       print('Invalid Input')
                                                                       print('Try Again!!!')
                                                                       print('Enter the correct month')
                                                               except:
                                                                   print('Invalid Input')
                                                                   print('Try Again!!!')
                                                                   print('Enter the correct month')
                                                                   continue
                                                           df=str(rew)
                                                           while True:
                                                               try:
                                                                   we=int(input("  *(6)Enter the day on which the game was played:"))
                                                                   if xy==2:
                                                                       if int(zx)%4==0:
                                                                           if we>29 or we<0:
                                                                               print('Invalid Input')
                                                                               print('Try Again!!!')
                                                                               print('Enter the correct date')
                                                                               continue
                                                                           elif we<=29 and we>0:
                                                                               ew=str(we)
                                                                               if len(ew)==1:
                                                                                   tre='0'+ew
                                                                                   break
                                                                               else:
                                                                                   tre=we
                                                                                   break
                                                                       else:
                                                                            if we>28 or we<0:
                                                                                print('Invalid Input')
                                                                                print('Try Again!!!')
                                                                                print('Enter the correct date')
                                                                                continue
                                                                            elif we<=28 and we>0:
                                                                               ew=str(we)
                                                                               if len(ew)==1:
                                                                                   tre='0'+ew
                                                                                   break
                                                                               else:
                                                                                   tre=we
                                                                                   break  
                                                                   elif xy==1 or xy==3 or xy==5 or xy==7 or xy==8 or xy==10 or xy==12:
                                                                       if we>31 or we<0:
                                                                           print('Invalid Input')
                                                                           print('Try Again!!!')
                                                                           print('Enter the correct date')
                                                                           continue
                                                                       elif we<=31 and we>0:
                                                                           ew=str(we)
                                                                           if len(ew)==1:
                                                                               tre='0'+ew
                                                                               break
                                                                           else:
                                                                               tre=we
                                                                               break
                                                                       else:
                                                                           break
                                                                   elif xy==4 or xy==6 or xy==9 or xy==11:
                                                                       if we>30 or we<0:
                                                                           print('Invalid Input')
                                                                           print('Try Again!!!')
                                                                           print('Enter the correct date')
                                                                           continue
                                                                       elif we<=30 and we>0:
                                                                           ew=str(we)
                                                                           if len(ew)==1:
                                                                               tre='0'+ew
                                                                               break
                                                                           else:
                                                                               tre=we
                                                                               break
                                                                       else:
                                                                           break
                                                                   else:
                                                                           print('Invalid Input')
                                                                           print('Try Again!!!')
                                                                           print('Enter the correct date')
                                                                           continue
                                                                   wsk=str(tre)
                                                               except:
                                                                     print('Invalid Input')
                                                                     print('Try Again!!!')
                                                                     print('Enter the correct date')
                                                                     continue
                                                           wsk=str(tre)
                                                           qwe=wsk+''+df+''+zx
                                                           p='insert into {} values({},"{}",{},"{}","{}",{},"{}","{}","{}");'.format(m,w,qwe,aaa,x,t,ggg,z,s,hh)
                                                           r(p)
                                                           c()
                                                           print('Table has been created for the player')
                                                       while True:
                                                           prg()
                                                           break
                                                       break
                              def bowl():
                                     #To create bowling statistics for a new player
                                     if ll==2:
                                        mmm=input('->Name of the Player:')
                                        m=mmm.lower()
                                        nam='insert into name values("{}")'.format(m)
                                        r(nam)
                                        c()
                                        m=str(m)+'bowl' 
                                        while True:
                                          try:
                                             r('select * from {}'.format(m))
                                             print('This name already exist in bowling stats')
                                             print('Please try again')
                                             m=0
                                             break
                                          except:
                                              if m!=0:
                                                  while True:
                                                    try:
                                                     n=int(input("->How many match's input you need to give?:"))
                                                     nn=str(n)
                                                     if nn.isdigit and n>0:
                                                         nnn=int(nn)
                                                         break
                                                     else:
                                                         print('Invalid input,give only positive integers')
                                                         continue
                                                    except:
                                                         print('Invalid Input')
                                                         print('Try Again!!!')
                                                         print('Give only positive integers(numbers)')
                                                         continue
                                                  while True:
                                                        try:
                                                            k='create table {}(Sno int,date varchar(20),totnoofwickets int,noofovers int,noofrunsgivenbybowler int(10))'.format(m,)
                                                            r(k)
                                                            break
                                                        except:
                                                            break
                                                  lst=[0]
                                                  for abc in range(n):
                                                      print("->Enter details of ",abc+1,"match")
                                                      lst.append((lst[-1]+1))
                                                      w=lst[-1]
                                                      while True:
                                                          try:
                                                           x=int(input("  *(1)Number of wickets taken by the bowler:"))
                                                           xx=str(x)
                                                           if xx.isdigit and x>=0:
                                                               xxx=int(xx)
                                                               break
                                                           else:
                                                               print('Invalid Input')
                                                               print('Try Again!!!')
                                                               print('Give only positive integers(numbers)')
                                                               continue
                                                          except:
                                                               print('Invalid Input')
                                                               print('Try Again!!!')
                                                               print('Give only positive integers(numbers)')
                                                               continue
                                                      while True:
                                                          try:
                                                           z=int(input("  *(2)Number of overs bowled:"))
                                                           zz=str(z)
                                                           if zz.isdigit and z>0:
                                                               zzz=int(zz)
                                                               break
                                                          except:
                                                               print('Invalid Input')
                                                               print('Try Again!!!')
                                                               print('Give only positive integers(numbers)')
                                                               continue
                                                      while True:
                                                          try:
                                                           zn=int(input("  *(3)Number of runs given by the bowler:"))
                                                           zzn=str(zn)
                                                           if zzn.isdigit and zn>=0:
                                                               zzzn=int(zzn)
                                                               break
                                                          except:
                                                               print('Invalid Input')
                                                               print('Try Again!!!')
                                                               print('Give only positive integers(numbers)')
                                                               continue
                                                      while True:
                                                            try:
                                                                zx=int(input("  *(4)Enter which year was the match played:"))
                                                                er=str(zx)
                                                                if len(er)==4 and er[0]!='0':
                                                                    zx=zx
                                                                    break
                                                                else:
                                                                    print('Invalid Input')
                                                                    print('Try Again!!!')
                                                                    print('Enter the entire year')
                                                                    continue
                                                                zx=str(zx)
                                                            except:
                                                                print('Invalid Input')
                                                                print('Try Again!!!')
                                                                print('Enter the entire year')
                                                                continue
                                                      zx=str(zx)
                                                      while True:
                                                            try:
                                                                xy=int(input("  *(5)Which month was the match played(Enter in number):"))
                                                                if xy in (1,2,3,4,5,6,7,8,9,10,11,12):
                                                                    re=str(xy)
                                                                    if len(re)==1:
                                                                        rew='0'+re
                                                                        break
                                                                    else:
                                                                        rew=xy
                                                                        break
                                                                else:
                                                                    print('Invalid Input')
                                                                    print('Try Again!!!')
                                                                    print('Enter the correct month')
                                                                df=str(rew)
                                                            except:
                                                                print('Invalid Input')
                                                                print('Try Again!!!')
                                                                print('Enter the correct month')
                                                                continue
                                                      df=str(rew)
                                                      while True:
                                                            try:
                                                                we=int(input("  *(6)Enter the day on which the game was played:"))
                                                                if xy==2:
                                                                    if int(zx)%4==0:
                                                                        if we>29 or we<0:
                                                                            print('Invalid Input')
                                                                            print('Try Again!!!')
                                                                            print('Enter the correct date')
                                                                            continue
                                                                        elif we<=29 and we>0:
                                                                            ew=str(we)
                                                                            if len(ew)==1:
                                                                                tre='0'+ew
                                                                                break
                                                                            else:
                                                                                tre=we
                                                                                break
                                                                    else:
                                                                         if we>28 or we<0:
                                                                             print('Invalid Input')
                                                                             print('Try Again!!!')
                                                                             print('Enter the correct date')
                                                                             continue
                                                                         elif we<=28 and we>0:
                                                                            ew=str(we)
                                                                            if len(ew)==1:
                                                                                tre='0'+ew
                                                                                break
                                                                            else:
                                                                                tre=we
                                                                                break 
                                                                elif xy==1 or xy==3 or xy==5 or xy==7 or xy==8 or xy==10 or xy==12:
                                                                    if we>31 or we<0:
                                                                        print('Invalid Input')
                                                                        print('Try Again!!!')
                                                                        print('Enter the correct date')
                                                                        continue
                                                                    elif we<=31 and we>0:
                                                                        ew=str(we)
                                                                        if len(ew)==1:
                                                                            tre='0'+ew
                                                                            break
                                                                        else:
                                                                            tre=we
                                                                            break
                                                                    else:
                                                                        break
                                                                elif xy==4 or xy==6 or xy==9 or xy==11:
                                                                    if we>30 or we<0:
                                                                        print('Invalid Input')
                                                                        print('Try Again!!!')
                                                                        print('Enter the correct date')
                                                                        continue
                                                                    elif we<=30 and we>0:
                                                                        ew=str(we)
                                                                        if len(ew)==1:
                                                                            tre='0'+ew
                                                                            break
                                                                        else:
                                                                            tre=we
                                                                            break
                                                                    else:
                                                                        break
                                                                else:
                                                                        print('Invalid Input')
                                                                        print('Try Again!!!')
                                                                        print('Enter the correct date')
                                                                        continue
                                                                wsl=str(tre)
                                                            except:
                                                                  print('Invalid Input')
                                                                  print('Try Again!!!')
                                                                  print('Enter the correct date')
                                                                  continue
                                                      wsl=str(tre)
                                                      qwe=wsl+''+df+''+zx
                                                      p='insert into {} values({},{},{},{},{});'.format(m,w,qwe,xxx,zzz,zzzn)
                                                      r(p)
                                                      c()
                                                      print('Table has been created for the player')
                                                  while True:
                                                      prg()
                                                      break
                                          break
                              if ll==1:
                                  bat()
                              elif ll==2:
                                bowl()
                            def vie():
                                            #To view statistics of a player
                                            n=input("Enter player name:")
                                            n=n.lower()
                                            while True:
                                                r('select name from name')
                                                asw=cursor.fetchall()
                                                if (n,) not in asw:
                                                    print('No such player exist in the database')
                                                    while True:
                                                       try:
                                                            afg=int(input('Press \n1)Create stats for new player,\n2)Back to home,\n3)To view another player stats,\n4)View all players name\n5)Exit'))
                                                            if afg==1:
                                                               cre()
                                                               break
                                                            elif afg==2:
                                                                prg()
                                                                break
                                                            elif afg==5:
                                                                break
                                                            elif afg==3:
                                                                vie()
                                                                break
                                                            elif afg==4:
                                                                    kkk=[]
                                                                    mnm=0
                                                                    r('select name from name')
                                                                    fgh=cursor.fetchall()
                                                                    for j in fgh:
                                                                        while True:
                                                                            try:
                                                                                if j[0][-1:-4:-1]=='tab':
                                                                                    j=j[0]-j[0][-1:-4:-1]
                                                                                    j=j[-1::-1]
                                                                                    if j not in kkk:
                                                                                        kkk+=[j]
                                                                                break
                                                                            except:
                                                                                break
                                                                        while True:
                                                                            try:
                                                                                if j[[0][-1:-5:-1]]=='lowb':
                                                                                    j=j[0]-j[0][-1:-5:-1]
                                                                                    j=j[-1::-1]
                                                                                    if j not in kkk:
                                                                                        kkk+=[j]
                                                                                break
                                                                            except:
                                                                                break
                                                                        if j not in kkk:
                                                                            kkk+=[j]
                                                                    for bvb in kkk:
                                                                        if bvb[0]!=None:
                                                                            print(mnm+1,bvb[0])
                                                                            mnm+=1
                                                                    while True:
                                                                        try:
                                                                            afg=int(input('Press\n1)Create stats for player,\n2)Back to home,\n3)To view another player stats,\n4)Exit'))
                                                                            if afg==1:
                                                                                cre()
                                                                                break
                                                                            elif afg==2:
                                                                                prg()
                                                                                break
                                                                            elif afg==4:
                                                                                break
                                                                            elif afg==3:
                                                                                vie()
                                                                                break
                                                                            else:
                                                                                print('Enter only 1 or 2 or 3 or 4')
                                                                                continue
                                                                        except:
                                                                            print('Enter only 1 or 2 or 3 or 4')
                                                                            continue
                                                                    break
                                                            else:
                                                                print('Enter only 1 or 2 or 3 or 4 or 5')
                                                                continue
                                                            break
                                                       except:
                                                            print('Enter only 1 or 2 or 3 or 4 orn 5')
                                                            continue
                                                break
                                            pap=[]
                                            for j in asw:
                                               for k in j:
                                                   pap+=[k]
                                            if (n,) in asw:
                                                if n in pap:
                                                                #viewing statistics of a player in different aspects
                                                                while True:
                                                                    try:
                                                                        mut=int(input('Enter \n1.View overall batting statistics\n2.View overall bowling statistics\n3.View overall both bowling and batting statistics\n4.View all matches batting statistics\n5.View all matches bowling statistcs\n6.View all players names'))
                                                                        break
                                                                    except:
                                                                        print('Enter only 1 or 2 or 3 or 4 or 5 or 6')
                                                                        continue
                                                                if mut==6:
                                                                    kkk=[]
                                                                    mnm=0
                                                                    r('select name from name')
                                                                    fgh=cursor.fetchall()
                                                                    for j in fgh:
                                                                        while True:
                                                                            try:
                                                                                if j[0][-1:-4:-1]=='tab':
                                                                                    j=j[0]-j[0][-1:-4:-1]
                                                                                    j=j[-1::-1]
                                                                                    if j not in kkk:
                                                                                        kkk+=[j]
                                                                                break
                                                                            except:
                                                                                break
                                                                        while True:
                                                                            try:
                                                                                if j[[0][-1:-5:-1]]=='lowb':
                                                                                    j=j[0]-j[0][-1:-5:-1]
                                                                                    j=j[-1::-1]
                                                                                    if j not in kkk:
                                                                                        kkk+=[j]
                                                                                break
                                                                            except:
                                                                                break
                                                                        if j not in kkk:
                                                                            kkk+=[j]
                                                                    for bvb in kkk:
                                                                        if bvb[0]!=None:
                                                                            print(mnm+1,bvb[0])
                                                                            mnm+=1
                                                                    while True:
                                                                        try:
                                                                            afg=int(input('Press\n1)Create stats for player,\n2)Back to home,\n3)To view another player stats,\n4)Exit'))
                                                                            if afg==1:
                                                                                cre()
                                                                                break
                                                                            elif afg==2:
                                                                                prg()
                                                                                break
                                                                            elif afg==4:
                                                                                break
                                                                            elif afg==3:
                                                                                vie()
                                                                                break
                                                                            else:
                                                                                print('Enter only 1 or 2 or 3 or 4')
                                                                                continue
                                                                        except:
                                                                            print('Enter only 1 or 2 or 3 or 4')
                                                                            continue
                                                                if mut==4:
                                                                    kgf=n+'bat'
                                                                    while True:
                                                                        try:
                                                                            r('select * from {}'.format(kgf))
                                                                            lop=cursor.fetchall()
                                                                            for j in lop:
                                                                                print('Match',lop.index(j)+1)
                                                                                print('*date:',j[1])
                                                                                print('*Score:',j[2])
                                                                                print('*First or second batting:',j[3])
                                                                                print('*Out or Not Out:',j[4])
                                                                                print('*Number of balls faces:',j[5])
                                                                                print('*Strikerate:',j[6])
                                                                                print('*Opponent team:',j[7])
                                                                                print('*Win or loss:',j[8],'\n')
                                                                            while True:
                                                                                try:
                                                                                    afg=int(input('Press \n1)Create stats for player,\n2)Back to home,\n3)To view another player stats,\n4)Exit'))
                                                                                    if afg==1:
                                                                                        cre()
                                                                                        break
                                                                                    elif afg==2:
                                                                                        prg()
                                                                                        break
                                                                                    elif afg==4:
                                                                                        break
                                                                                    elif afg==3:
                                                                                        vie()
                                                                                        break
                                                                                    else:
                                                                                        print('Enter only 1 or 2 or 3 or 4')
                                                                                        continue
                                                                                except:
                                                                                    print('Enter only 1 or 2 or 3 or 4')
                                                                                    continue
                                                                            break
                                                                        except:
                                                                            print('No batting statistics is existing')
                                                                            while True:
                                                                                        try:
                                                                                            afg=int(input('Press \n1)Create stats for player,\n2)Back to home,\n3)To view another player stats,\n4)Exit'))
                                                                                            if afg==1:
                                                                                                cre()
                                                                                                break
                                                                                            elif afg==2:
                                                                                                prg()
                                                                                                break
                                                                                            elif afg==4:
                                                                                                break
                                                                                            elif afg==3:
                                                                                                vie()
                                                                                                break
                                                                                            else:
                                                                                                print('enter only 1 or 2 or 3 or 4')
                                                                                                continue
                                                                                        except:
                                                                                            print('enter only 1 or 2 or 3 or 4')
                                                                                            continue
                                                                            break
                                                                elif mut==2:
                                                                    bowl='create table Bowlinginfo(noofmatchesbowled int,totnoofwickets int,totnoof3wickets int,totnoof5wickets int,economy float)'
                                                                    r(bowl)
                                                                    kgf=n+'bowl'
                                                                    while 1:
                                                                        try:
                                                                            r('select * from {}'.format(kgf))
                                                                            l=cursor.fetchall()
                                                                            break
                                                                        except:
                                                                            print('No bowling stats availabe for the player')
                                                                            while True:
                                                                                try:
                                                                                    afg=int(input('Press \n1)Create stats for player,\n2)Back to home,\n3)To view another player stats,\n4)Exit'))
                                                                                    if afg==1:
                                                                                        cre()
                                                                                        break
                                                                                    elif afg==2:
                                                                                        prg()
                                                                                        break
                                                                                    elif afg==4:
                                                                                        break
                                                                                    elif afg==3:
                                                                                        vie()
                                                                                        break
                                                                                    else:
                                                                                        print('Enter only 1 or 2 or 3 or 4')
                                                                                        continue
                                                                                except:
                                                                                    print('Enter only 1 or 2 or 3 or 4')
                                                                                    continue
                                                                    noofmatchesbowled=len(l)
                                                                    o=0
                                                                    w3=w5=0
                                                                    economy=[]
                                                                    for j in l:
                                                                        if j[2]>=3 and j[2]<5:
                                                                            w3+=1
                                                                        elif j[2]>=5:
                                                                            w5+=1
                                                                        o+=j[2]
                                                                        economy+=[j[4]/j[3]]
                                                                    totnoofwickets=o
                                                                    fvf=0
                                                                    for k in economy:
                                                                       fvf+=k
                                                                    toteonomy=fvf/len(l)
                                                                    r('insert into Bowlinginfo values({},{},{},{},{})'.format(noofmatchesbowled,totnoofwickets,w3,w5,toteonomy))
                                                                    ank='select * from Bowlinginfo'
                                                                    r(ank)
                                                                    llll=cursor.fetchall()
                                                                    for k in range(len(llll)):
                                                                        print('*No of matches bowled:\t',llll[k][0])
                                                                        print('*Total no of wickets:\t',llll[k][1])
                                                                        print('*Total no of 3 wickets:\t',llll[k][2])
                                                                        print('*Total no of 5 wickets:\t',llll[k][3])
                                                                        print('*Overall Economy:\t',llll[k][4])
                                                                    r('drop table Bowlinginfo')
                                                                    c()
                                                                    while True:
                                                                        try:
                                                                            afg=int(input('Press \n1)Create stats for player,\n2)Back to home,\n3)To view another player stats,\n4)Exit'))
                                                                            if afg==1:
                                                                                cre()
                                                                                break
                                                                            elif afg==2:
                                                                                prg()
                                                                                break
                                                                            elif afg==4:
                                                                                break
                                                                            elif afg==3:
                                                                                vie()
                                                                                break
                                                                            else:
                                                                                print('Enter only 1 or 2 or 3 or 4')
                                                                                continue
                                                                        except:
                                                                            print('Enter only 1 or 2 or 3 or 4')
                                                                            continue
                                                                elif mut==3:
                                                                    noof30s=0
                                                                    noof50s=0
                                                                    noof100s=0
                                                                    n=n+'bat'
                                                                    while True:
                                                                        try:
                                                                            r('select * from {}'.format(n))
                                                                            l=cursor.fetchall()
                                                                            break
                                                                        except:
                                                                            print('\nNo Batting statistics is existing\n')
                                                                            while True:
                                                                                try:
                                                                                    afg=int(input('Press \n1)Create stats for player,\n2)Back to home,\n3)To view another player stats,\n4)Exit'))
                                                                                    if afg==1:
                                                                                        cre()
                                                                                        break
                                                                                    elif afg==2:
                                                                                        prg()
                                                                                        break
                                                                                    elif afg==4:
                                                                                        break
                                                                                    elif afg==3:
                                                                                        vie()
                                                                                        break
                                                                                    else:
                                                                                        print('Enter only 1 or 2 or 3 or 4')
                                                                                        continue
                                                                                except:
                                                                                    print('Enter only 1 or 2 or 3 or 4')
                                                                                    continue
                                                                        break
                                                                    stri=0
                                                                    while True:
                                                                        try:
                                                                                for b in range(0,len(l)):
                                                                                    cvv=l[b][-3]
                                                                                    stri=stri+float(cvv)
                                                                                strikerate=stri/len(l)
                                                                                ru=0
                                                                                for b in range(len(l)):
                                                                                    tt=l[b][2]
                                                                                    ru=ru+int(tt)
                                                                                totruns=ru
                                                                                cc=[0]
                                                                                for b in range(len(l)):
                                                                                    bb=l[b][2]
                                                                                    if int(bb)>cc[-1]:
                                                                                        cc=[int(bb)]
                                                                                highestruns=cc[-1]
                                                                                r('select OpponentTeamname from {} where runs={}'.format(n,highestruns))
                                                                                v=cursor.fetchall()
                                                                                bb=v[0][0]
                                                                                highrunsagainst=bb
                                                                                for b in range(len(l)):
                                                                                    if float(l[b][2])>=30 and float(l[b][2])<50:
                                                                                        noof30s+=1
                                                                                    elif float(l[b][2])>=50 and float(l[b][2])<100:
                                                                                        noof50s+=1
                                                                                    elif float(l[b][2])>=100:
                                                                                        noof100s+=1
                                                                                noofmatchesbat=len(l)
                                                                                count=0
                                                                                for j in range(len(l)):
                                                                                    bb=l[b][4]
                                                                                    if bb=='out':
                                                                                        count+=1
                                                                                if count!=0:
                                                                                    average=totruns/count
                                                                                else:
                                                                                    average=totruns
                                                                                while True:
                                                                                    try:
                                                                                        bat='create table Battinginfo(noofmatchesbat int,Average float,Highestscore int,Highestscoreagainstteam varchar(30),noof50s int,noof100s int,totnoof30s int,strikerate float,totalruns int)'
                                                                                        r(bat)
                                                                                        break
                                                                                    except:
                                                                                        r('drop table Battinginfo')
                                                                                        bat='create table Battinginfo(noofmatchesbat int,Average float,Highestscore int,Highestscoreagainstteam varchar(30),noof50s int,noof100s int,totnoof30s int,strikerate float,totalruns int)'
                                                                                        r(bat)
                                                                                        c()
                                                                                        break
                                                                                r('insert into Battinginfo values({},{},{},"{}",{},{},{},{},{})'.format(noofmatchesbat,average, highestruns,highrunsagainst,noof50s,noof100s,noof30s,strikerate,totruns))
                                                                                c()
                                                                                ank='select * from Battinginfo'
                                                                                r(ank)
                                                                                llll=cursor.fetchall()
                                                                                for k in range(len(llll)):
                                                                                    print('1)Bating statistics:')
                                                                                    print('*No of matches bat:\t',llll[k][0])
                                                                                    print('*Average:\t',llll[k][1])
                                                                                    print('*Highest runs:\t',llll[k][2])
                                                                                    print('*Highest runs against:\t',llll[k][3])
                                                                                    print('*No of 50s:\t',llll[k][4])
                                                                                    print('*No of 100s:\t',llll[k][5])
                                                                                    print('*No of 30s:\t',llll[k][6])
                                                                                    print('*Strikerate:\t',llll[k][7])
                                                                                    print('*Total runs:\t',llll[k][8])
                                                                                sr='drop table Battinginfo'
                                                                                r(sr)
                                                                                c()
                                                                                break
                                                                        except:
                                                                            break
                                                                    bowl='create table Bowlinginfo(noofmatchesbowled int,totnoofwickets int,totnoof3wickets int,totnoof5wickets int,economy float)'#best
                                                                    r(bowl)
                                                                    kgf=n[:len(n)-3]+'bowl'
                                                                    while True:
                                                                        try:
                                                                            r('select * from {}'.format(kgf))
                                                                            l=cursor.fetchall()
                                                                            break
                                                                        except:
                                                                            print('No bowling stats availabe for the player')
                                                                            while True:
                                                                                try:
                                                                                    afg=int(input('Press \n1)Create stats for player,\n2)Back to home,\n3)To view another player stats,\n4)Exit'))
                                                                                    if afg==1:
                                                                                        cre()
                                                                                        break
                                                                                    elif afg==2:
                                                                                        prg()
                                                                                        break
                                                                                    elif afg==4:
                                                                                        break
                                                                                    elif afg==3:
                                                                                        vie()
                                                                                        break
                                                                                    else:
                                                                                        print('Enter only 1 or 2 or 3 or 4')
                                                                                        continue
                                                                                except:
                                                                                    print('Enter only 1 or 2 or 3 or 4')
                                                                                    continue
                                                                            break
                                                                    noofmatchesbowled=len(l)
                                                                    o=0
                                                                    w3=w5=0
                                                                    economy=[]
                                                                    for j in l:
                                                                        if j[2]>=3 and j[2]<5:
                                                                            w3+=1
                                                                        elif j[2]>=5:
                                                                            w5+=1
                                                                        o+=j[2]
                                                                        economy+=[j[4]/j[3]]
                                                                    totnoofwickets=o
                                                                    fvf=0
                                                                    for k in economy:
                                                                       fvf+=k
                                                                    toteonomy=fvf/len(l)
                                                                    r('insert into Bowlinginfo values({},{},{},{},{})'.format(noofmatchesbowled,totnoofwickets,w3,w5,toteonomy))
                                                                    ank='select * from Bowlinginfo'
                                                                    r(ank)
                                                                    llll=cursor.fetchall()
                                                                    for k in range(len(llll)):
                                                                        print('\n2)Bowling statistics')
                                                                        print('*No of matches bowled:\t',llll[k][0])
                                                                        print('*Total no of wickets:\t',llll[k][1])
                                                                        print('*Total no of 3 wickets:\t',llll[k][2])
                                                                        print('*Total no of 5 wickets:\t',llll[k][3])
                                                                        print('*Overall Economy:\t',llll[k][4])
                                                                    r('drop table Bowlinginfo')
                                                                    while True:
                                                                        try:
                                                                            afg=int(input('Press \n1)Create stats for player,\n2)Back to home,\n3)To view another player stats,\n4)Exit'))
                                                                            if afg==1:
                                                                                cre()
                                                                                break
                                                                            elif afg==2:
                                                                                prg()
                                                                                break
                                                                            elif afg==4:
                                                                                break
                                                                            elif afg==3:
                                                                                vie()
                                                                                break
                                                                            else:
                                                                                print('Enter only 1 or 2 or 3 or 4')
                                                                                continue
                                                                        except:
                                                                            print('Enter only 1 or 2 or 3 or 4')
                                                                            continue
                                                                    c()
                                                                elif mut==5:
                                                                    kgf=n+'bowl'
                                                                    while True:
                                                                        try:
                                                                            r('select * from {}'.format(kgf))
                                                                            lop=cursor.fetchall()
                                                                            for j in lop:
                                                                                print('Match',j[0])
                                                                                print('*Date of match:',j[1])
                                                                                print('*Total number of wickets:',j[2])
                                                                                print('*Number of overs bowled:',j[3])
                                                                                print('*Number of runs given by bowler:',j[4])
                                                                            while True:
                                                                                    try:
                                                                                        afg=int(input('Press \n1)Create stats for player,\n2)Back to home,\n3)To view another player stats,\n4)Exit'))
                                                                                        if afg==1:
                                                                                            cre()
                                                                                            break
                                                                                        elif afg==2:
                                                                                            prg()
                                                                                            break
                                                                                        elif afg==4:
                                                                                            break
                                                                                        elif afg==3:
                                                                                            vie()
                                                                                            break
                                                                                        else:
                                                                                            print('Enter only 1 or 2 or 3 or 4')
                                                                                            continue
                                                                                    except:
                                                                                        print('Enter only 1 or 2 or 3 or 4')
                                                                                        continue
                                                                            break
                                                                        except:
                                                                            print('No bowling statistics is existing')
                                                                            while True:
                                                                                try:
                                                                                    afg=int(input('Press \n1)Create stats for player,\n2)Back to home,\n3)To view another player stats,\n4)Exit'))
                                                                                    if afg==1:
                                                                                        cre()
                                                                                        break
                                                                                    elif afg==2:
                                                                                        prg()
                                                                                        break
                                                                                    elif afg==4:
                                                                                        break
                                                                                    elif afg==3:
                                                                                        vie()
                                                                                        break
                                                                                    else:
                                                                                        print('Enter only 1 or 2 or 3 or 4')
                                                                                        continue
                                                                                except:
                                                                                    print('Enter only 1 or 2 or 3 or 4')
                                                                                    continue
                                                                            break
                                                                elif mut==1:
                                                                            noof30s=0
                                                                            noof50s=0
                                                                            noof100s=0
                                                                            n=n+'bat'
                                                                            while True:
                                                                                try:
                                                                                    r('select * from {}'.format(n))
                                                                                    l=cursor.fetchall()
                                                                                    break
                                                                                except:
                                                                                    while True:
                                                                                        print('\nNo batting statistics is existing\n')
                                                                                        print('Try again')
                                                                                        break
                                                                                break
                                                                            stri=0
                                                                            while True:
                                                                                try:
                                                                                        for b in range(0,len(l)):
                                                                                            cvv=l[b][-3]
                                                                                            stri=stri+float(cvv)
                                                                                        strikerate=stri/len(l)
                                                                                        ru=0
                                                                                        for b in range(len(l)):
                                                                                            tt=l[b][2]
                                                                                            ru=ru+int(tt)
                                                                                        totruns=ru
                                                                                        cc=[0]
                                                                                        for b in range(len(l)):
                                                                                            bb=l[b][2]
                                                                                            if int(bb)>cc[-1]:
                                                                                                cc=[int(bb)]
                                                                                        highestruns=cc[-1]
                                                                                        r('select OpponentTeamname from {} where runs={}'.format(n,highestruns))
                                                                                        v=cursor.fetchall()
                                                                                        bb=v[0][0]
                                                                                        highrunsagainst=bb
                                                                                        for b in range(len(l)):
                                                                                            if float(l[b][2])>=30 and float(l[b][2])<50:
                                                                                                noof30s+=1
                                                                                            elif float(l[b][2])>=50 and float(l[b][2])<100:
                                                                                                noof50s+=1
                                                                                            elif float(l[b][2])>=100:
                                                                                                noof100s+=1
                                                                                        noofmatchesbat=len(l)
                                                                                        count=0
                                                                                        for j in range(len(l)):
                                                                                            bb=l[b][4]
                                                                                            if bb=='out':
                                                                                                count+=1
                                                                                        if count!=0:
                                                                                            average=totruns/count
                                                                                        else:
                                                                                            average=totruns
                                                                                        while True:
                                                                                            try:
                                                                                                bat='create table Battinginfo(noofmatchesbat int,Average float,Highestscore int,Highestscoreagainstteam varchar(30),noof50s int,noof100s int,totnoof30s int,strikerate float,totalruns int)'
                                                                                                r(bat)
                                                                                                break
                                                                                            except:
                                                                                                r('drop table Battinginfo')
                                                                                                bat='create table Battinginfo(noofmatchesbat int,Average float,Highestscore int,Highestscoreagainstteam varchar(30),noof50s int,noof100s int,totnoof30s int,strikerate float,totalruns int)'
                                                                                                r(bat)
                                                                                                c()
                                                                                                break
                                                                                        r('insert into Battinginfo values({},{},{},"{}",{},{},{},{},{})'.format(noofmatchesbat,average, highestruns,highrunsagainst,noof50s,noof100s,noof30s,strikerate,totruns))
                                                                                        c()
                                                                                        ank='select * from Battinginfo'
                                                                                        r(ank)
                                                                                        llll=cursor.fetchall()
                                                                                        for k in range(len(llll)):
                                                                                            print('*No of matches bat:\t',llll[k][0])
                                                                                            print('*Average:\t',llll[k][1])
                                                                                            print('*Highest runs:\t',llll[k][2])
                                                                                            print('*Highest runs against:\t',llll[k][3])
                                                                                            print('*No of 50s:\t',llll[k][4])
                                                                                            print('*No of 100s:\t',llll[k][5])
                                                                                            print('*No of 30s:\t',llll[k][6])
                                                                                            print('*Strikerate:\t',llll[k][7])
                                                                                            print('*Total runs:\t',llll[k][8])
                                                                                        sr='drop table Battinginfo'
                                                                                        r(sr)
                                                                                        c()
                                                                                        while True:
                                                                                            prg()
                                                                                            break
                                                                                        break
                                                                                except:
                                                                                    prg()
                                                                                    break
                                                                if mut not in [1,2,3,4,5,6]:
                                                                        print('Enter only 1 to 6')
                                                                        vie()
                                                else:
                                                    print("No such player's batting info or bowling info is available")
                                                    while True:
                                                        try:
                                                            afg=int(input('Press\n1)Create stats for player,\n2)Back to home,\n3)To view another player stats,\n4)Exit'))
                                                            if afg==1:
                                                                cre()
                                                                break
                                                            elif afg==2:
                                                                prg()
                                                                break
                                                            elif afg==4:
                                                                break
                                                            elif afg==3:
                                                                vie()
                                                                break
                                                            else:
                                                                print('Enter only 1 or 2 or 3 or 4')
                                                                continue
                                                        except:
                                                            print('Enter only 1 or 2 or 3 or 4')
                                                            continue
                            if ss==2:
                                cre()
                            if ss==1:
                                vie()
                            break
    prg()
db()
