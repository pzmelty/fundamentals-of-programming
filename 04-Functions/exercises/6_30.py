def sum_natural(n):
    j=0
    for i in range(1,n):
        j = j + i
    return j

def main():
    n = 4
    print(f'Sum of natural number between <1,{n}> is {sum_natural(n)}')

if __name__ == "__main__":
    main()