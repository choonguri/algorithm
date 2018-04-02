# https://www.hackerrank.com/challenges/drawing-book/problem

def solve(n, p):
    page_idx = (p+1)//2
    last_page_idx = (n+1)//2
    if page_idx-1 < last_page_idx-page_idx:
        return page_idx-1
    else :
        return last_page_idx-page_idx


if __name__ == '__main__':

    n = int(input())

    p = int(input())

    res = solve(n, p)

    print(res)