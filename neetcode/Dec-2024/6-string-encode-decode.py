from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded: str = ""

        for s in strs:
            length = len(s)
            # encoded = str(length)+s
            encoded = encoded + "".join(str(length) + s)
        print(f"{encoded=}")
        return encoded

    def decode(self, s: str) -> List[str]:
        """
        - my code fails when string is multi digit length
        - eg ["we","say",":","yes","!@#$%^&*()"]
        """
        decoded: list = []
        left, right = 0, len(s) - 1
        while left <= right:
            temp: str = ""
            if isinstance(int(s[left]), int):
                step: int = int(s[left])
                print(f"current pointer increment {step=}")
                print(f"slice from {left+1}:{step+1}")
                end = left + step + 1
                temp = s[left + 1 : end]
                print(f"{temp=}")
            left += step + 1
            print(f"updated pointer {left=}")
            decoded.append(temp)
        print(f"{decoded=}")
        return decoded

    def encode2(self, strs: List[str]) -> str:
        """
        NC sol using separator logic
        """
        encoded: str = ""

        for s in strs:
            # encoded = str(length)+s
            encoded += str(len(s)) + "#" + s
        print(f"{encoded=}")
        return encoded

    def decode2(self, s: str) -> List[str]:
        decoded = []
        left = 0

        while left < len(s):
            step = left
            while s[step] != "#":
                step += 1
            length = int(s[left:step])
            left = step + 1
            step = left + length
            word = s[left:step]
            print(f"Slice from {left}:{step} make the {word=}")
            decoded.append(word)
            left = step
        return decoded


if __name__ == "__main__":
    input = ["neet", "code", "love", "you"]
    input2 = ["we", "say", ":", "yes"]
    input3 = ["we", "say", ":", "yes", "!@#$%^&*()"]
    output = Solution().encode2(input3)
    assert Solution().decode2(output) == input3
