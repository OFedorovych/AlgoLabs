# AlgoLabs

Завдання:

Код задачi: WCHAIN

Двоє учасникiв грають у лiнгвiстичну гру. На початку гри дано список iз N слiв.
Перший гравець обирає довiльне слово w1 i викреслює з нього одну довiльну лiтеру
так, щоб отримати iнше слово w2 з цього списку. Пiсля цього хiд переходить до
iншого гравця, i вiн намагається зробити те саме зi словом w2.
Гра завершується в одному з двох випадкiв:
• Залишається слово з однiєї лiтери.
• Неможливо викреслити жодну лiтеру так, щоб отримати iнше слово зi словника.

Визначте довжину максимального ланцюжка, якого можна досягти в цiй грi при
заданих словах.
Вхiднi данi
Вхiдний файл wchain .in складається з N + 1 рядкiв.
• Перший рядок мiстить N — кiлькiсть слiв у словнику, 1 ≤ N ≤ 105
.

• Кожен з наступних N рядкiв мiстить слово довжиною вiд 1 до 50 символiв, яке
складається з малих латинських лiтер вiд a до z.
Вихiднi данi
Вихiдний файл wchain .out повинен мiстити одне число — довжина максимального
ланцюжка.
