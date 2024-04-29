
score = 0

quelist = {
    "1. What is the name of the newspaper that reported and publish by the children?": "balaknama",
    "2. seating capacity of narendra modi stadium(NMS)?": "132000",
    "3. where is the worlds biggest dining table?": "hyderabad",
    "4. national vegetable of our india?": "pumpkin",
    "5. which city is known as white city of india?": "udaipur"
}


for que, ans in quelist.items():
	user_ans = input(que + "\n your answer: " + " ")
	if user_ans.lower() == ans.lower():
		print("yeahh! you are correct! you got 1 point.")
		score += 1
	else:
		print(f"oopc! ypu are incorrect! The correct answer is {ans}.")
print("your score is " + str(score) + " thank you!")