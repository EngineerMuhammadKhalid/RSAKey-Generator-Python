import unittest
import subprocess
import time
import os

class TestRSAKeyGeneration(unittest.TestCase):
    def test_generate_2000_keys(self):
        self.run_test(2000)

    def test_generate_4000_keys(self):
        self.run_test(4000)

    def test_generate_8000_keys(self):
        self.run_test(8000)

    def run_test(self, num_keys):
        script_path = "C:/Users/softe/OneDrive/Desktop/final/1/task.py"  # Update with the correct path
        start_time = time.time()

        try:
            subprocess.check_output(["python", script_path, str(num_keys)], stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            self.fail(f"Failed to run the script. Error: {e.output.decode('utf-8')}")

        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f"Time taken to generate {num_keys} keys: {elapsed_time} seconds")

        # Optionally, you can include assertions based on the elapsed time.

    def test_generate_1000000_keys(self):
        # Extrapolate time based on the trend observed in previous tests
        extrapolated_time = self.extrapolate_time()

        print(f"Extrapolated time to generate 1,000,000 keys: {extrapolated_time} seconds")

        # Optionally, you can include assertions based on the extrapolation.

    def extrapolate_time(self):
        # Implement your extrapolation logic here based on the trend observed in previous tests
        # This can be a simple linear extrapolation or more sophisticated analysis

        return estimated_time

if __name__ == "__main__":
    unittest.main()
