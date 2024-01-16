"""
Feel free to add more test classes and/or tests that are not provided by the skeleton code!
Make sure you follow these naming conventions: https://docs.pytest.org/en/reorganize-docs/goodpractices.html#test-discovery
for your new tests/classes/python files or else they might be skipped.
"""
from utils import *
import time
import operator

"""
- We will test you on your performance on add, sub, abs, neg, mul, and pow, so make sure to test these
yourself! We will also test your implementation on matrices on different sizes. It is normal if
your smaller matrices are about the same speed as the naive implementation or even slower.
- Use time.time(), NOT time.perf_counter() to time your program!
- DO NOT count the time for initializing matrices into your performance time. Only count the
time the part where operations are carried out.
- Please also check for correctness while testing for performance!
- We provide the structure for test_small_add. All other tests should have similar structures
"""
class TestAddPerformance:
    def test_small_add(self):
        # Initialize matrices using rand_dp_nc_matrix
        # TODO: YOUR CODE HERE
        dc_mat1, nc_mat1 = rand_dc_nc_matrix(2, 2, seed=0)
        dc_mat2, nc_mat2 = rand_dc_nc_matrix(2, 2, seed=1)

        nc_start = time.time()
        # Carry out numc matrix operations
        # TODO: YOUR CODE HERE
        nc_out = nc_mat1 + nc_mat2
        nc_end = time.time()

        dc_start = time.time()
        # Carry out dumbpy matrix operations
        # TODO: YOUR CODE HERE
        dc_out = dc_mat1 + dc_mat2
        dc_end = time.time()

        # Check for correctness using cmp_dp_nc_matrix and calculate speedup
        # TODO: YOUR CODE HERE
        is_correct = cmp_dc_nc_matrix(dc_out, nc_out)
        self.assertTrue(is_correct)
        speedup = (dc_end - dc_start) / (nc_end - nc_start)
        print("Speedup: ", speedup)

    def test_medium_add(self):
        # TODO: YOUR CODE HERE
        dc_mat1, nc_mat1 = rand_dc_nc_matrix(512, 512, seed=0)
        dc_mat2, nc_mat2 = rand_dc_nc_matrix(512, 512, seed=1)

        nc_start = time.time()
        # Carry out numc matrix operations
        # TODO: YOUR CODE HERE
        nc_out = nc_mat1 + nc_mat2
        nc_end = time.time()

        dc_start = time.time()
        # Carry out dumbpy matrix operations
        # TODO: YOUR CODE HERE
        dc_out = dc_mat1 + dc_mat2
        dc_end = time.time()

        # Check for correctness using cmp_dp_nc_matrix and calculate speedup
        # TODO: YOUR CODE HERE
        is_correct = cmp_dc_nc_matrix(dc_out, nc_out)
        self.assertTrue(is_correct)
        speedup = (dc_end - dc_start) / (nc_end - nc_start)
        print("Speedup: ", speedup)

    def test_large_add(self):
        # TODO: YOUR CODE HERE
        dc_mat1, nc_mat1 = rand_dc_nc_matrix(4196, 4196, seed=0)
        dc_mat2, nc_mat2 = rand_dc_nc_matrix(4196, 4196, seed=1)

        nc_start = time.time()
        # Carry out numc matrix operations
        # TODO: YOUR CODE HERE
        nc_out = nc_mat1 + nc_mat2
        nc_end = time.time()

        dc_start = time.time()
        # Carry out dumbpy matrix operations
        # TODO: YOUR CODE HERE
        dc_out = dc_mat1 + dc_mat2
        dc_end = time.time()

        # Check for correctness using cmp_dp_nc_matrix and calculate speedup
        # TODO: YOUR CODE HERE
        is_correct = cmp_dc_nc_matrix(dc_out, nc_out)
        self.assertTrue(is_correct)
        speedup = (dc_end - dc_start) / (nc_end - nc_start)
        print("Speedup: ", speedup)

