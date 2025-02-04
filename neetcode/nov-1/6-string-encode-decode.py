class Solution:

    def encode(self, strs: list[str]) -> str:
        """
        this does not work if the seperator is used in the text
        hence we do need the length to be encoded here.
        """
        encoded = ""
        for word in strs:
            encoded = encoded + word + "#"
            print(f"{encoded=}")
        return encoded

    def decode(self, s: str) -> list[str]:
        decoded = []
        word = ""
        for char in s:
            if char != "#":
                word = word + char
            else:
                decoded.append(word)
                word = ""
                print(f"{word=}, {decoded=}")
        return decoded


if __name__ == "__main__":
    input1 = ["neet", "code", "love", "you"]
    input2 = ["we", "say", ":", "yes"]
    input3 = ["we", "say", ":", "yes", "!@#$%^&*()"]
    output = Solution().encode(input2)
    assert Solution().decode(output) == input2
