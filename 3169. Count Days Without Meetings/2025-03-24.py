from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        merge_meeting = []
        for meeting in meetings:
            if not merge_meeting:
                merge_meeting.append(meeting)
            last_meeting = merge_meeting[-1]
            if meeting[0]>last_meeting[1]:
                merge_meeting.append(meeting)
            else:
                if meeting[1]>last_meeting[1]:
                    merge_meeting[-1][1] = meeting[1]

        count = 0
        merge_len = len(merge_meeting)
        for i in range(merge_len):
            if i == 0:
                if merge_meeting[0][0] != 1:
                    rest_day = merge_meeting[0][0] - 1
                    count += rest_day
            if i == merge_len-1:
                rest_day = days-merge_meeting[i][1]
                if rest_day!=0:
                    count += rest_day
                break
            rest_day = merge_meeting[i+1][0]-merge_meeting[i][1]-1
            count += rest_day

        return count