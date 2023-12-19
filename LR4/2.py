def minimize_spaces(words, line_length):
    n = len(words)
    dp = [float('inf')] * n
    spaces = [0] * n

    for i in range(n - 1, -1, -1):
        remaining_spaces = line_length - len(words[i])
        dp[i] = remaining_spaces ** 3 + (dp[i + 1] if i + 1 < n else 0)
        spaces[i] = i + 1 if i + 1 < n else 0

        for j in range(i + 1, n):
            remaining_spaces -= len(words[j]) + 1
            if remaining_spaces < 0:
                break

            current_cost = remaining_spaces ** 3 + (dp[j + 1] if j + 1 < n else 0)
            if current_cost < dp[i]:
                dp[i] = current_cost
                spaces[i] = j - i

    lines = []
    i = 0
    while i < n:
        lines.append(' '.join(words[i:i + spaces[i] + 1]))
        i += spaces[i] + 1
    print(i)
    return lines


# Приклад використання
text = "У процесі формування тексту в текстовому редакторі виникає завдання переносу слів за рядками. Для розв’язання даного завдання задається текст, який складається з деякого набору слів, та кількість символів, яка може міститися в одному рядку."
words = text.split()
line_length = 50

result = minimize_spaces(words, line_length)
for line in result:
    print(line)
