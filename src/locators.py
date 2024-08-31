from selenium.webdriver.common.by import By

class RegistrationLocators:
    LOGIN_IN_ACCOUNT_BOTTON = By.XPATH, ".//button[text()='Войти в аккаунт']"
    REGISTRATION_BUTTON = By.XPATH, ".//a[@href='/register']" #Кнопка "Зарегистрироваться"
    NAME_FIELD = By.





    EMAIL_FIELD = By.XPATH, ".//input[@name='name']"
    PASSWORD_FIELD = By.XPATH, ".//input[@name='Пароль']"


"""
Регистрация
Проверь:
Успешную регистрацию.
Поле «Имя» должно быть не пустым;
в поле Email введён email в формате логин@домен: например, 123@ya.ru.
Минимальный пароль — шесть символов.
Ошибку для некорректного пароля.
"""