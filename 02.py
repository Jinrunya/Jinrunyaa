c=2
m_max=c
m_min=0
g=(m_min+m_max)/2
print(1)
while (abs(pow(g,2)-c)>0.00000001):
    print(1)
    if(pow(g,2)<c):
        m_min=g
    else:
        m_max=g
    g=(m_min+m_max)/2
print(g)