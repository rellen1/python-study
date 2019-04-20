import turtle as t

n, lin = map(int, input().split())

t.shape('turtle')
t.speed('fastest')

for i in range(n):
	t.fd(lin)
	t.rt(360 / n * 2)
	t.fd(lin)
	t.lt(360 / n)

t.mainloop()