class Solution:
    def findOrder(self, words):
        # first finding max no of words and making graph
        chars=set()
        for word in words:
            for c in word:
                chars.add(c)

        n=len(chars)
        graph={i:[] for i in range(n)}
        chars_to_index = {c: i for i, c in enumerate(chars)}
        index_to_char = {i: c for c, i in chars_to_index.items()}
        #making a dag
        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]
            min_len=min(len(w1),len(w2))
            # Prefix invalid case
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j]!=w2[j]:
                    u=chars_to_index[w1[j]]
                    v=chars_to_index[w2[j]]
                    graph[u].append(v)
                    break

        ## now doing topo_Sort

        visited=set()
        path=set()
        order=[]
        def dfs(node):
            visited.add(node)
            path.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    if dfs(nei):
                        return True #cycle deceted no true ordering
                elif nei in path:
                    return True  #cycle deceted no true ordering

            path.remove(node)
            order.append(node)
            return False

        for i in range(len(graph)):
            if i not in visited:
                if dfs(i):
                    return "__"

        order.reverse()
        return "".join(index_to_char[i] for i in order)










words1=["baa", "abcd", "abca", "cab", "cad"]
words2= ["caa", "aaa", "aab"]
words3=["ab", "cd", "ef", "ad"]

Sol=Solution()
print(Sol.findOrder(words1))
print(Sol.findOrder(words2))
print(Sol.findOrder(words3))

