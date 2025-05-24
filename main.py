print("👋 Welcome to the Armstrong Number Checker!")
print("Enter any number and I will tell you if it's an Armstrong number! 🤓\n")

# User input
num = int(input("🔢 Enter a number: "))

# Calculate number of digits
power = len(str(num))

# Calculate Armstrong sum
armstrong_sum = sum(int(digit) ** power for digit in str(num))

# Check and respond
if num == armstrong_sum:
    print(f"🎉 Yes! {num} is an Armstrong number!")
else:
    print(f"❌ Nope! {num} is not an Armstrong number.")