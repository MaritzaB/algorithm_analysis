def count_expressions(numbers, target_result):
    def count(index, partial_result):
        """
        Counts the number of expressions equal to `target_result`,
        given that the first `index` operators have been assigned,
        thus the left part of the expression is equal to `partial_result`.
        """
        if index == len(numbers):
        # We formed a full expression. Count it if we hit the target.
            if partial_result == target_result:
            return 1
        return 0
    # For the operator before `numbers[index]`, we have two options:
    # Add the `+` sign:
    count_add = count(index + 1, partial_result + numbers[index])
    # Add the `­` sign:
    count_sub = count(index + 1, partial_result ­ numbers[index])
    # Each option may yield some valid expressions. Sum up the counters.
    return count_add + count_sub
    first_index = 1
    partial_result = numbers[0]
    return count(first_index, partial_result)