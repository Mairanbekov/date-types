# Работа с модулями: создание, подключение инструкциями import и from!
#    Модулем в Python называется любой файл с программой (да-да, все те программы, которые вы писали, можно назвать модулями).
# Первый шаг
# Подключение модуля из стандартной библиотеки
# Подключить модуль можно с помощью инструкции import. К примеру, подключим модуль os для получения текущей директории: import os
# После ключевого слова import указывается название модуля. Одной инструкцией можно подключить несколько модулей, хотя этого не рекомендуется делать, так как это снижает читаемость кода. 
# После импортирования модуля его название становится переменной, через которую можно получить доступ к атрибутам модуля. Например, можно обратиться к константе e, расположенной в модуле math:
# Стоит отметить, что если указанный атрибут модуля не будет найден, возбудится исключение AttributeError. А если не удастся найти модуль для импортирования, то ImportError.

# Использование псевдонимов!
# Если название модуля слишком длинное, или оно вам не нравится по каким-то другим причинам, то для него можно создать псевдоним, с помощью ключевого слова as.
# import math as mt
# print(mt)
# Теперь доступ ко всем атрибутам модуля math осуществляется только с помощью переменной m, а переменной math в этой программе уже не будет (если, конечно, вы после этого не напишете import math, 
# тогда модуль будет доступен как под именем m, так и под именем math).

# Инструкция from!
# Подключить определенные атрибуты модуля можно с помощью инструкции from. Она имеет несколько форматов:

# from <Название модуля> import <Атрибут 1> [ as <Псевдоним 1> ], [<Атрибут 2> [ as <Псевдоним 2> ] ...]
# from <Название модуля> import *
# Первый формат позволяет подключить из модуля только указанные вами атрибуты. Для длинных имен также можно назначить псевдоним, указав его после ключевого слова as.

# Практика

# def pos():
#     print('hello')


# pos()

# 2

# (As) бул узун бублатекадагы кана создорду кана кыскарта алат 

# import math as mt

# print(mt)

# from set import s
# print(s) 


# 1) Modul - Бул деп  биз (python тилинде папканы айтабыз )
# 2) Ал эми пакет бул (python тилинде внещний файлды айтабыз)
# 3) Modul - Бул экиге болунот (внешний , ички)
# 4) Ал эми биз пакет деп главный ( PYTHONду ) айтабыз

