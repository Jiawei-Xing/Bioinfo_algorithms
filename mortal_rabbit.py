Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> r=[]
>>> for i in range(0, 16):
	r.append(0)

>>> r[0]=1
>>> print(r)
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> for n in range(2, 82):
	a=sum(r)-r[0]
	r = r[:-1]
	r.insert(0, a)

>>> print(r)
[14279021112426106, 8826714694539927, 5456318867054989, 3372876161659149, 2084975947901086, 1288848002408615, 796713830193059, 492496342497067, 304441366750485, 188193368744571, 116333546973126, 71912704691083, 44453532369142, 27479380014744, 16986643934710, 10500457870949]
>>> sum(r)
37378265960028808
>>> 