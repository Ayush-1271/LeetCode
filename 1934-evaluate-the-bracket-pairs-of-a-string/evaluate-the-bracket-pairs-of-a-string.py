class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        ob = False
        knowledge = dict(knowledge)
        res = []
        c_key = []

        for v in s:
            if v == '(':
                ob = True
            elif v == ')':
                ob = False
                key = ''.join(c_key)

                if key in knowledge:
                    res.append(knowledge[key])
                else:
                    res.append('?')
                c_key = []
            else:
                if ob:
                    c_key.append(v)
                else:
                    res.append(v)
        
        return "".join(res)