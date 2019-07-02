#Given an array, find the int that appears an odd number of times.

#There will always be only one integer that appears an odd number of times.

# Used nested loops to compare arrays number to each other. since there will be one integer, we just need to 
# find one


def find_it(seq):
    size = int(len(seq))

#loop all numbers in the list
    for i in range(0 , size):
        count = 0

 #loop all the list numbers for comparison       
        for j in range(0, size):
            #print('i= ', i)
            #print('j= ', j)
 #find total number of the times i number is repeated           
            if seq[i] == seq[j]:
                count += 1


 #return if that number is odd       
        if (count % 2 != 0 ):
            result = seq[i]
            print(result)
            return seq[i]


    return None

seq = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
find_it(seq)


################################## BEST PRACTICE 1 ################################
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

