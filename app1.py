print("Welcome to my Quiz Game ")
print("You need to answer my Questions:")
Questions = ["Cinema in Bremen ?", "Universum in Bremen ", "Haupstadt von Thüringen", "Money in Germanny", "How cost a Gold Ingot", "A Game in Amerika"]
Answers = ["Cinestar", "Universum Bremen", "Erfurt", "Euro", "55.000$", "Minecraft"]
score = 0
print(Questions[0])
user_input = input("Please wrote your answers here")
if user_input.lower() == Answers[0].lower():
  print("Right")
  score = score +1
else:
  print("Wrong")

print(Questions[1])
user_input = input("Please wrote your answers here")
if user_input.lower() == Answers[1].lower():
  print("Right")
  score = score +1
else:
 print("Wrong")

print(Questions[2])
user_input = input("Please wrote your answers here")
if user_input.lower() == Answers[2].lower():
  print("Right")
  score = score +1 
else:
 print("Wrong")

print(Questions[3])
user_input = input("Please wrote your answers here")
if user_input.lower() == Answers[3].lower():
  print("Right")
  score = score +1
else:
  print("Wrong")
  
print(Questions[4])
user_input = input("Please wrote your answers here")
if user_input.lower() == Answers[4].lower():
  print("Right")
  score = score +1
else:
  print("Wrong")

print(Questions[5])
user_input = input("Please wrote your answers here ")
if user_input.lower() == Answers[5].lower():
  print("Right")
  score = score +1
else:
  print("Wrong")

if score > 5:
  print("Oh this is a best result")
elif score > 3 :
   print("Oh this a good score")
else:
  print("In the next try your good it better")