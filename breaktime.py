import webbrowser
import time
import random as rd

current_time = time.strftime('%H:%M')

a='https://www.youtube.com/watch?v=eW2qlKa6oHw'
b='https://www.youtube.com/watch?v=uyrAhLIbDHM'
c='https://www.youtube.com/watch?v=aRYokc3VBC4'
d='https://www.youtube.com/watch?v=AYmlVPp_4TI'
e='https://www.youtube.com/watch?v=mqiH0ZSkM9I'
f='https://www.youtube.com/watch?v=nc9rYioj2QM'
g='https://www.youtube.com/watch?v=mGgMZpGYiy8'
h='https://www.youtube.com/watch?v=TiCxqhu9cio'
j='https://www.youtube.com/watch?v=N8i5NLyXZdc'
k='https://www.youtube.com/watch?v=trig1MiEo1s'
l='https://www.youtube.com/watch?v=xEx147n9G1A'
m='https://www.youtube.com/watch?v=VVRaaCObo0M'
n='https://www.youtube.com/watch?v=eFjjO_lhf9c'
o='https://www.youtube.com/watch?v=hCuMWrfXG4E'
p='https://www.youtube.com/watch?v=mdlyEC2wcQQ'
q='https://www.youtube.com/watch?v=QUQsqBqxoR4'
r='https://www.youtube.com/watch?v=oozQ4yV__Vw'
s='https://www.youtube.com/watch?v=OPf0YbXqDm0'
t='https://www.youtube.com/watch?v=x-5OX7CO26c'

playlist=[a,b,c,d,e,f,g,h,j,l,m,n,o,p,q,r,s,t]

#musics=[0,1,2,3,4,5,6,7,8,9]

#while (current_time > '08:00'  and current_time < '12:00'):
for i in range(0,6):
    item = rd.choice(playlist)
    webbrowser.open(item)
    time.sleep(3600)

print('Out of time to break a time :)')
