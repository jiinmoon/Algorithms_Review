# 722 Remove Comments

class Solution:
    def removeComments(self, source):
        res = list()
        temp = list()
        isComment = False

        for line in source:
            i = 0
            while i < len(line):
                curr = line[i:i+2]
                if not isComment and curr == '/*':
                    isComment = True
                    i += 2
                elif not isComment and curr == '//':
                    i = len(line)
                elif isComment and curr == '*/':
                    isComment = False
                    i += 2
                elif isComment:
                    i += 1
                else:
                    temp.append(line[i])
                    i += 1
            if not is comment and temp:
                res.append("".join(temp))
                temp = list()

        if temp:
            res.append("".join(temp))

        return res
