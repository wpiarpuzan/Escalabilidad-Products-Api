from locust import HttpUser, task, between, events
import time, json

results = []

class ProductUser(HttpUser):
    wait_time = between(5.0, 10.0)

    @task
    def create_product(self):
        start = time.time()
        try:
            response = self.client.post("/products/create", json={
                "name": "Surgical Mask",
                "stock_quantity": 500,
                "price": 1200,
                "description": "Disposable 3-layer surgical mask for medical use"
            })
            status = "success" if response.status_code == 201 else "error"
        except:
            status = "error"
        end = time.time()
        duration = end - start
        results.append({"status": status, "duration": duration})

@events.quitting.add_listener
def save_results(environment, **kwargs):
    with open("metrics/results.json", "w") as f:
        json.dump(results, f)
