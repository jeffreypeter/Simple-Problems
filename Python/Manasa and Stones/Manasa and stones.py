# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools as it
for count in range(int(raw_input())):
    (n,a,b) = (raw_input(),int(raw_input()),int(raw_input()))
    comb = list(it.combinations_with_replacement((a,b),int(n)))
    dist =  sorted(set([(sum(x)) for x in comb]))
    print " ".join(map(str, dist))