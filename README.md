# Online Market

_____
1) Необходимо выполнить для установки зависимостей:
```
pip install -r requirements.txt
```
2) Запустим бд Postgres в докере командой:
```
docker-compose up
```
3) Выполним миграцию бд:
```
cd data_base
alembic upgrade head
```
4) Подключимся к бд и проверим, что миграция выполнена успешно и соответствует схеме, представленной в __/documentation/table_schema.png__:
```
psql -h localhost -p 5432 -U user postgres
\dt;
\di;
\d "CartList";

```
5) Перед проведением тестирования микросервиса необходимо добавить объект Cart. (подразумевается, что объект должен создаваться при создании пользователя: владельца корзины)
Но мы создадим сами, при помощи выполнения следующий команды:
```
python3 init_cart_temp_file.py
```
_____
### Тестирование ручек
Ручки микросервиса описаны в файле __documentation/OnlineMarker.yaml__

**Запустим микросервис** командой:
> python3 app.py

**Запустим БД** командой:
> docker-compose up

Для тестирования можно воспользоваться представленными ниже curl запросами:
```
curl  -H 'Content-Type: application/json' --data '{"name":"SmartD","manufacturer":"NikSul", "price":10001}' http://localhost:8080/product
curl  -H 'Content-Type: application/json' --data '{"name":"InterP","manufacturer":"NikSul", "price":5555}' http://localhost:8080/product
curl  -H 'Content-Type: application/json' --data '{"name":"ABC","manufacturer":"Somebody", "price":123}' http://localhost:8080/product



curl http://localhost:8080/product
curl "http://localhost:8080/product?price_min=0&price_max=200000&sorting=name_down"
curl "http://localhost:8080/product?price_min=0sorting=name_up"
curl "http://localhost:8080/product?sorting=price_up"
curl "http://localhost:8080/product?price_max=200000&sorting=price_down"
curl "http://localhost:8080/product?price_max=6000&sorting=price_down"
curl "http://localhost:8080/product?price_min=5800&price_max=6000"
curl "http://localhost:8080/product?manufacturer=NikSul"
curl "http://localhost:8080/product?name=ABC"
curl "http://localhost:8080/product?name=NO_NAME"


curl "http://localhost:8080/product?price_min=0&price_max=-500"


curl  -H 'Content-Type: application/json' --data '{"cart_id":1, "product_id":1}' http://localhost:8080/cart
curl  -H 'Content-Type: application/json' --data '{"cart_id":1, "product_id":2}' http://localhost:8080/cart

curl  -X PUT -H 'Content-Type: application/json' --data '{"cart_id":1, "product_id":1, "count": 10}' http://localhost:8080/cart
curl  -X PUT -H 'Content-Type: application/json' --data '{"cart_id":1, "product_id":1, "count": -11}' http://localhost:8080/cart

curl  -X PUT -H 'Content-Type: application/json' --data '{"cart_id":1, "product_id":1, "count": -11}' http://localhost:8080/cart

curl  -X PUT -H 'Content-Type: application/json' --data '{"cart_id":1, "product_id":1, "count": 11}' http://localhost:8080/cart

```

Информация о событиях записывается в logger.log (не все события)