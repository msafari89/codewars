def tribonacci(signature, n):
    if n < 4:
        return signature[:n]
    else:
        working_list = signature.copy()
        for i in range(n-3):
            working_list.append(sum(working_list[-3:]))
        return working_list

print(tribonacci([1, 1, 1], 6))

def tribonacci_bp(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res

#print(tribonacci_bp([1, 1, 1], 6))