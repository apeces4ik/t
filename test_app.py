def test_metrics_route(client):
    # Сброс счётчика перед тестом (если нужно)
    client.get('/metrics')  # Сбросить счётчик, если это предусмотрено логикой приложения
    
    # Делаем 5 запросов к /time
    for _ in range(5):
        client.get('/time')
    
    # Проверяем /metrics
    response = client.get('/metrics')
    assert response.status_code == 200
    assert response.json['count'] == 5  # Ожидаем 5 запросов
