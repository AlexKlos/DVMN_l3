import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')

letter = 'From: {3}' \
         '\nTo: {4}' \
         '\nSubject: Приглашение!' \
         '\nContent-Type: text/plain; charset="UTF-8";' \
         '\n\nПривет, {2}! {1} приглашает тебя на сайт {0}!' \
         '\n\n{0} — это новая версия онлайн-курса по программированию.' \
         '\nИзучаем Python и не только. Решаем задачи. Получаем ревью от ' \
         'преподавателя.' \
         '\n\nКак будет проходить ваше обучение на {0}? ' \
         '\n\n→ Попрактикуешься на реальных кейсах. ' \
         '\nЗадачи от тимлидов со стажем от 10 лет в программировании.' \
         '\n→ Будешь учиться без стресса и бессонных ночей. ' \
         '\nЗадачи не «сгорят» и не уйдут к другому. Занимайся в удобное время ' \
         'и ровно столько, сколько можешь.' \
         '\n→ Подготовишь крепкое резюме.' \
         '\nВсе проекты — они же решение наших задачек — можно разместить на ' \
         'твоём GitHub. Работодатели такое оценят. ' \
         '\n\nРегистрируйся → {0}  ' \
         '\nНа курсы, которые еще не вышли, можно подписаться и получить ' \
         'уведомление о релизе сразу на имейл.'

ref_link = 'https://dvmn.org/profession-ref-program/zverohren/F925v/'
my_name = 'AlexKlos'
friend_name = 'Oshin'
mail_from = 'klos@list.ru'
mail_to = 'zverohren@gmail.com'

letter = letter.format(ref_link, my_name, friend_name, mail_from, mail_to)
letter = letter.encode('UTF-8')

server = smtplib.SMTP_SSL('smtp.mail.ru:465')
server.login(LOGIN, PASSWORD)
server.sendmail(mail_from, mail_to, letter)
server.quit()
