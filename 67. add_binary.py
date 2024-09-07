# Given two binary strings a and b, return their sum as a binary string.
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
def addBinary(a: str, b: str) -> str:
    a = int(a, 2)
    b = int(b, 2)

    while b:
        without_carry = a ^ b
        carry = (a & b) << 1
        a = without_carry
        b = carry

    return bin(a)[2:]


print(addBinary("11", "1"))
print(addBinary("1010", "1011"))
