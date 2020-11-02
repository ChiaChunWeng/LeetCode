"""
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

    Best solution:
        class Solution(object):
        def isValid(self, s):
            # The stack to keep track of opening brackets.
            stack = []

            # Hash map for keeping track of mappings. This keeps the code very clean.
            # Also makes adding more types of parenthesis easier
            mapping = {")": "(", "}": "{", "]": "["}

            # For every bracket in the expression.
            for char in s:

                # If the character is an closing bracket
                if char in mapping:

                    # Pop the topmost element from the stack, if it is non empty
                    # Otherwise assign a dummy value of '#' to the top_element variable
                    top_element = stack.pop() if stack else '#'

                    # The mapping for the opening bracket in our hash and the top
                    # element of the stack don't match, return False
                    if mapping[char] != top_element:
                        return False
                else:
                    # We have an opening bracket, simply push it onto the stack.
                    stack.append(char)

            # In the end, if the stack is empty, then we have a valid expression.
            # The stack won't be empty for cases like ((()
            return not stack

    https://leetcode.com/problems/valid-parentheses
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack =[]
        for element in s:
            if element == "(" or element == "[" or element== "{":
                print(element)
                stack.append(element)
            else:
                if not stack:
                    print(s, "Contains invalid parentheses.")
                    return False
                else:
                    bottom = stack[-1]
                    if element ==")" and bottom == "(" or element == "]" and bottom == "[" or element == "}" and bottom=="{":
                        stack.pop()
                    else:
                        print(s, ">Contains invalid parentheses.")
                        return False
        if not stack:
            print(s, ">Contains valid parentheses.")
            return True
        else:
            print(s, ">Contains invalid parentheses.")
            return False




if __name__ == '__main__':

    input = "(])"
    A=Solution().isValid(input)