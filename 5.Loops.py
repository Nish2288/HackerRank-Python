'''Task
Read an integer . For all non-negative integers , print

. See the sample for details.

Input Format

The first and only line contains the integer,

.

Constraints

Output Format

Print
lines, one corresponding to each . '''

if __name__ == '__main__':
    n = int(input())

    if(n>1 and n<=20):
        i=0
        while(i<n):
            print(i*i)
            i=i+1