class TestSubPerformance:
    def test_small_sub(self):
        # TODO: YOUR CODE HERE
        dc_mat1, nc_mat1 = rand_dc_nc_matrix(2, 2, seed=0)
        dc_mat2, nc_mat2 = rand_dc_nc_matrix(2, 2, seed=1)

        nc_start = time.time()
        # Carry out numc matrix operations
        # TODO: YOUR CODE HERE
        nc_out = nc_mat1 - nc_mat2
        nc_end = time.time()

        dc_start = time.time()
        # Carry out dumbpy matrix operations
        # TODO: YOUR CODE HERE
        dc_out = dc_mat1 - dc_mat2
        dc_end = time.time()

        # Check for correctness using cmp_dp_nc_matrix and calculate speedup
        # TODO: YOUR CODE HERE
        is_correct = cmp_dc_nc_matrix(dc_out, nc_out)
        self.assertTrue(is_correct)
        speedup = (dc_end - dc_start) / (nc_end - nc_start)
        print("Speedup: ", speedup)

    def test_medium_sub(self):
        # TODO: YOUR CODE HERE
        dc_mat1, nc_mat1 = rand_dc_nc_matrix(512, 512, seed=0)
        dc_mat2, nc_mat2 = rand_dc_nc_matrix(512, 512, seed=1)

        nc_start = time.time()
        # Carry out numc matrix operations
        # TODO: YOUR CODE HERE
        nc_out = nc_mat1 - nc_mat2
        nc_end = time.time()

        dc_start = time.time()
        # Carry out dumbpy matrix operations
        # TODO: YOUR CODE HERE
        dc_out = dc_mat1 - dc_mat2
        dc_end = time.time()

        # Check for correctness using cmp_dp_nc_matrix and calculate speedup
        # TODO: YOUR CODE HERE
        is_correct = cmp_dc_nc_matrix(dc_out, nc_out)
        self.assertTrue(is_correct)
        speedup = (dc_end - dc_start) / (nc_end - nc_start)
        print("Speedup: ", speedup)

    def test_large_sub(self):
        # TODO: YOUR CODE HERE
        dc_mat1, nc_mat1 = rand_dc_nc_matrix(4196, 4196, seed=0)
        dc_mat2, nc_mat2 = rand_dc_nc_matrix(4196, 4196, seed=1)

        nc_start = time.time()
        # Carry out numc matrix operations
        # TODO: YOUR CODE HERE
        nc_out = nc_mat1 - nc_mat2
        nc_end = time.time()

        dc_start = time.time()
        # Carry out dumbpy matrix operations
        # TODO: YOUR CODE HERE
        dc_out = dc_mat1 - dc_mat2
        dc_end = time.time()

        # Check for correctness using cmp_dp_nc_matrix and calculate speedup
        # TODO: YOUR CODE HERE
        is_correct = cmp_dc_nc_matrix(dc_out, nc_out)
        self.assertTrue(is_correct)
        speedup = (dc_end - dc_start) / (nc_end - nc_start)
        print("Speedup: ", speedup)

class TestAbsPerformance:
    def test_small_abs(self):
        # TODO: YOUR CODE HERE
        dc_mat1, nc_mat1 = rand_dc_nc_matrix(2, 2, seed=0)

        nc_start = time.time()
        # Carry out numc matrix operations
        # TODO: YOUR CODE HERE
        nc_out = operator.abs(nc_mat1)
        nc_end = time.time()

        dc_start = time.time()
        # Carry out dumbpy matrix operations
        # TODO: YOUR CODE HERE
        dc_out = operator.abs(dc_mat1)
        dc_end = time.time()

        # Check for correctness using cmp_dp_nc_matrix and calculate speedup
        # TODO: YOUR CODE HERE
        is_correct = cmp_dc_nc_matrix(dc_out, nc_out)
        self.assertTrue(is_correct)
        speedup = (dc_end - dc_start) / (nc_end - nc_start)
        print("Speedup: ", speedup)

    def test_medium_abs(self):
        # TODO: YOUR CODE HERE
        dc_mat1, nc_mat1 = rand_dc_nc_matrix(512, 512, seed=0)

        nc_start = time.time()
        # Carry out numc matrix operations
        # TODO: YOUR CODE HERE
        nc_out = operator.abs(nc_mat1)
        nc_end = time.time()

        dc_start = time.time()
        # Carry out dumbpy matrix operations
        # TODO: YOUR CODE HERE
        dc_out = operator.abs(dc_mat1)
        dc_end = time.time()

        # Check for correctness using cmp_dp_nc_matrix and calculate speedup
        # TODO: YOUR CODE HERE
        is_correct = cmp_dc_nc_matrix(dc_out, nc_out)
        self.assertTrue(is_correct)
        speedup = (dc_end - dc_start) / (nc_end - nc_start)
        print("Speedup: ", speedup)

    def test_large_abs(self):
        # TODO: YOUR CODE HERE
        dc_mat1, nc_mat1 = rand_dc_nc_matrix(4196, 4196, seed=0)

        nc_start = time.time()
        # Carry out numc matrix operations
        # TODO: YOUR CODE HERE
        nc_out = operator.abs(nc_mat1)
        nc_end = time.time()

        dc_start = time.time()
        # Carry out dumbpy matrix operations
        # TODO: YOUR CODE HERE
        dc_out = operator.abs(dc_mat1)
        dc_end = time.time()

        # Check for correctness using cmp_dp_nc_matrix and calculate speedup
        # TODO: YOUR CODE HERE
        is_correct = cmp_dc_nc_matrix(dc_out, nc_out)
        self.assertTrue(is_correct)
        speedup = (dc_end - dc_start) / (nc_end - nc_start)
        print("Speedup: ", speedup)

