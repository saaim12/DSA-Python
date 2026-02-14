from collections import deque


def level_order_traversal(root):
    q=deque
    q.append(root)
    arr=[]
    while q:
        level=[]
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.rigth)

        arr.append(level)

    return arr
