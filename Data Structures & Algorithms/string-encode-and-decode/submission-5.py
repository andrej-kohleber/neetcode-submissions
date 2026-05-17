class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for s in strs:
            encode += str(len(s)) + "#" + s
        return encode


    def decode(self, s: str) -> List[str]:
        decode = []

        print(s)

        i = 0
        str_length = ""
        while i < len(s):
            if s[i] == '#':
                length = int(str_length)
                decoded_str = ""
                i += 1
                while length:
                    decoded_str += s[i]
                    length -= 1
                    i += 1
                decode.append(decoded_str)
                str_length = ""
                print(decoded_str)
            else:
                str_length += s[i]
                i += 1

        return decode
