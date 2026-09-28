class Solution:

    def encode(self, strs: List[str]) -> str:
        # + 사용시 str()과 같이 타입 맞춰줘야함. fstring이 보다 편리.
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            # i번째 위치부터 #을 찾음.
            j = s.find('#', i)
            length = int(s[i:j])
            # length만큼 append하고 넘어가기 때문에 내부에 32#와 같은 값 있어도 상관없음.
            res.append(s[j+1:j+length+1])
            i = j + length + 1

        return res