class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = [[]]
        if numRows == 0:
            ret = []
        elif numRows == 1:
            ret = [[1]]
        else:
            ret = [[1], [1, 1]]
        if numRows > 2:
            for i in range(1, numRows - 1):
                tmp = [1]
                for j, _ in enumerate(ret[i]):
                    if j + 1 < len(ret[i]):
                        tmp.append(ret[i][j] + ret[i][j + 1])
                else:
                    tmp.append(1)
                ret.append(tmp)
        return ret
