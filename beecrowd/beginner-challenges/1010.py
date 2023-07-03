cod1, num_pecas1, v_unitario1 = input().split()
cod1, num_pecas1, v_unitario1 = int(cod1), int(num_pecas1), float(v_unitario1)

cod2, num_pecas2, v_unitario2 = input().split()
cod2, num_pecas2, v_unitario2 = int(cod2), int(num_pecas2), float(v_unitario2)

total = (num_pecas1 * v_unitario1) + (num_pecas2 * v_unitario2)

print("VALOR A PAGAR: R$ {:.2f}".format(total))
