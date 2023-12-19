from variables2 import text, line_length
def minimize_spaces(words, line_length):
    memo = {}

    def dp(start):
        if start == len(words):
            return 0, []

        if start in memo:
            return memo[start]

        min_cost = float('inf')
        best_lines = []

        for end in range(start + 1, len(words) + 1):
            line = ' '.join(words[start:end])
            remaining_spaces = line_length - len(line)
            if remaining_spaces >= 0:
                cost, lines = dp(end)
                # print(cost, lines)
                cost += remaining_spaces
                lines = [line] + lines

                if cost < min_cost:
                    min_cost = cost
                    best_lines = lines

        memo[start] = (min_cost, best_lines)
        # print(min_cost)
        return memo[start]


    cost, result_lines = dp(0)
    print(cost)
    return result_lines

words = text.split()

result = minimize_spaces(words, line_length)
for line in result:
    print(line)
