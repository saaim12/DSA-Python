# flood_fill.py
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        Perform a flood fill on a 2D image starting at (sr, sc).
        DFS implementation.
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        original = image[sr][sc]
        if original == color:
            return image  # nothing to do

        rows, cols = len(image), len(image[0])
        visited = set()

        def dfs(i, j):
            # boundary and validity checks
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return
            if (i, j) in visited:
                return
            if image[i][j] != original:
                return

            visited.add((i, j))
            image[i][j] = color  # fill current cell

            # explore 4 directions
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        dfs(sr, sc)
        return image

# ---------------- Driver / Test ----------------
if __name__ == "__main__":
    sol = Solution()

    image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ]
    sr, sc = 1, 1
    color = 2

    new_image = sol.floodFill(image, sr, sc, color)

    print("Flood Filled Image:")
    for row in new_image:
        print(row)