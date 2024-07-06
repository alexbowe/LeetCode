class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []
        toks = [x for x in path.split("/") if x]
        for x in toks:
            if x == ".": continue
            if x == "..": s = s[:-1]
            else: s.append(x)
        return "/" + "/".join(s)