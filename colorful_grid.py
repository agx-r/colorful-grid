class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]

    def create_symbol(self, char, x, y, r, g, b):
        # Check if the coordinates are within the grid
        if 0 <= x < self.width and 0 <= y < self.height:
            # Format RGB values into a color representation
            color = f'\033[38;2;{r};{g};{b}m{char}\033[0m'
            self.grid[y][x] = color
        else:
            print("Invalid coordinates. Coordinates out of grid range.")

    def delete_symbol(self, x, y):
        # Check if the coordinates are within the grid
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = ' '
        else:
            print("Invalid coordinates. Coordinates out of grid range.")

    def draw_grid(self):
        horizontal_line = '+---' * self.width + '+'
        for row in self.grid:
            print(horizontal_line)
            print('|', end='')
            for cell in row:
                print(f' {cell} |', end='')
            print()
        print(horizontal_line)


# Example usage:
if __name__ == "__main__":
    # Create a 5x5 grid
    my_grid = Grid(5, 5)

    # Set colored symbols at specific coordinates
    my_grid.create_symbol('R', 0, 0, 255, 0, 0)
    my_grid.create_symbol('G', 2, 2, 0, 255, 0)
    my_grid.create_symbol('B', 4, 4, 0, 0, 255)

    # Draw the grid
    my_grid.draw_grid()
