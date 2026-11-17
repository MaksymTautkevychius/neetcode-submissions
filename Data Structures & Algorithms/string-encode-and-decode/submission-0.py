class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = s.index("#", i)          # find end of length prefix
            length = int(s[i:j])
            i = j + 1                    # skip '#'
            res.append(s[i:i + length])  # take exactly `length` chars
            i += length                  # move to next block
        return res
