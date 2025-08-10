from colorama import init, Fore, Back, Style

# Initialize Colorama with auto-reset so colors don't leak into next prints
init(autoreset=True)

def count_and_display_islands(grid):
    n = len(grid)
    if n == 0:
        print("Grid is empty.")
        return 0
    m = len(grid[0])
    visited = [[False] * m for _ in range(n)]

    def dfs(i, j):
        if i < 0 or i >= n or j < 0 or j >= m:
            return
        if grid[i][j] != 'L' or visited[i][j]:
            return
        visited[i][j] = True
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx != 0 or dy != 0:
                    dfs(i + dx, j + dy)

    island_count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'L' and not visited[i][j]:
                island_count += 1
                dfs(i, j)

    # Print the beautifully colored grid
    print("\nHere’s your grid (Green = Land, Blue = Water):\n")
    for row in grid:
        for cell in row:
            if cell == 'L':
                print(Fore.GREEN + 'L', end=' ')
            else:
                print(Fore.BLUE + 'W', end=' ')
        print()
    print(Style.RESET_ALL)
    return island_count

if __name__ == "__main__":
    sample_grid = [
        ['L', 'W', 'L', 'W'],
        ['L', 'L', 'W', 'W'],
        ['W', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L']
    ]
    num = count_and_display_islands(sample_grid)
    print(f"\nTotal Islands Found: {Fore.YELLOW}{num}{Style.RESET_ALL}")
