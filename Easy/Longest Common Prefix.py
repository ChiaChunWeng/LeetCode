"""
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".



    Reference:
        https://www.youtube.com/watch?v=g5kH8EX4l-U&feature=emb_logo&ab_channel=TerribleWhiteboard
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)== 0 or strs == None or len(strs)>200 or len(strs) < 0:
            return ""
        else:
            min_string = min(strs)
            max_string = max(strs)
            print(min_string, max_string)
            for i, c in enumerate(min_string):
                if c != max_string[i]:
                    return min_string[:i]
            return min_string
            # size = len(strs)
            # strs.sort(key=len)
            # end = min(len(strs[0]), len(strs[size - 1]))
            # i = 0
            # while (i < end and strs[0][i] == strs[size - 1][i]):
            #     i += 1
            # Result = strs[0][:i]
            # if Result == None or Result == "":
            #     print("There is no common prefix among the input strings.")
            #     return ""
            # else:
            #     print(Result)
            #     return Result






if __name__ == '__main__':
    #["dog","racecar","car"], ["flower", "flow", "flight"]
    input = ["dog","racecar","car"]
    A=Solution().longestCommonPrefix(input)
