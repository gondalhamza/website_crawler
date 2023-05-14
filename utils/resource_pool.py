import gevent
import logging


class ResourcePool:
    def __init__(self, num_workers, max_waiting_time=30):
        self.num_workers = num_workers
        self.active_workers = set()
        self.max_waiting_time = max_waiting_time

    def spawn_worker(self, worker_func, *args, **kwargs):
        if len(self.active_workers) >= self.num_workers:
            self.wait_for_free_worker()

        worker = gevent.spawn(worker_func, *args, **kwargs)
        self.active_workers.add(worker)  # Add the worker to the set of active workers
        worker.link(self.worker_completed)
        logging.info(f"Worker spawned: {worker}")


    def wait_for_free_worker(self):
        logging.info("Waiting for free worker...")
        gevent.wait(self.active_workers, count=len(self.active_workers) - self.num_workers + 1, timeout=self.max_waiting_time)
        logging.info("Free worker available or timeout reached")

    def worker_completed(self, worker):
        self.active_workers.remove(worker)
        logging.info(f"Worker completed: {worker}")
