#Simran is running up a staircase with N steps, and can hop(jump) either 1 step, 3 steps or 5 steps at a time.
#You have to count, how many possible ways Simran can run up to the stairs.

#Input Format:
#Input contains integer N that is number of steps

#Output Format:
#Output for each integer N the no of possible ways w.

#Constraints
#0<n<30


steps=int(input())
def numways(steps):
	if steps==0 or steps==1:
		return 1
	total=0
	for i in [1,3,5]:
		if steps-i>=0:
			total=total+numways(steps-i)
	return total	

print(numways(steps))

