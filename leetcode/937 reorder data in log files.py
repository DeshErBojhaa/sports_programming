class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs, text_logs = [], []
        for l in logs:
            if l.split()[1].isdigit():
                digit_logs.append(l)
            else:
                text_logs.append(l)
        
        text_logs.sort(key=lambda l:(l.split()[1:], l.split()[0]))
        return text_logs + digit_logs
