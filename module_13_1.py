import asyncio


# Асинхронная функция для имитации действий каждого силача
async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')

    # Поднятие каждого из 5 шаров с соответствующей задержкой
    for i in range(1, 6):
        await asyncio.sleep(1 / power)  # задержка обратно пропорциональна силе
        print(f'Силач {name} поднял {i} шар')

    print(f'Силач {name} закончил соревнования.')


# Асинхронная функция для запуска турнира
async def start_tournament():
    # Создание задач для трех силачей с разными параметрами
    tasks = [
        start_strongman('Pasha', 3),
        start_strongman('Denis', 4),
        start_strongman('Apollon', 5)
    ]

    # Ожидание завершения всех задач
    await asyncio.gather(*tasks)


# Запуск турнира
asyncio.run(start_tournament())
