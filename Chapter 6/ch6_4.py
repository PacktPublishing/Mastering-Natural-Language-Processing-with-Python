import nltk
input_expr = nltk.sem.Expression.fromstring
expression = input_expr('run(marcus)', type_check=True)
print(expression.argument)
print(expression.argument.type)
print(expression.function)
print(expression.function.type)
sign = {'run': '<e, t>'}
expression = input_expr('run(marcus)', signature=sign)
print(expression.function.type)
