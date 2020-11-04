# Define a function generate_n_chars() that takes an integer n and a character c and returns a string, n
# characters long, consisting only of c:s. For example, generate_n_chars(5,"x") should return the
# string "xxxxx". (Python is unusual in that you can actually write an expression 5 * "x" that will evaluate
# to "xxxxx". For the sake of the exercise you should ignore that the problem can be solved in this manner.)

def generate_n_chars(n, c):
    output = ""
    for i in range(n):
        output = output + c
    return output


print(generate_n_chars(5, 'x'))


## python way

def gen_no_of_chars(num, chars):
    return num * chars


print(gen_no_of_chars(8, 'a'))



