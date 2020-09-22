# 428 Serialize and Deserialize N-ary Tree
#
# Traverse and append all nodes seen - but denote the end of children with
# special character.

class Codec:
    def serialize(self, root):
        def helper(node):
            if not node:
                return
            res.append(str(node.val))
            for child in node.children:
                helper(child)
            res.append("#")

        res = list()
        helper(root)

        return ",".join(res)
    
    def deserialize(self, data):
        def helper(node):
            if not data:
                return
            while data and data[-1] != "#":
                newNode = Node(int(data.pop()), list())
                node.children.append(newNode)
                helper(newNode)
            data.pop()

        data = data.split(",")[::-1]
        root = Node(int(data.pop()), list())
        helper(root)

        return root
