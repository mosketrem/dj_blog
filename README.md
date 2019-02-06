Укр/Eng

Це звичайний простий пробний проект. Має примітивну верстку, дозволяє реєструватись користувачам, редагувати свої обліковки, переглядати обліковки інших користувачів, створювати дописи та редагувати їх.

В налаштуваннях `settings.py` є параметри для GMail обліковки, з якої надсилатиметься лист для активації користувача. Адреса та пароль до цієї скриньки беруться з середовища машини, на якій працюватиме цей проект. Внести ці дані туди - в середовище змінних - можна так:

`export EMAIL_ADDRESS=<gmail address>`

`export EMAIL_PASSWORD=<your gmail password`

Активувати користувачів не обов'язково, в проекті зробено два методи реєстрації: один з активацією, другий - без.

Також є скрипт для запуску проекту в режимі `DEBUG`. Використовується цей скрипт так:

`./run_dev.sh`

---

This is simple test project. It has poor HTML layout, allows users to register, edit their profiles and see other users' ones, create and edit posts.

In the `settings.py` there are parameters for a GMail account used to send activations codes to new users. The address and the password are taken from environment variables. You can put that data into environment this way:

`export EMAIL_ADDRESS=<gmail address>`

`export EMAIL_PASSWORD=<your gmail password`

You don't have to activate users. The project contains two methods of registration: one with activation and second - without it.

There is also the script for running the project in a `DEBUG` mode. You can use it like this:

`./run_dev.sh`


