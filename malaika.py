def is_valid_word(word):
    """Check if word is a valid operation or number word."""
    operations = {'add', 'sub', 'mul', 'rem', 'pow', 'div'}
    digits = {'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'}

    # Check if it's an operation
    if word in operations:
        return True

    # Check if it's a number word
    parts = word.split('c')
    return all(part in digits for part in parts)


def word_to_digit(word):
    """Convert a word number to its digit."""
    digit_map = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    return digit_map.get(word, '')


def parse_number(word):
    """Convert a word sequence to a number."""
    if 'c' not in word:
        return word_to_digit(word)

    parts = word.split('c')
    return ''.join(word_to_digit(part) for part in parts)


def evaluate_operation(op, num1, num2):
    """Evaluate a single operation."""
    num1, num2 = int(num1), int(num2)

    if op == 'add':
        return num1 + num2
    elif op == 'sub':
        return num1 - num2
    elif op == 'mul':
        return num1 * num2
    elif op == 'div':
        if num2 == 0:
            raise ValueError("Division by zero")
        return num1 // num2
    elif op == 'rem':
        if num2 == 0:
            raise ValueError("Modulo by zero")
        return num1 % num2
    elif op == 'pow':
        return num1 ** num2

    raise ValueError("Invalid operation")


def evaluate_expression(words):
    """Evaluate the complete expression."""
    # Check for valid words first
    if not all(is_valid_word(word) for word in words):
        return "expression evaluation stopped invalid words present"

    try:
        # Single operation case: op num1 num2
        if len(words) == 3:
            op, num1, num2 = words
            num1 = parse_number(num1)
            num2 = parse_number(num2)
            return evaluate_operation(op, num1, num2)

        # Double operation cases
        elif len(words) == 5:
            # Case 1: op1 op2 num1 num2 num3
            if words[1] in {'add', 'sub', 'mul', 'rem', 'pow', 'div'}:
                op1, op2, num1, num2, num3 = words
                num1 = parse_number(num1)
                num2 = parse_number(num2)
                num3 = parse_number(num3)
                temp = evaluate_operation(op2, num2, num3)
                return evaluate_operation(op1, num1, temp)

            # Case 2: op1 num1 op2 num2 num3
            else:
                op1, num1, op2, num2, num3 = words
                num1 = parse_number(num1)
                num2 = parse_number(num2)
                num3 = parse_number(num3)
                temp = evaluate_operation(op2, num2, num3)
                return evaluate_operation(op1, num1, temp)

        return "expression is not complete or invalid"

    except (ValueError, ZeroDivisionError):
        return "expression is not complete or invalid"


def main():
    try:
        # Read input
        expression = input().strip().split()

        # Evaluate expression
        result = evaluate_expression(expression)

        # Print result
        if isinstance(result, int):
            print(result)
        else:
            print(result)

    except Exception:
        print("expression is not complete or invalid")


if __name__ == "__main__":
    main()