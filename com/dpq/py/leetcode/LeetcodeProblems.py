class LinkedListNode:
    def __init__(self, val):
        self.val = val

    def __init__(self, next1, val):
        self.val = val
        self.next = next1


class LeetcodeProblems:

    @staticmethod
    def findTwoNumbersIndexes(input, target):
        print("deepak is here to solve everything...")
        i = 0
        length = len(input)
        while i < length:
            j = i + 1
            while j < length:
                if input[i] + input[j] == target:
                    return [i, j]
                j = j + 1
            i = i + 1
        return [-1, -1]

    @staticmethod
    def findTwoNumbersIndexesOptimized(input, target):
        i = 0
        length = len(input)
        inputPositionMap = {}
        while i < length:
            delta = target - input[i]
            print(delta)
            if inputPositionMap.__contains__(delta):
                return [inputPositionMap.get(delta), i]
            else:
                inputPositionMap.update({input[i]: i})
            i = i + 1
        print(inputPositionMap)
        return [-1, -1]

    @staticmethod
    def sumOfTwoListInReverseOrder(list1, list2):
        input1 = ""
        input2 = ""
        length1 = len(list1) - 1
        length2 = len(list2) - 1

        while length1 >= 0:
            input1 = input1 + str(list1[length1])
            length1 = length1 - 1

        while length2 >= 0:
            input2 = input2 + str(list2[length2])
            length2 = length2 - 1

        result = int(input1) + int(input2)
        output = []
        print(result)
        if result == 0:
            return [0]
        while result > 0:
            out = result % 10
            output.append(out)
            result = int(result / 10)

        return output


if __name__ == '__main__':
    # but complexity is O(n^2)
    # print(LeetcodeProblems.findTwoNumbersIndexes([1, 2, 3, 4], 3))
    #  complexity is O(n)
    # print(LeetcodeProblems.findTwoNumbersIndexesOptimized([1, 2, 3, 4], 7))

    print(LeetcodeProblems.sumOfTwoListInReverseOrder([2, 4, 3], [5, 6, 4]))
    print(LeetcodeProblems.sumOfTwoListInReverseOrder([1], [1]))
    print(LeetcodeProblems.sumOfTwoListInReverseOrder([0], [0]))
