FROM python:3.11.5

WORKDIR /app

ENV DEBUG=True
ENV ALLOWED_HOSTS='localhost 127.0.0.1'

ENV SECRET_KEY='django-insecure-gd%4djzj)*h-#^wdsx)lur+khx+*3y+!p_m568(bjc-0nr9qwt'
ENV STRIPE_PUBLIC_KEY='pk_test_51OqumWLF5mL9VX58RYvC3ZoxhqPmF174CRxolBPjZiNtre3HYyRWHBuru5xL5n7XFcreFhhSE6Uj2ipna0PXhwec002SDVegg8'
ENV STRIPE_SECRET_KEY='sk_test_51OqumWLF5mL9VX58vPWRqJoUpQJQPwbOrLEOpT5ke3eedmaba9uks92Eufo8GHVMESu3Whgbw0nVweGItXlrDmCi009HdbXSUv'

ENV DJANGO_SUPERUSER_USERNAME='admin'
ENV DJANGO_SUPERUSER_PASSWORD='admin'
ENV DJANGO_SUPERUSER_EMAIL='adm@adm.adm'


COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD sh -c 'python manage.py migrate && \
          python manage.py createsuperuser --noinput && \
          python manage.py runserver 0.0.0.0:8000'

