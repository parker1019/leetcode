class Solution:
    def maximum69Number (self, num: int) -> int:
        num_list = list(str(num))
        num_str = ""
        tmp = True
        for i in range(len(num_list)):
            if num_list[i] == "6" and tmp:
                num_list[i] = "9"
                tmp = False
            num_str += num_list[i]
        
        return int(num_str)