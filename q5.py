test_cases = int(input("Enter number of test cases: \n"))
results = []
def string_div(string1, string2):
    string1_1 = string1[:len(string1)//2]
    string1_2 = string1[len(string1)//2:]

    string2_1 = string2[:len(string2) // 2]
    string2_2 = string2[len(string2) // 2:]

    if string1_1 == string2_1 and string1_2 == string2_2 or string1_1 == string2_2 and string1_2 == string2_1:
        results.append("YES \n")
    else:
        results.append("NO \n")


if 1 <= test_cases <= 10:
    for i in range(0, test_cases):
        s1 = input()
        s2 = input()
        string_div(s1, s2)

print(*results, sep="")
#end
