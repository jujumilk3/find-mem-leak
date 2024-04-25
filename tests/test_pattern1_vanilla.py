import psutil
import gc
from fastapi import status
from datetime import datetime
from time import sleep
from collections import defaultdict


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


def test_check_obj_sync_root_request_by_obj_count(client):
    # it increases forever. wtf
    ex_obj_count = 0
    while True:
        obj_count = len(gc.get_objects())
        if ex_obj_count > 0:
            print(f"obj_count: {obj_count}. obj_count dff: {obj_count - ex_obj_count}")
        ex_obj_count = obj_count
        response = client.get("/sync")
        assert response.status_code == status.HTTP_200_OK


def test_check_obj_sorted_by_type(client):
    call_api = True
    # if it is True, it will call api every second
    # then you can see the difference between objects
    # especially, dict, function, list, weakref.ReferenceType, cell, builtin_function_or_method
    ex_dict = {}
    ex_total = 0
    while True:
        if call_api:
            response = client.get("/sync")
            assert response.status_code == status.HTTP_200_OK
        found_result = gc.get_objects()
        by_dict = defaultdict(int)
        for item in found_result:
            by_dict[str(type(item))] += 1
        sorted_dict = {
            k: v for k, v in sorted(by_dict.items(), key=lambda x: x[1], reverse=True)
        }
        # print top 20
        index = 0
        for k, v in sorted_dict.items():
            print(k, v)
            if k in ex_dict:
                print("  -> diff: ", v - ex_dict[k])
            index += 1
            if index == 20:
                break
        print("total:", len(found_result))
        print("total_diff:", len(found_result) - ex_total)
        ex_dict = sorted_dict
        ex_total = len(found_result)
        print("===" * 10)
        sleep(1)


def test_check_mem_usage_sync_root_request_by_obj_objects(client):
    # it increases forever. wtf
    response = client.get("/sync")
    found_result = gc.get_objects()
    print(type(found_result))
    print(len(found_result))
    # print(gc.get_objects())
    with open("gc_objects.txt", "w") as f:
        for item in found_result:
            f.write(f"{item}\n")
    assert response.status_code == status.HTTP_200_OK


def test_check_mem_usage_without_any_api_call(client):
    # obj count never changes
    while True:
        print("obj count: ", len(gc.get_objects()))


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


def test_check_mem_usage_intended_leak(client):
    pid = psutil.Process()
    process = psutil.Process(pid.pid)
    index = 0
    while True:
        start_time = datetime.now()
        response = client.get(
            "/intended_mem_leak",
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
