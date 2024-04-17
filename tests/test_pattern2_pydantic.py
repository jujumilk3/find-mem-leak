import psutil
from fastapi import status
from datetime import datetime


def test_check_mem_usage_async_pydantic(client):
    pid = psutil.Process()
    process = psutil.Process(pid.pid)
    index = 0
    while True:
        start_time = datetime.now()
        response = client.post(
            "/async/pydantic",
            json={
                "name": "name",
                "description": "description",
            },
        )
        assert response.status_code == status.HTTP_200_OK
        index += 1
        if index % 1000 == 0:
            end_time = datetime.now()
            takes_time = end_time - start_time
            mem_info = process.memory_info()
            print(
                f"Memory Usage: {round(mem_info.rss / (1024 * 1024), 2)} MB. index: {index}. takes_time: {takes_time}"
            )
