def arithmetic_arranger(problems, answers=False):
  """
  Arranges arithmetic problems neatly in output format.

  Args:
    problems: A list of strings representing arithmetic problems.
    answers: A boolean indicating whether to include answers.

  Returns:
    A string representing the neatly arranged problems and optional answers.
  """

  if len(problems) > 5:
    return "Error: Too many problems."

  top_row = ""
  bottom_row = ""
  dashes = ""
  results = ""

  for problem in problems:
    operands = problem.split()
    if len(operands) != 3:
      return "Error: Invalid problem format."
    num1, operator, num2 = operands

    if not (operator == "+" or operator == "-"):
      return "Error: Operator must be '+' or '-'."

    if not (num1.isdigit() and num2.isdigit()):
      return "Error: Numbers must only contain digits."

    if len(num1) > 4 or len(num2) > 4:
      return "Error: Numbers cannot be more than four digits."

    width = max(len(num1), len(num2)) + 2

    top_row += num1.rjust(width) + "    "
    bottom_row += operator + " " + num2.rjust(width - 2) + "    "
    dashes += "-" * width + "    "

    if answers:
      if operator == "+":
        result = str(int(num1) + int(num2))
      else:
        result = str(int(num1) - int(num2))
      results += result.rjust(width) + "    "

  if answers:
    arranged_problems = top_row.rstrip() + "\n" + bottom_row.rstrip() + "\n" + dashes.rstrip() + "\n" + results.rstrip()
  else:
    arranged_problems = top_row.rstrip() + "\n" + bottom_row.rstrip() + "\n" + dashes.rstrip()

  return arranged_problems

# Example usage
problems = ["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"]
print(arithmetic_arranger(problems, True))