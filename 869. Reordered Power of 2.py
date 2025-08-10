class Solution:
    def get_num_count_dic(self, num_str: str) -> dict:
        tmp = {}
        for num_char in num_str:
            if num_char not in tmp:
                tmp[num_char] = 0
            tmp[num_char] += 1
        return tmp

    def reorder_string_compare(self, a: str, b: str) -> bool:
        a_count = self.get_num_count_dic(a)
        b_count = self.get_num_count_dic(b)
        return a_count == b_count
    
    def reorderedPowerOf2(self, n: int) -> bool:
        power_list = {}
        tmp = 1
        for i in range(31):
            l = len(str(tmp))
            if l not in power_list:
                power_list[l] = []
            power_list[l].append(str(tmp))
            tmp *= 2

        l = len(str(n))
        for target in power_list[l]:
            if self.reorder_string_compare(str(n), target):
                return True
        return False