class TestNegPerformance:
    def test_small_neg(self):
        # TODO: YOUR CODE HERE
        dc_mat1, nc_mat1 = rand_dc_nc_matrix(2, 2, seed=0)

        nc_start = time.time()
        # Carry out numc matrix operations
        # TODO: YOUR CODE HERE
        nc_out = operator.neg(nc_mat1)
        nc_end = time.time()

        dc_start = time.time()
        # Carry out dumbpy matrix operations
        # TODO: YOUR CODE HERE
        dc_out = operator.neg(dc_mat1)
        dc_end = time.time()

        # Check for correctness using cmp_dp_nc_matrix and calculate speedup
        # TODO: YOUR CODE HERE
        is_correct = cmp_dc_nc_matrix(dc_out, nc_out)
        self.assertTrue(is_correct)
        speedup = (dc_end - dc_start) / (nc_end - nc_start)
        print("Speedup: ", speedup)

    def test_medium_neg(self):
        # TODO: YOUR CODE HERE
        # TODO: YOUR CODE HERE
        dc_mat1, nc_mat1 = rand_dc_nc_matrix(512, 512, seed=0)

        nc_start = time.time()
        # Carry out numc matrix operations
        # TODO: YOUR CODE HERE
        nc_out = operator.neg(nc_mat1)
        nc_end = time.time()

        dc_start = time.time()
        # Carry out dumbpy matrix operations
        # TODO: YOUR CODE HERE
        dc_out = operator.neg(dc_mat1)
        dc_end = time.time()

        # Check for correctness using cmp_dp_nc_matrix and calculate speedup
        # TODO: YOUR CODE HERE
        is_correct = cmp_dc_nc_matrix(dc_out, nc_out)
        self.assertTrue(is_correct)
        speedup = (dc_end - dc_start) / (nc_end - nc_start)
        print("Speedup: ", speedup)

    def test_large_neg(self):
        # TODO: YOUR CODE HERE
        # TODO: YOUR CODE HERE
        dc_mat1, nc_mat1 = rand_dc_nc_matrix(4196, 4196, seed=0)

        nc_start = time.time()
        # Carry out numc matrix operations
        # TODO: YOUR CODE HERE
        nc_out = operator.neg(nc_mat1)
        nc_end = time.time()

        dc_start = time.time()
        # Carry out dumbpy matrix operations
        # TODO: YOUR CODE HERE
        dc_out = operator.neg(dc_mat1)
        dc_end = time.time()

        # Check for correctness using cmp_dp_nc_matrix and calculate speedup
        # TODO: YOUR CODE HERE
        is_correct = cmp_dc_nc_matrix(dc_out, nc_out)
        self.assertTrue(is_correct)
        speedup = (dc_end - dc_start) / (nc_end - nc_start)
        print("Speedup: ", speedup)

