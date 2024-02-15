def magic_square(n):
    # Initialize an empty 2D list for the magic square
    magicSquare = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        magicSquare.append(l)

    # Start from the middle of the first row
    i = n // 2
    j = n // 2 + 1

    # Set the maximum number to be filled in the magic square
    num = n * n
    count = 1

    # Loop to fill the magic square
    while count <= num:
        # Handle special cases where i becomes -1 and j becomes n
        if (i == -1 and j == n):
            i = 0
            j = n - 2
        else:
            # Handle wrapping around the matrix
            if j == n:
                j = 0
            if i < 0:
                i = n - 1

        # Adjust starting position for even order magic square
        if n % 2 == 0 and count == 1:
            j = n // 2 - 1

        # Check if the current cell is already filled
        if magicSquare[i][j] != 0:
            # Adjust position if cell is filled
            j -= 2
            i += 1
            continue
        else:
            # Fill the current cell with the current count
            magicSquare[i][j] = count
            count = count + 1

        # Move to the next cell
        i -= 1
        j += 1

    # Print the generated magic square
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j], end=" ")
        print()

    # Print the sum of each row, column, or diagonal
    print("The sum of each row or column or diagonal is", int(n * (n**2 + 1) / 2))


# Example: Generate a magic square of order 7
magic_square(7)
