def list_dict(index):
  arr_index = index.split()

  try:
    firstNum = int(arr_index[0])
    lastNum = int(arr_index[2])
  except:
    return "Error: Numbers must only contain digits."

  if (len(firstNum) > 4 or len(lastNum) > 4):
    return "Error: Numbers cannot be more than four digits."

  operation = arr_index[1]
  eqLength = len(firstNum) if len(firstNum) > len(lastNum) else len(lastNum)

  if (operation != "+" and operation != "-"):
    return "Error: Operator must be '+' or '-'."

  return {
    "firstNum": firstNum,
    "operation": operation,
    "lastNum": lastNum,
    "eqLength": eqLength
  }


def arithmetic_arranger(problems, show_answers=False):
  if (len(problems) > 4):
    return "Error: too many problems."

  struct_problems = list(map(list_dict, problems))

  # structuring and error checking
  for problem in struct_problems:
    if (type(problem) == str):
      return problem

  return struct_problems
