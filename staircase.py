steps=6
def numways(steps):
	if steps==0 or steps==1:
		return 1
	total=0
	for i in [1,3,5]:
		if steps-i>=0:
			total=total+numways(steps-i)
	return total	

print(numways(steps))

