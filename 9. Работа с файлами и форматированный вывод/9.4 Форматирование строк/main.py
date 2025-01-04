team1_num = 5
team2_num = 6
team1_time = 1552.512
team2_time = 2153.31451
score_1 = 40
score_2 = 42
#Использование %
print("\nВ команде Мастера кода участников: %i!" % team1_num)
print("Итого сегодня в командах участников: %i из %i!" % (team1_num, team2_num))
#Использование format()
print("\nКоманда Волшебники данных решила задач: {score_2}!".format(score_2= score_2))
print("Волшебники данных решили задачи за {team1_time} с!".format(team1_time=team1_time))
#Использование f-строк
print(f"\nКоманды решили {score_1} и {score_2} задач.")
if score_1 > score_2: challenge_result = "победа команды волшебников"
elif score_1 <score_2: challenge_result = "победа команды Мастера кода"
else: challenge_result = "Ничья"
print(f"Результат битвы: {challenge_result}!")
task_total = score_1 + score_2; time_avg = int((team1_time + team2_time) / task_total)
print(f"Сегодня было решено {task_total} задач, в среднем по {time_avg} секунды на задачу!")