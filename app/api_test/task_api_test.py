import requests
import json

BASE_URL = "http://127.0.0.1:8001/api/v1/tasks"

# ==========================
# 1️⃣ 提交前端任务
# ==========================
task_payload = {
    "userName": "muzi",
    "taskID": "task001",
    "taskType": "rbg_test",
    "data": {"param1": "value1", "param2": 123}
}

resp = requests.post(f"{BASE_URL}/frontend_rbg_task_submit", json=task_payload)
print("提交任务:", resp.status_code, resp.json())

# ==========================
# 2️⃣ 提交任务监听信息
# ==========================
listener_payload = {
    "taskID": "task001",
    "taskStatus": "处理中",
    "taskResult": {"progress": 50}
}

resp = requests.post(f"{BASE_URL}/task_listener", json=listener_payload)
print("提交监听:", resp.status_code, resp.json())

# ==========================
# 3️⃣ 查询某用户所有任务
# ==========================
resp = requests.get(f"{BASE_URL}/frontend_rbg_tasks_by_user/muzi")
print("查询用户任务:", resp.status_code, json.dumps(resp.json(), indent=2, ensure_ascii=False))

# ==========================
# 4️⃣ 查询某用户所有任务及状态信息
# ==========================
resp = requests.get(f"{BASE_URL}/frontend_rbg_tasks_full/muzi")
print("查询用户任务及状态:", resp.status_code, json.dumps(resp.json(), indent=2, ensure_ascii=False))

# ==========================
# 5️⃣ 再更新任务监听状态
# ==========================
listener_update_payload = {
    "taskID": "task001",
    "taskStatus": "完成",
    "taskResult": {"progress": 100, "result": "ok"}
}

resp = requests.post(f"{BASE_URL}/task_listener", json=listener_update_payload)
print("更新监听:", resp.status_code, resp.json())

# ==========================
# 6️⃣ 再查询任务及状态信息
# ==========================
resp = requests.get(f"{BASE_URL}/frontend_rbg_tasks_full/muzi")
print("查询更新后的任务及状态:", resp.status_code, json.dumps(resp.json(), indent=2, ensure_ascii=False))
import requests
import json


# ==========================
# 1️⃣ 提交前端任务
# ==========================
task_payload = {
    "userName": "muzi",
    "taskID": "task001",
    "taskType": "rbg_test",
    "data": {"param1": "value1", "param2": 123}
}

resp = requests.post(f"{BASE_URL}/frontend_rbg_task_submit", json=task_payload)
print("提交任务:", resp.status_code, resp.json())

# ==========================
# 2️⃣ 提交任务监听信息
# ==========================
listener_payload = {
    "taskID": "task001",
    "taskStatus": "处理中",
    "taskResult": {"progress": 50}
}

resp = requests.post(f"{BASE_URL}/task_listener", json=listener_payload)
print("提交监听:", resp.status_code, resp.json())

# ==========================
# 3️⃣ 查询某用户所有任务
# ==========================
resp = requests.get(f"{BASE_URL}/frontend_rbg_tasks_by_user/muzi")
print("查询用户任务:", resp.status_code, json.dumps(resp.json(), indent=2, ensure_ascii=False))

# ==========================
# 4️⃣ 查询某用户所有任务及状态信息
# ==========================
resp = requests.get(f"{BASE_URL}/frontend_rbg_tasks_full/muzi")
print("查询用户任务及状态:", resp.status_code, json.dumps(resp.json(), indent=2, ensure_ascii=False))

# ==========================
# 5️⃣ 再更新任务监听状态
# ==========================
listener_update_payload = {
    "taskID": "task001",
    "taskStatus": "完成",
    "taskResult": {"progress": 100, "result": "ok"}
}

resp = requests.post(f"{BASE_URL}/task_listener", json=listener_update_payload)
print("更新监听:", resp.status_code, resp.json())

# ==========================
# 6️⃣ 再查询任务及状态信息
# ==========================
resp = requests.get(f"{BASE_URL}/frontend_rbg_tasks_full/muzi")
print("查询更新后的任务及状态:", resp.status_code, json.dumps(resp.json(), indent=2, ensure_ascii=False))


'''
提交任务: 400 {'detail': '任务ID已存在'}
提交监听: 200 {'message': '任务监听更新成功', 'taskID': 'task001'}
查询用户任务: 200 {
  "userName": "muzi",
  "tasks": [
    {
      "taskID": "task001",
      "taskType": "rbg_test",
      "data": {
        "param1": "value1",
        "param2": 123
      },
      "dateTime": "2025-09-02 08:05:05"
    }
  ]
}
查询用户任务及状态: 200 {
  "userName": "muzi",
  "tasks": [
    {
      "taskID": "task001",
      "taskType": "rbg_test",
      "data": {
        "param1": "value1",
        "param2": 123
      },
      "dateTime": "2025-09-02 08:05:05",
      "taskStatus": "处理中",
      "taskResult": {
        "progress": 50
      }
    }
  ]
}
更新监听: 200 {'message': '任务监听更新成功', 'taskID': 'task001'}
查询更新后的任务及状态: 200 {
  "userName": "muzi",
  "tasks": [
    {
      "taskID": "task001",
      "taskType": "rbg_test",
      "data": {
        "param1": "value1",
        "param2": 123
      },
      "dateTime": "2025-09-02 08:05:05",
      "taskStatus": "完成",
      "taskResult": {
        "progress": 100,
        "result": "ok"
      }
    }
  ]
}
提交任务: 400 {'detail': '任务ID已存在'}
提交监听: 200 {'message': '任务监听更新成功', 'taskID': 'task001'}
查询用户任务: 200 {
  "userName": "muzi",
  "tasks": [
    {
      "taskID": "task001",
      "taskType": "rbg_test",
      "data": {
        "param1": "value1",
        "param2": 123
      },
      "dateTime": "2025-09-02 08:05:05"
    }
  ]
}
查询用户任务及状态: 200 {
  "userName": "muzi",
  "tasks": [
    {
      "taskID": "task001",
      "taskType": "rbg_test",
      "data": {
        "param1": "value1",
        "param2": 123
      },
      "dateTime": "2025-09-02 08:05:05",
      "taskStatus": "处理中",
      "taskResult": {
        "progress": 50
      }
    }
  ]
}
更新监听: 200 {'message': '任务监听更新成功', 'taskID': 'task001'}
查询更新后的任务及状态: 200 {
  "userName": "muzi",
  "tasks": [
    {
      "taskID": "task001",
      "taskType": "rbg_test",
      "data": {
        "param1": "value1",
        "param2": 123
      },
      "dateTime": "2025-09-02 08:05:05",
      "taskStatus": "完成",
      "taskResult": {
        "progress": 100,
        "result": "ok"
      }
    }
  ]
}'''