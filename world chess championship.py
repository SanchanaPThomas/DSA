for _ in range(int(input())):
    x=int(input())
    res=input()
    carlsen_points=(2*(res.count('C')))+res.count("D")
    chef_points=(2*(res.count('N')))+res.count("D")
    if carlsen_points>chef_points:
        print(x*60)
    elif carlsen_points<chef_points:
        print(x*40)
    else:
        print(x*55)
