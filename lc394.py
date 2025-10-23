class Solution:
    def decodeString(self, s: str) -> str:
        stack = []          # To store (previous_string, repeat_count)
        current_str = ""    # Current substring being built
        current_num = 0     # Current repeat number

        for ch in s:
            if ch.isdigit():
                current_num = current_num * 10 + int(ch)  # Handle multi-digit numbers
            elif ch == '[':
                stack.append((current_str, current_num))  # Save current state
                current_str = ""
                current_num = 0
            elif ch == ']':
                prev_str, num = stack.pop()               # Pop previous state
                current_str = prev_str + current_str * num
            else:
                current_str += ch                         # Add character

        return current_str

        