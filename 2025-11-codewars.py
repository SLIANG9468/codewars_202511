""" # 7 Kyu Python Fundamentals Approved Questions

https://www.codewars.com/kata/557592fcdfc2220bed000042

#Complete The Pattern #7 - Cyclical Permutation
You have to write a function which creates the following pattern (See Examples) upto desired number of rows.

If the Argument is 0 or a Negative Integer then it should return "" i.e. empty string.

Examples:
Argument: 9

123456789
234567891
345678912
456789123
567891234
678912345
789123456
891234567
912345678
"""

def pattern(n: int) -> str:
    if n <= 0:
        return ""

    rows = []
    for start in range(1, n + 1):
        row = ""
        for k in range(n):
            num = (start + k - 1) % n + 1
            row += str(num)
        rows.append(row)

    return "\n".join(rows)


def pattern(n):
    return '\n'.join(''.join(str((x+y)%n+1) for y in range(n)) for x in range(n))