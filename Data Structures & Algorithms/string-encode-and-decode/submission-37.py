import base64

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = []

        if not strs:
            return '0:'

        for s in strs:
            str_to_encode = s
            if not str_to_encode or str_to_encode == '':
                str_to_encode = ''

            encoded_str = base64.b64encode(str_to_encode.encode('utf-8')).decode('utf-8')

            encoded_strs.append(encoded_str)

        result = ','.join(encoded_strs) if encoded_strs else ''
        result = f"{len(strs)}:{result}"
        print(f"encoded string: '{result}'")
        return result


    def decode(self, s: str) -> List[str]:
        print(f"incoming encoded string={s}")

        count, encoded_str = s.split(':')

        if int(count) == 0:
            return []

        encoded_strs = encoded_str.split(',')
        print(f"encoded_strs: {encoded_strs}")
        decoded_strs = []

        for es in encoded_strs:
            ds = base64.b64decode(es.encode('utf-8')).decode('utf-8')
            print(f"decoded string: '{ds}'")
            decoded_strs.append(ds)

        return decoded_strs


