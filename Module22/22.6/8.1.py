str = open("text8.txt", "r").read().lower()
f = {}
n = 0
for c in str:
   if ord('a') <= ord(c) <= ord('z'):
       x = f.get(c, 0)
       f[c] = x + 1
       n += 1

lout = [(k, "{:5.3f}".format(f[k]/n)) for k in f.keys()]
lout.sort(key = lambda x: x[0])
lout.sort(key = lambda x: x[1], reverse = True)
print(lout)
sout = "\n".join([i[0] + " " + i[1] for i in lout])
print(sout)
open("analysis.txt","w").write(sout)