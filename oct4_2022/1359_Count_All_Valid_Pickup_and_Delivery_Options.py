# Link: https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options


class Solution:
    def countOrders(self, n: int) -> int:
        """
        Time: O(n^2)
        Space: O(n^2)

        dp table:
        not_delivered -->
        not_picked up
        |
        |
        \/

        dp[not_picked][not_delivered] denotes the number of ways to deliver
        with not_picked orders and not_delivered orders.
        """
        mod = 10**9 + 7
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # Base case.
        dp[0][0] = 1

        for not_picked in range(n + 1):
            for not_delivered in range(not_picked, n + 1):
                new_permutations = 0
                if not_picked > 0:
                    # Choose order to pick up.
                    new_permutations += not_picked * dp[not_picked - 1][not_delivered]

                if not_delivered > not_picked:
                    # Choose order to deliver.
                    new_permutations += (not_delivered - not_picked) * dp[not_picked][
                        not_delivered - 1
                    ]

                # Add new permutations to dp table.
                dp[not_picked][not_delivered] += new_permutations
                dp[not_picked][not_delivered] %= mod

        return dp[n][n]
