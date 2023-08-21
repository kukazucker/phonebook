### phonebook

Описание программы:

аннотирование функций и переменных

В начале вы попадаете на начальный экран в котором вы можете выбрать следующие функции:

1. Посмотреть список всех записей;
2. Изменить существующую запись;
3. Создать новую запись;
4. Найти определённые(-ую) запись(-и);

Для выбора любой функции вам необходимо прописать соответствующую команду, как это прописано в меню. 


При запуске функции показа всех записей постранично (/show):
Сперва вам необходимо ввести количество сторок, которое желаете видеть. После этого перед вами отобразится список из выбранных строк из телефонного справочника. 
Вы можете: продолжить просмотр списков при помощи клавиши ENTER или же выйти из этого окна при помощи команды выхода (/exit). Если список закончится, то окно закроется автоматически и 
откроется главное меню.


При запуске функции изменения существующей записи (/edit):
Сперва вам необходимо знать ID той записи, которую вы хотите редактировать, найти номер строки вы можете при отображении всех записей или же при поиске (сам ID - это число перед фамилией).
Теперь вам необходимо ввести этот ID и нажать ENTER. После введения ID перед вам откроется окно с фамилией профиля или же отобразится сообщение о невозможности найти запись (попробуйте перепроверить ID или
такого аккаунта просто не существуюет). Теперь вы можете увидеть текущую фамилию профиля, которую вы можете поменять, но если вы не хотите менять этот параметр, то очистите окно ввода и нажмите ENTER и тогда вы сможете 
приступить к окну с именем и так до конца списка.


При запуске функции создания новой записи в справочнике (/new):
После ввода команды перед вами откроется окно, где вам необходимо ввести фамилию новой записи: введите фамилию и нажмите ENTER. И так до конца списка. В конце вы автоматически перейдёте на окно главного меню.


При запуске функции поиска записи в справочнике (/search):
После ввода команды перед вами откроется окно, где вам необходимо ввести интересующую вас информацию и значение, то есть, к примеру, вы хотите найти запись с фамилией Иванова: введите название 
характеристики для поиска "Фамилия" (без скобок) и нажмите на ENTER, теперь введите значение характеристики "Иванова" (без скобок) и нажмите ENTRER - теперь вы можете вводить неограниченное число таких характеристик,
однако если вы захотите отсановить набор характеристик, то отчистите поле ввода и нажмите на ENTER.


Техническая информацию:
проверено в mypy, необходим pandas для запуска (не знал точно, нужно ли было использовать лишь ванильную версию питона)
