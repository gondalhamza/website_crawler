import time
import unittest
from utils.resource_pool import ResourcePool


class ResourcePoolTests(unittest.TestCase):
    def test_spawn_worker(self):
        pool = ResourcePool(num_workers=1)
        worker_func = lambda: None

        pool.spawn_worker(worker_func)

        self.assertEqual(len(pool.active_workers), 1)


    def test_wait_for_free_worker(self):
        pool = ResourcePool(num_workers=1)
        worker_func = lambda: time.sleep(2)

        pool.spawn_worker(worker_func)
        pool.wait_for_free_worker()

        self.assertEqual(len(pool.active_workers), 0)



if __name__ == '__main__':
    unittest.main()
