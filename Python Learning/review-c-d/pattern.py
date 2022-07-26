"""The following number pattern should be printed using a loop.
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
"""

# Hint: pattern contains 5 rows
# declared variable for row # user can input any value
row = int(input())

# start: 1
# stop: row+1 (range never include stop number in result)
# step: 1

# run loop 5 times
for i in range(1, row+1, 1):

    # Run inner loop i+1 times
    for j in range(1, i+1):
        print(j, end=' ')
    # empty line after each row
    print("")