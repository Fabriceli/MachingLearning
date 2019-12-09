# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-12-07 15:39
# @Author   : Fabrice LI
# @File     : 20191207_7_serialize_and_deserialize_binary_tree.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Design an algorithm and write code to serialize and deserialize a binary tree.
#               Writing the tree to a file is called 'serialization' and reading back from the
#               file to reconstruct the exact same binary tree is 'deserialization'.
#Reference:**********************************************
"""
There is no limit of how you deserialize or serialize a binary tree,
LintCode will take your output of serialize as the input of deserialize,
it won't check the result of serialize.

Input：{3,9,20,#,#,15,7}
Output：{3,9,20,#,#,15,7}
Explanation：
Binary tree {3,9,20,#,#,15,7},  denote the following structure:
	  3
	 / \
	9  20
	  /  \
	 15   7
it will be serialized {3,9,20,#,#,15,7}

Input：{1,2,3}
Output：{1,2,3}
Explanation：
Binary tree {1,2,3},  denote the following structure:
   1
  / \
 2   3
it will be serialized {1,2,3}

Our data serialization use BFS traversal. This is just for when you got Wrong Answer and want to debug the input.

You can use other method to do serializaiton and deserialization.
"""


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        if not root:
            return []
        # 使用队列，把第一层结点放进队列
        queue = [root]
        index = 0
        # 注意每次遍历都会改变队列的长度，所以len(queue)是动态变化的，所以while才能遍历完整一个树
        # 直到把所有结点都放进队列
        while index < len(queue):
            if queue[index]:
                queue.append(queue[index].left)
                queue.append(queue[index].right)
            index += 1
        # 对于队列中最后的结点，是none的化就直接pop弹出队列
        while queue[-1] is None:
            queue.pop()
        # 对于结果队列，进行遍历，把所有结点值与None都序列化成要求字符串{1,2,3,#,4,6}
        result = '{%s}' % ','.join(str(node.val) if node else '#' for node in queue)
        return result


    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        # 如果输入是空的字符串或者括号里面是空的则直接返回一个None
        if data is '{}':
            return None
        # 对于data字符串{}里面的字符串进行分割转换成list
        vals = data[1:-1].split(',')
        root = TreeNode(int(vals[0]))
        queue = [root]
        is_left_node = True
        index = 0
        for val in vals[1:]:
            if val is not '#':
                node = TreeNode(int(val))
                if is_left_node:
                    queue[index].left = node
                else:
                    queue[index].right = node
                queue.append(node)
            if not is_left_node:
                index += 1
            is_left_node = not is_left_node
        return root


if __name__ == '__main__':
    s = Solution()
    data = '{3,9,20,#,#,15,7}'
    s.deserialize(data)
