# Given a list lst and a number N, create a new list that contains each number of lst 
# at most N times without reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], 
# you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being i
# n the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].

def delete_nth(order,max_e):
    rv = list(reversed(order))
    print(rv)
    for i in order:
        count = rv.count(i)
        while rv.count(i) > max_e:
            rv.remove(i)
    return list(reversed(rv))

print(delete_nth([27, 27, 39, 39, 13, 13, 29, 13, 27, 3, 27, 27, 3, 29, 27, 39, 39, 3, 24, 13, 13, 27, 27, 13, 27, 27], 1))

def delete_nth_bp(order,max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans