import re

def arithmetic_arranger(problems, show_ans=False):

	# initialise empty strings
	line1 = ""
	line2 = ""
	line3 = ""
	line4 = ""
	
	# First rule: ensure length of problem list is 5 or less
	if len(problems) > 5:
		return "Error: Too many problems."
	else:
		for problem in problems:
			P = problem.strip() # in case user includes leading or trailing whitespace
			
			# if re.search(expected_pattern, P) is not None:
			first_num = P.split()[0]
			operator = P.split()[1]
			second_num = P.split()[2]

			# Second rule: check whether operator is neither addition nor subtraction
			if operator != "+" and operator != "-":
				return "Error: Operator must be '+' or '-'."

			# Third rule: check if numbers contain non-digit characters (regex \D (inverse of \d))
			elif re.search(r"\D", first_num) is not None or re.search(r"\D", second_num) is not None:
				return "Error: Numbers must only contain digits."

			# Fourth rule: check that each number is 4 digits long at most
			elif len(first_num) > 4 or len(second_num) > 4:
				return "Error: Numbers cannot be more than four digits."

			else:
				gap = " " * 4 # four spaces between each problem
				width = max(len(first_num), len(second_num)) + 2

				# concat strings in the correct format for each line
				# each loop iteration appends new values to the strings
				line1 += first_num.rjust(width) + gap
				line2 += operator + second_num.rjust(width - 1) + gap
				line3 += "-" * width + gap
				line4 += str(eval(problem)).rjust(width) + gap

	# for i in range(1, 5):
		# eval(f"vars().update(dict(line{i}=line{i}.rstrip()))")

	# remove trailing whitespace; we only need space between arithmetic problems
	line1 = line1.rstrip()
	line2 = line2.rstrip()
	line3 = line3.rstrip()
	line4 = line4.rstrip()
	
	if show_ans is True:
		arranged_problems = f"{line1}\n{line2}\n{line3}\n{line4}"
	else:
		arranged_problems = f"{line1}\n{line2}\n{line3}"
		
	return arranged_problems