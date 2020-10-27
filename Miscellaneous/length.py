n=10
log = (n==10)
#z=9 if log else None
cl = [{1, 2, 3}, {0,2,3}]
mx = 4
# strc = {z: {x for x in range(z+1, n+1) if z**2+x**2 == int((z**2+x**2)**0.5)**2} for z in range(1, n+1)}
# [strc[d].add(x) for x in range(1,n+1) for d in strc[x]]
# print(strc)
game = [x for x in range(64)]
xlate = [x*8+z for z in range(8) for x in range(7,-1,-1)]
newGame = [game[x] for x in xlate]
print(xlate)
print(newGame)
mx = 2 if log else 3 if log else 4 
#lis = {z: {z+1 if (z+1)%n!=0, z-1 if (z)%n!=0, z-8 if (z)//n!=0, z+8 if (z)//n!=n-1} for z in range(n**2)}
#lis = set().union({z+1 if (z+1)%n!=0}, {z-1 if (z)%n!=0}, {z-8 if (z)//n!=0}, {z+8 if (z)//n!=n-1})
#lis = [{d for z in cl for d in z  if k in z} for k in range(mx)]
print(mx)
# tl = {n,1} # z//n
# tr = {n,-1}
# br = {0-n,-1}
# bl = {0-n,1}
# t = {n, 1, -1}
# l = {n, 1, 0-n}
# r = {n, -1, 0-n}
# t = {n, 1, -1}
# b = {0-n, 1, -1}
# {z: {z+d for d in {n,1} if } for z in range(n**2)}
# for x in {1,2,3,4} if mx == 4 else {1,2,3}:
#     print(x)