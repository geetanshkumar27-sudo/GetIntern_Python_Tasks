print("=== EASY MARKSHEET ===")

s1 = int(input("Sub1: "))
s2 = int(input("Sub2: "))
s3 = int(input("Sub3: "))
s4 = int(input("Sub4: "))
s5 = int(input("Sub5: "))

total = s1 + s2 + s3 + s4 + s5
perc = total / 5
status = "PASS" if perc >= 33 else "FAIL"

print("MARKSHEET")
print("Sub1:", s1)
print("Sub2:", s2)
print("Sub3:", s3)
print("Sub4:", s4)
print("Sub5:", s5)
print("Total:", total, "/500")
print("Perc:", perc, "%")
print("Status:", status)

