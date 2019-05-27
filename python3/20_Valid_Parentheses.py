import pdb


class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c in "[{(":
                st.append(c)
            elif c == ")":
                if not st or st.pop() != "(":
                    return False
            elif c == "]":
                if not st or st.pop() != "[":
                    return False
            elif c == "}":
                if not st or st.pop() != "{":
                    return False
        if st:
            return False
        return True


if __name__ == "__main__":
    print(Solution().isValid(")"))