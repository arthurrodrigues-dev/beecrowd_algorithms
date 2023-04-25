n = int(input())
v_in = v_out = 0

for i in range(n):
  x = int(input())
  if x >= 10 and x <= 20:
    v_in += 1
  else:
    v_out += 1

print(v_in, "in")
print(v_out, "out")
