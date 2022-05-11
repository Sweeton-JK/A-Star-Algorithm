#A* Search

graph={

        'Arad' : [('Zerind',75),('Timisoara',118),('Sibiu',140)],

        'Zerind' : [('Oradea',71)],

        'Timisoara' : [('Lugoj',111)],

        'Sibiu' : [('Ruminic Vilcea',80),('Fagaras',99)],

        'Oradea' : [('Sibiu',151)],

        'Lugoj' : [('Mehadia',70)],

        'Ruminic Vilcea' : [('Pitesti',97),('Craiova',146)],

        'Fagaras' : [('Bucharest',211)],

        'Mehadia' : [('Doberata',75)],

        'Pitesti' : [('Bucharest',101),('Craiova',146)],

        'Craiova' : [('Pitesti',138),('Ruminic Vilcea',146)],

        'Bucharest' : [('Urziceni',85),('Giurgiu',90)],

        'Urziceni' : [('Hirsova',98),('Vasuli',142)],

        'Hirsova' : [('Etorie',86)],

        'Vaslui' : [('Iasi',92)],

        'Iasi' : [('Neamt',87)],

        'Dobreta' : [('Craiova',120)]

        }


hk={
        'Arad' : 366,

        'Bucharest' : 0,

        'Craiova' : 160,

        'Dobreta' : 242,

        'Fagaras' : 178,

        'Lugoj' : 244,

        'Mehadia' : 241,

        'Pitesti' : 98,

        'Ruminic Vilcea' : 193,

        'Sibiu' : 253,

        'Timisoara' : 329,

        'Zerind' : 374,

        'Urziceni' : 80,

        'Giurgiu' : 77,

        'Hirsova' : 151,

        'Etorie' : 161,

        'Vaslui' : 199,

        'Iasi' : 226,

        'Neamt' : 234,

        'Oradea' : 380

        }


def a_star(s,e,total):

    cost=[]

    c=[]

    if s in graph:

        for val in graph[s]:

           total=val[1]+hk[val[0]]

           c.append(total)

           cost.append([total,val[0]])

        m = min(c)

        for i in cost:

            if(i[0]==m):

                if(i[1]==e):

                    print(i[1])

                    break

                else:

                    print(i[1],end="\n")

                    a_star(i[1],e,total-hk[val[0]])

s=input("Enter The Starting City\n")

e=input("Enter The Ending City\n")

total=0

print("\n-----Required Path-----\n")

print(s,end="\n")

a_star(s,e,total)

