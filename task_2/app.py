import redis

with redis.Redis(host='redis', port=6379) as client:
    expression = input("Введите пример: ").lower().strip()
    while expression != 'stop':
        client.lpush('expressions', expression)
        expression = input("Введите пример: ").lower().strip()
print("Вы завершили программу")
