## Тестовое задание

* Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
* Django Модель `Item` с полями `(name, description, price) `
* API с двумя методами:
    * GET `/buy/{id}`, c помощью которого можно оплатить покупку для оплаты выбранного Item.
    * GET `/item/{id}`, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о
      выбранном `Item` и кнопка Buy.

* Запуск используя `Docker`

* Использование environment variables

* Просмотр Django Моделей в Django Admin панели - доступно по адресу `127.0.0.1:8000/admin`

* Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items

* Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме

* Реализовать не Stripe Session, а Stripe Payment Intent.




Создайте в корне проекта .env и запишите следующие поля:
DEBUG=True
ALLOWED_HOSTS=localhost 127.0.0.1

SECRET_KEY = Ваш SECRET_KEY

STRIPE_PUBLIC_KEY = С сайта https://dashboard.stripe.com/apikeys после регистрации
STRIPE_SECRET_KEY = С сайта https://dashboard.stripe.com/apikeys после регистрации



Запуск
------

```
git clone https://github.com/timoshenkost/rishat_test
cd rishat_test
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
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
* `buy/<item_id>` - Покупка по id через Stripe Payment Inten
* `item/<item_id>` - Отдаёт информацию о товаре по id 
* `order/<slug>` - Отдаёт информацию о заказе по slug
* `buy_order/<slug>` - Покупка заказа по slug через Stripe Session


