str1 ="str1\nstr2\nstr3\nstr4\nstr5\nstr6\nstr7\nstr8\nstr9\nstr10\nstr11\nstr12\nstr13\nstr14\nstr15\nstr16\nstr17\nstr18\nstr19\nstr20\nstr21\nstr22\nstr23\nstr24\nstr25"
n = 3
def print_n_lines(str1, n):
    res_lst = str1.split("\n")
    len_str = len(res_lst)
    result = res_lst[len(res_lst)-n:len_str]
    print("RESULT - ",result )
    print("\n".join(result))

print_n_lines(str1, n)