def solve_query(q):
    automaton = build_kmp(q)

    def dfs(u):
        # dp[state][flip_used] = (paths, flips)
        dp = init_dp()

        for v in children[u]:
            child_dp = dfs(v)
            dp = merge(dp, child_dp, u, v)

        # process leaf
        if is_leaf(u):
            for state in dp:
                if state == len(q):
                    dp[state] = (1, dp[state][1])

        return dp

    result = dfs(0)
    best_paths, min_flips = best(result)
    return min_flips * M
