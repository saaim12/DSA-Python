list=[1,2,3,4]
list.append(5)
print(list)
list.pop()
print(list)

import time


def spiral_animation(matrix):
    if not matrix: return []

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    result = []

    step = 1

    while top <= bottom and left <= right:
        # 1. Traverse Right
        print(f"\n--- STEP {step}: Move RIGHT ---")
        print(f"Pointers -> Top:{top} Bottom:{bottom} Left:{left} Right:{right}")
        for col in range(left, right + 1):
            result.append(matrix[top][col])
            print(f"Added: {matrix[top][col]} | Current List: {result}")
            time.sleep(2)
        top += 1
        step += 1

        # 2. Traverse Down
        if top <= bottom and left <= right:  # Check needed if top moved past bottom
            print(f"\n--- STEP {step}: Move DOWN ---")
            print(f"Pointers -> Top:{top} Bottom:{bottom} Left:{left} Right:{right}")
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
                print(f"Added: {matrix[row][right]} | Current List: {result}")
                time.sleep(2)
            right -= 1
            step += 1

        # 3. Traverse Left
        if top <= bottom:
            print(f"\n--- STEP {step}: Move LEFT ---")
            print(f"Pointers -> Top:{top} Bottom:{bottom} Left:{left} Right:{right}")
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
                print(f"Added: {matrix[bottom][col]} | Current List: {result}")
                time.sleep(2)
            bottom -= 1
            step += 1

        # 4. Traverse Up
        if left <= right:
            print(f"\n--- STEP {step}: Move UP ---")
            print(f"Pointers -> Top:{top} Bottom:{bottom} Left:{left} Right:{right}")
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
                print(f"Added: {matrix[row][left]} | Current List: {result}")
                time.sleep(2)
            left += 1
            step += 1

    print("\nDONE! Final Result:", result)


# Run it
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
spiral_animation(matrix)