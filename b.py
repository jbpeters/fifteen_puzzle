grid = 4
num = [ [0 for _ in range(grid)]  for _ in range(grid)]
def main():
    for row in range(grid):
        for col in  range(grid):
            num[row][col]=( row*grid + col+1)
    print(num)
if __name__ =="__main__":
    main()
