a = input();
s = input();
l = 0
r = 0
for i, ch in enumerate(s):
	if ch=='>':
		break
	l+=1
for i, ch in enumerate(s):
	if s[-i-1]=='<':
		break;
	r+=1
print(l+r)
