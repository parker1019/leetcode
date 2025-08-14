class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good_num_list = ["000", "111", "222", "333", "444", "555", "666", "777", "888", "999"]
        tmp = -1
        for good_num in good_num_list:
            if good_num in num:
                if int(good_num) > tmp:
                    tmp = int(good_num)
        if tmp == -1:
            return ""
        elif tmp == 0:
            return "000"
        return str(tmp)