class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # Step 1: Build graph
        graph = defaultdict(dict)
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val

        # Step 2: DFS helper
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited.add(start)
            for nei, val in graph[start].items():
                if nei in visited:
                    continue
                res = dfs(nei, end, visited)
                if res != -1.0:
                    return res * val
            return -1.0

        # Step 3: Process each query
        results = []
        for a, b in queries:
            results.append(dfs(a, b, set()))
        return results