class TestMulPerformance:
    def test_small_mul(self):
        # TODO: YOUR CODE HERE
        dc_mat1, nc_mat1 = rand_dc_nc_matrix(2, 2, seed=0)
        dc_mat2, nc_mat2 = rand_dc_nc_matrix(2, 2, seed=1)

        nc_start = time.time()
        # Carry out numc matrix operations
        # TODO: YOUR CODE HERE
        nc_out = nc_mat1 * nc_mat2
        nc_end = time.time()

        dc_start = time.time()
        # Carry out dumbpy matrix operations
        # TODO: YOUR CODE HERE
        dc_out = dc_mat1 * dc_mat2
        dc_end = time.time()

        # Check for correctness using cmp_dp_nc_matrix and calculate speedup
        # TODO: YOUR CODE HERE
        is_correct = cmp_dc_nc_matrix(dc_out, nc_out)
        self.assertTrue(is_correct)
        speedup = (dc_end - dc_start) / (nc_end - nc_start)
        print("Speedup: ", speedup)

    def test_medium_mul(self):
        # TODO: YOUR CODE HERE
        dc_mat1, nc_mat1 = rand_dc_nc_matrix(512, 512, seed=0)
        dc_mat2, nc_mat2 = rand_dc_nc_matrix(512, 512, seed=1)

        nc_start = time.time()
        # Carry out numc matrix operations
        # TODO: YOUR CODE HERE
        nc_out = nc_mat1 * nc_mat2
        nc_end = time.time()

        dc_start = time.time()
        # Carry out dumbpy matrix operations
        # TODO: YOUR CODE HERE
        dc_out = dc_mat1 * dc_mat2
        dc_end = time.time()

        # Check for correctness using cmp_dp_nc_matrix and calculate speedup
        # TODO: YOUR CODE HERE
        is_correct = cmp_dc_nc_matrix(dc_out, nc_out)
        self.assertTrue(is_correct)
        speedup = (dc_end - dc_start) / (nc_end - nc_start)
        print("Speedup: ", speedup)

    def test_large_mul(self):
        # TODO: YOUR CODE HERE
        dc_mat1, nc_mat1 = rand_dc_nc_matrix(4196, 4196, seed=0)
        dc_mat2, nc_mat2 = rand_dc_nc_matrix(4196, 4196, seed=1)

        nc_start = time.time()
        # Carry out numc matrix operations
        # TODO: YOUR CODE HERE
        nc_out = nc_mat1 * nc_mat2
        nc_end = time.time()

        dc_start = time.time()
        # Carry out dumbpy matrix operations
        # TODO: YOUR CODE HERE
        dc_out = dc_mat1 * dc_mat2
        dc_end = time.time()

        # Check for correctness using cmp_dp_nc_matrix and calculate speedup
        # TODO: YOUR CODE HERE
        is_correct = cmp_dc_nc_matrix(dc_out, nc_out)
        self.assertTrue(is_correct)
        speedup = (dc_end - dc_start) / (nc_end - nc_start)
        print("Speedup: ", speedup)

class TestPowPerformance:
    def test_small_pow(self):
        # TODO: YOUR CODE HERE
        dc_mat1, nc_mat1 = rand_dc_nc_matrix(2, 2, seed=0)
        dc_mat2, nc_mat2 = rand_dc_nc_matrix(2, 2, seed=1)

        nc_start = time.time()
        # Carry out numc matrix operations
        # TODO: YOUR CODE HERE
        nc_out = nc_mat1 ** nc_mat2
        nc_end = time.time()

        dc_start = time.time()
        # Carry out dumbpy matrix operations
        # TODO: YOUR CODE HERE
        dc_out = dc_mat1 ** dc_mat2
        dc_end = time.time()

        # Check for correctness using cmp_dp_nc_matrix and calculate speedup
        # TODO: YOUR CODE HERE
        is_correct = cmp_dc_nc_matrix(dc_out, nc_out)
        self.assertTrue(is_correct)
        speedup = (dc_end - dc_start) / (nc_end - nc_start)
        print("Speedup: ", speedup)

    def test_medium_pow(self):
        # TODO: YOUR CODE HERE
        dc_mat1, nc_mat1 = rand_dc_nc_matrix(512, 512, seed=0)
        dc_mat2, nc_mat2 = rand_dc_nc_matrix(512, 512, seed=1)

        nc_start = time.time()
        # Carry out numc matrix operations
        # TODO: YOUR CODE HERE
        nc_out = nc_mat1 ** nc_mat2
        nc_end = time.time()

        dc_start = time.time()
        # Carry out dumbpy matrix operations
        # TODO: YOUR CODE HERE
        dc_out = dc_mat1 ** dc_mat2
        dc_end = time.time()

        # Check for correctness using cmp_dp_nc_matrix and calculate speedup
        # TODO: YOUR CODE HERE
        is_correct = cmp_dc_nc_matrix(dc_out, nc_out)
        self.assertTrue(is_correct)
        speedup = (dc_end - dc_start) / (nc_end - nc_start)
        print("Speedup: ", speedup)

    def test_large_pow(self):
        # TODO: YOUR CODE HERE
        dc_mat1, nc_mat1 = rand_dc_nc_matrix(4196, 4196, seed=0)
        dc_mat2, nc_mat2 = rand_dc_nc_matrix(4196, 4196, seed=1)

        nc_start = time.time()
        # Carry out numc matrix operations
        # TODO: YOUR CODE HERE
        nc_out = nc_mat1 ** nc_mat2
        nc_end = time.time()

        dc_start = time.time()
        # Carry out dumbpy matrix operations
        # TODO: YOUR CODE HERE
        dc_out = dc_mat1 ** dc_mat2
        dc_end = time.time()

        # Check for correctness using cmp_dp_nc_matrix and calculate speedup
        # TODO: YOUR CODE HERE
        is_correct = cmp_dc_nc_matrix(dc_out, nc_out)
        self.assertTrue(is_correct)
        speedup = (dc_end - dc_start) / (nc_end - nc_start)
        print("Speedup: ", speedup)