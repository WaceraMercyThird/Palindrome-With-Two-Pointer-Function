# 2 pointer function
# palindrome
# compare sequence of characters if it palindrom using two pointer function 
# A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward.


expression = "I am AkiraChix"
left = 0 
right = len(expression) - 1
while left < right:
    if expression[left] != expression[right]:
        print("Not palindrome")
    else:
        left += 1        
        right -= 1
print("Is palindrome")