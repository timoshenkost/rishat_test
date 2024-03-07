## Тестовое задание

* Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
* Django Модель `Item` с полями `(name, description, price) `
* API с двумя методами:
    * GET `/buy/{id}`, c помощью которого можно оплатить покупку для оплаты выбранного Item.
    * GET `/item/{id}`, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о
      выбранном `Item` и кнопка Buy.

* Запуск используя Docker

* Использование environment variables

* Просмотр Django Моделей в Django Admin панели

* Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items

* Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме

* Реализовать не Stripe Session, а Stripe Payment Intent.



Подготовка
------
Введите следующие команды
```
git clone https://github.com/timoshenkost/rishat_test
cd rishat_test
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

Создайте в корне rishat_test файл `.env` и запишите следующие поля:
```
DEBUG=True
ALLOWED_HOSTS=localhost 127.0.0.1
SECRET_KEY = Ваш SECRET_KEY
STRIPE_PUBLIC_KEY = Ваш STRIPE_PUBLIC_KEY с сайта https://dashboard.stripe.com/apikeys после регистрации
STRIPE_SECRET_KEY = Ваш STRIPE_SECRET_KEY с сайта https://dashboard.stripe.com/apikeys после регистрации
```

Настройка базы данных
```
python manage.py migrate
```

#### Для админ панели:
```
python manage.py createsuperuser
```

Запуск Docker
------

```
docker build -t rishat_test .
docker run --name rishat_test_container -p 8000:8000 rishat_test
```

Сервис
------


* `admin/` - Админка
* `item/<item_id>` - Информация о товаре по id 
* `buy/<item_id>` - Покупка по id через Stripe Payment Inten
* `order/<slug>` - Информация о заказе по slug
* `buy_order/<slug>` - Получить индефикатор сессии для Stripe Session


