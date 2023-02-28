def list_dict(index):
  arr_index = index.split()

  firstNum = arr_index[0]
  lastNum = arr_index[2]

  if (len(firstNum) > 4 or len(lastNum) > 4):
    return "Error: Numbers cannot be more than four digits."

  eqLength = len(firstNum) if len(firstNum) > len(lastNum) else len(lastNum)

  try:
    firstNum = int(firstNum)
    lastNum = int(lastNum)
  except:
    return "Error: Numbers must only contain digits."

  operation = arr_index[1]

  if (operation != "+" and operation != "-"):
    return "Error: Operator must be '+' or '-'."

  total = firstNum + lastNum if operation == "+" else firstNum - lastNum

  return {
    "firstNum": firstNum,
    "lastNum": lastNum,
    "operation": operation,
    "total": total,
    "eqLength": eqLength,
  }


def g_char(tchar, char_length):
  string = ""
  for i in range(0, char_length):
    string += tchar
  return string


def arithmetic_arranger(problems, show_answers=False):
  probs_length = len(problems)

  struct_problems = list(map(list_dict, problems))

  # structuring output and error checking
  output = ""
  for i, problem in enumerate(struct_problems):
    if (type(problem) == str):
      return problem

    firstNum = str(problem['firstNum'])
    calc_space = problem["eqLength"] - len(firstNum)
    beforefnum = "  " + g_char(" ", 0 if calc_space < 0 else calc_space)
    afterfnum = "    " if i < len(struct_problems) - 1 else "\n"

    output += beforefnum + firstNum + afterfnum


  for i, problem in enumerate(struct_problems):
    lastNum = str(problem['lastNum'])
    calc_space = problem["eqLength"] - len(lastNum)
    beforefnum = problem["operation"] + " " + g_char(" ", 0 if calc_space < 0 else calc_space)
    afterfnum = "    " if i < len(struct_problems) - 1 else "\n"

    output += beforefnum + lastNum + afterfnum

  
  for i, problem in enumerate(struct_problems):
    afterborder = "    " if i < len(struct_problems) - 1 else ""
    output += g_char("-", problem['eqLength'] + 2) + afterborder

  if (show_answers):
    output += "\n"

    for i, problem in enumerate(struct_problems):
      total = str(problem['total'])
      calc_space = problem["eqLength"] + 2 - len(total)
      beforefnum = g_char(" ", 0 if calc_space <= 0 else calc_space)

      afteranswer = "    " if i < len(struct_problems) - 1 else ""

      output += beforefnum + total + afteranswer

  if (probs_length > 5):
    return "Error: Too many problems."

  return output
