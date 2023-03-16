def isPalindrome(s):
  if len(s)<=1:
    return "Yes"
  r=s[::-1]
  if r.lower()==s.lower():
    return "Yes"
  else:
    return "No"

s=input()
print(isPalindrome(s))