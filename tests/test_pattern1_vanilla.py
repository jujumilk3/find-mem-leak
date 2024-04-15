import psutil
from fastapi import status
from datetime import datetime


def test_one_plus_one():
    assert 1 + 1 == 2


def test_hello_world():
    assert True


def test_openapi_doc(client):
    response = client.get(
        "/docs",
    )
    assert response.status_code == status.HTTP_200_OK


def test_check_mem_usage():
    pid = psutil.Process()

    # get process by using pid
    process = psutil.Process(pid.pid)

    # get memory info
    for _ in range(10):
        mem_info = process.memory_info()
        print(f"Memory Usage: {mem_info.rss / (1024 * 1024)} MB")
        psutil.time.sleep(1)


def test_check_mem_usage_sync_root_request(client):
    pid = psutil.Process()
    process = psutil.Process(pid.pid)
    index = 0
    while True:
        start_time = datetime.now()
        response = client.get(
            "/sync",
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


def test_check_mem_usage_async_root_request(client):
    pid = psutil.Process()
    process = psutil.Process(pid.pid)
    index = 0
    while True:
        start_time = datetime.now()
        response = client.get(
            "/async",
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
