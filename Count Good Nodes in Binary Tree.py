# Time complexity: O(N) as we visit every node only once.
# Space complexity: O(H) where H is the height of the tree.
# In the worst case, H would be N given that the tree only has one path.
class Solution:
    # the idea is to record the max value from the root to the node
    # we can first initialise mx as -10000 
    def goodNodes(self, root: TreeNode, mx = -10000) -> int:
        # if the root is null, we return 0
        if root is None: return 0
        return (
            # then we can break it into 3 parts
            # the first part is the current node
            # if the current node value is greater than the maximum value so far
            # that means the current node is a good node
            # hence we add 1, else add 0
            (1 if mx <= root.val else 0) + 
            # the second part is the result of the left sub-tree
            # we traverse it with the updated maximum value at the current point
            # we don't need to check if root.left is null or not here
            # as we cover the null case in the first line
            self.goodNodes(root.left, max(root.val, mx)) +
            # the last part is the result of the right sub-tree
            # we traverse it with the updated maximum value at the current point
            # we don't need to check if root.right is null or not here
            # as we cover the null case in the first line
            self.goodNodes(root.right, max(root.val, mx))
        )
