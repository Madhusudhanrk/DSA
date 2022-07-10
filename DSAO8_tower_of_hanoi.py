# Recursive Python function to solve tower of hanoi

def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
	if n == 0:
		return
	TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
	print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
	TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
		
# Driver code
n = 4
TowerOfHanoi(n, 'A', 'C', 'B')
# A, C, B are the name of rods

# Contributed By Harshit Agrawal


Let rod 1 = 'A', rod 2 = 'B', rod 3 = 'C'.
An example with 2 disks :
Step 1 : Shift first disk from 'A' to 'B'.

Step 2 : Shift second disk from 'A' to 'C'.

Step 3 : Shift first disk from 'B' to 'C'.