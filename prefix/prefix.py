def prefix_to_infix(expression):
    stack = []
    operators = set(['+', '-', '*', '/'])

    # Разбиваем выражение на элементы
    tokens = expression.split()

    # Обрабатываем элементы в обратном порядке
    for token in reversed(tokens):
        if token in operators:
            # Операция: извлекаем два операнда из стека
            operand1 = stack.pop()
            operand2 = stack.pop()
            # Формируем инфиксное выражение
            new_expr = f'({operand1} {token} {operand2})'
            stack.append(new_expr)
        else:
            # Операнд: добавляем в стек
            stack.append(token)

    # В стеке должен остаться один элемент - итоговое инфиксное выражение
    return stack[0] if stack else ""
