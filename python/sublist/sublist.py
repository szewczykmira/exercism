EQUAL = 0
UNEQUAL = -2
SUBLIST = -1
SUPERLIST = 1


class CheckList:
    def __init__(self, list1, list2):
        self.first = list1
        self.second = list2

    def equal(self):
        if self.first == self.second:
            return EQUAL
        return UNEQUAL

    def sublist(self):
        return self.contains(self.first, self.second)
        # SUBLIST

    def superlist(self):
        return self.contains(self.second, self.first)
        # SUPERLIST

    def contains(self, first, second):
        len_first = len(first)
        len_second = len(second)
        if not len_first < len_second:
            return False
        for i in range(0, len_second - len_first + 1):
            if second[i : i + len_first] == first:
                return True
        return False

def check_lists(first, second):
    check = CheckList(first, second)
    if check.superlist():
        return SUPERLIST
    if check.sublist():
        return SUBLIST
    return check.equal()

