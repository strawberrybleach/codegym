class BinaryCode:
    def decode(self, message):
        ans0 = self.attempt(message, 0)
        ans1 = self.attempt(message, 1)
        return (ans0, ans1)

    def attempt(self, message, assumption):
        size = len(message)
        origin = [0] * size
        origin[0] = assumption
        for i in range(1, size):
            if i == 1:
                pi2 = 0
            else:
                pi2 = origin[i - 2]
            origin[i] = int(message[i - 1]) - origin[i - 1] - pi2
            if origin[i] != 0 and origin[i] != 1:
                return 'NONE'
        return ''.join(map(str, origin))
