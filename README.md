## Two Pointer Function And Palindrome 

Check whether characters in a string are palindrome or not using two pointer function

**A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward.**

- create a string inside a valiable
- from the left of the string or the start of the string equal to zero
- To the left equals the length of the string minus 1 which represent the last character
- Use a while loop to check if left is less than right or start is less than end, meaning start will not go above or beyond end.

After that this is what will happen:
- if the first character is not the last character return "is not palindrome" otherwise return is palindrome 
Otherwise it will print "is Palindrome" whereby the while loop condition iterate by start going forword with end going backwords

For more info on palidrome [Leetcode medium](https://medium.com/@timpark0807/leetcode-is-easy-two-pointers-90b9b0f2eb43)


## Palindrome
A palindrome is a word that reads the same forward and backward.

In a valid palindrome, the first and last letter of the input must be the same, the second and second to last letter must be the same, the third and third to last must be the same, and so on until we’ve checked every letter in the input.

- Letters are equal, input could be a palindrome.
- Letters are not equal, input cannot be a palindrome.
