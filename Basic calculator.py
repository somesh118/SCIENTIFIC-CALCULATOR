# This program performs basic calculator operations
def main():
  print("Choose an operation:")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  choice = int(input("Enter your choice (1-4): "))

  num1 = float(input("Enter the first operand: "))
  num2 = float(input("Enter the second operand: "))

  if choice == 1:
    result = num1 + num2
  elif choice == 2:
    result = num1 - num2
  elif choice == 3:
    result = num1 * num2
  elif choice == 4:
    result = num1 / num2
  else:
    print("Invalid choice")
    return

  # Print the result
  print("The result is", result)

main()
