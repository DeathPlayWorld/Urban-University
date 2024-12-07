
def calculate_structure_sum(structure):
  _type = check_type(structure)
  if _type == "array":
    for i in range(0, len(structure)): calculate_structure_sum(structure[i])
  else: return solve(structure, _type)

def check_type(_structure_to_check):
  if isinstance(_structure_to_check, str): return "str"
  elif isinstance(_structure_to_check, int) or isinstance(_structure_to_check, float): return "number"
  elif isinstance(_structure_to_check, set): return "set"
  elif isinstance(_structure_to_check, dict): return "dict"
  elif isinstance(_structure_to_check, list) or isinstance(_structure_to_check, tuple): return "array"
  elif _structure_to_check is None: return "none"

def solve(structure, type_structure):
  global final_answer
  match type_structure:
    case "none":
      final_answer += 0
    case "str":
      final_answer += len(structure)
    case "number":
      final_answer += structure
    case "dict":
      for key in dict(structure).keys(): final_answer += len(key)
      for value in dict(structure).values(): final_answer += value
    case "set": calculate_structure_sum(list(structure))

data_structure = [                                # For debug purpose only:
  [1, 2, 3],                                      # [0]   1 + 2 + 3 = 6
  {'a': 4, 'b': 5},                               # [1]   1 + 4 + 1 + 5 = 11
  (6, {'cube': 7, 'drum': 8}),                    # [2]   6 + 4 + 7 + 4 + 8 = 29
  "Hello",                                        # [3]   "Hello" = 5
  ( (), [{(2, 'Urban', ('Urban2', 35))}] )        # [4]   0 + 2 + 5 + 6 + 35 = 48
]                                                 #  ->   6 + 11 + 29 + 5 + 48 = 99

final_answer = 0

calculate_structure_sum(data_structure)
print(final_answer)