class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        """
        BFS approach.
        Use bit mask to denote the nodes that the route traversed.

        Time: O(2^N * N * N)
        Space: O(2^N * N)

        N: The number of nodes present in the given graph.
        """
        if len(graph) == 1:
            return 0

        # The mask of a completed solution.
        completed_mask = (1 << len(graph)) - 1

        # Each node in the queue starts the route with the current node.
        queue = deque([(node, 1 << node) for node in range(len(graph))])
        seen = set(queue)
        res = 0

        while queue:
            queue_length = len(queue)
            for _ in range(queue_length):
                node, mask = queue.popleft()
                for neighbour in graph[node]:
                    # New "route" includes the neighbor node.
                    new_mask = mask | (1 << neighbour)
                    if new_mask == completed_mask:
                        return res + 1

                    new_state = (neighbour, new_mask)
                    if new_state not in seen:
                        seen.add(new_state)
                        queue.append(new_state)

            res += 1

        # Unreach code given the constraint.
        return -1
