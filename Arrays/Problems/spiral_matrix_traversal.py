def spiral_matrix(mat):
    rows=len(mat)
    cols=len(mat[0])
    left=0
    right=cols-1
    top=0
    bottom=rows-1
    res=[]
    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            res.append(mat[top][i])
        top += 1
        for i in range(top, bottom + 1):
            res.append(mat[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                res.append(mat[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(mat[i][left])
            left += 1

    return res


print(spiral_matrix([[1,2,3],[4,5,6],[7,8,9]]))
print(spiral_matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))