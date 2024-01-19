#include "matrix.h"
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

// Include SSE intrinsics
#if defined(_MSC_VER)
#include <intrin.h>
#elif defined(__GNUC__) && (defined(__x86_64__) || defined(__i386__))
#include <immintrin.h>
#include <x86intrin.h>
#endif

/* Below are some intel intrinsics that might be useful
 * void _mm256_storeu_pd (double * mem_addr, __m256d a)
 * __m256d _mm256_set1_pd (double a)
 * __m256d _mm256_set_pd (double e3, double e2, double e1, double e0)
 * __m256d _mm256_loadu_pd (double const * mem_addr)
 * __m256d _mm256_add_pd (__m256d a, __m256d b)
 * __m256d _mm256_sub_pd (__m256d a, __m256d b)
 * __m256d _mm256_fmadd_pd (__m256d a, __m256d b, __m256d c)
 * __m256d _mm256_mul_pd (__m256d a, __m256d b)
 * __m256d _mm256_cmp_pd (__m256d a, __m256d b, const int imm8)
 * __m256d _mm256_and_pd (__m256d a, __m256d b)
 * __m256d _mm256_max_pd (__m256d a, __m256d b)
*/

/* Generates a random double between low and high */
double rand_double(double low, double high) {
    double range = (high - low);
    double div = RAND_MAX / range;
    return low + (rand() / div);
}

/* Generates a random matrix */
void rand_matrix(matrix *result, unsigned int seed, double low, double high) {
    srand(seed);
    for (int i = 0; i < result->rows; i++) {
        for (int j = 0; j < result->cols; j++) {
            set(result, i, j, rand_double(low, high));
        }
    }
}

/*
 * Allocates space for a matrix struct pointed to by the double pointer mat with
 * `rows` rows and `cols` columns. You should also allocate memory for the data array
 * and initialize all entries to be zeros. `parent` should be set to NULL to indicate that
 * this matrix is not a slice. You should also set `ref_cnt` to 1.
 * You should return -1 if either `rows` or `cols` or both have invalid values, or if any
 * call to allocate memory in this function fails. Return 0 upon success.
 */
int allocate_matrix(matrix **mat, int rows, int cols) {
    /* TODO: YOUR CODE HERE */
    if (rows <=0 || cols <= 0) {
        return -1;
    }

    matrix *m = malloc(sizeof(**mat));
    if (m == NULL) {
        return -2;
    }
    double *data = calloc(rows*cols, sizeof(*(m->data)));
    if (data == NULL) {
        return -2;
    }
    m->data = data;
    m->rows = rows;
    m->cols = cols;
    m->ref_cnt = 1;
    m->parent = NULL;
    *mat = m;
    return 0;
}

/*
 * Allocates space for a matrix struct pointed to by `mat` with `rows` rows and `cols` columns.
 * Its data should point to the `offset`th entry of `from`'s data (you do not need to allocate memory)
 * for the data field. `parent` should be set to `from` to indicate this matrix is a slice of `from`.
 * You should return -1 if either `rows` or `cols` or both are non-positive or if any
 * call to allocate memory in this function fails. Return 0 upon success.
 */
int allocate_matrix_ref(matrix **mat, matrix *from, int offset, int rows, int cols) {
    /* TODO: YOUR CODE HERE */
    if (rows <=0 || cols <= 0) {
        return -1;
    }

    matrix *m = malloc(sizeof(**mat));
    if (m == NULL) {
        return -2;
    }
    m->data = from->data + offset;
    m->rows = rows;
    m->cols = cols;
    m->parent = from;
    m->ref_cnt = 1;
    from->ref_cnt += 1;
    *mat = m;
    return 0;
}

/*
 * You need to make sure that you only free `mat->data` if `mat` is not a slice and has no existing slices,
 * or if `mat` is the last existing slice of its parent matrix and its parent matrix has no other references
 * (including itself). You cannot assume that mat is not NULL.
 */
void deallocate_matrix(matrix *mat) {
    /* TODO: YOUR CODE HERE */
    if (mat == NULL) {
        return;
    }

    if (mat->parent == NULL) {
        mat->ref_cnt -= 1;
        if (mat->ref_cnt == 0) {
            free(mat->data);
            free(mat);
        }
    } else {
        deallocate_matrix(mat->parent);
        free(mat);
    }
}

/*
 * Returns the double value of the matrix at the given row and column.
 * You may assume `row` and `col` are valid.
 */
double get(matrix *mat, int row, int col) {
    /* TODO: YOUR CODE HERE */
    return mat->data[row * mat->cols + col];
}

/*
 * Sets the value at the given row and column to val. You may assume `row` and
 * `col` are valid
 */
void set(matrix *mat, int row, int col, double val) {
    /* TODO: YOUR CODE HERE */
    mat->data[row * mat->cols + col] = val;
}

/*
 * Sets all entries in mat to val
 */
void fill_matrix(matrix *mat, double val) {
    /* TODO: YOUR CODE HERE */
    int elems = mat->rows * mat->cols;

	__m256d _val = _mm256_set1_pd(val);		// set vector to val

    #pragma omp parallel for
    for (int i = 0; i < elems / 4 * 4; i+=4) {
        _mm256_storeu_pd(mat->data + i, _val);
    }

    // tailcase
    #pragma omp parallel for
    for (int i = elems / 4 * 4; i < elems; i++) {
        mat->data[i] = val;
    }
}

/*
 * Store the result of adding mat1 and mat2 to `result`.
 * Return 0 upon success and a nonzero value upon failure.
 */
int add_matrix(matrix *result, matrix *mat1, matrix *mat2) {
    /* TODO: YOUR CODE HERE */
    int elems = mat1->rows * mat1->cols;

    #pragma omp parallel for
    for (int i = 0; i < elems / 4 * 4; i+= 4) {
        __m256d sum =_mm256_add_pd(_mm256_loadu_pd(mat1->data + i), _mm256_loadu_pd(mat2->data + i));
        _mm256_storeu_pd(result->data + i, sum);
    }

    // tailcase
    #pragma omp parallel for
    for (int i = elems / 4 * 4; i < elems; i++) {
        result->data[i] = mat1->data[i] + mat2->data[i];
    }
    return 0;
}

/*
 * Store the result of subtracting mat2 from mat1 to `result`.
 * Return 0 upon success and a nonzero value upon failure.
 */
int sub_matrix(matrix *result, matrix *mat1, matrix *mat2) {
    /* TODO: YOUR CODE HERE */
    int elems = mat1->rows * mat1->cols;

    #pragma omp parallel for
    for (int i = 0; i < elems / 4 * 4; i+= 4) {
        __m256d sum =_mm256_sub_pd(_mm256_loadu_pd(mat1->data + i), _mm256_loadu_pd(mat2->data + i));
        _mm256_storeu_pd(result->data + i, sum);
    }

    // tailcase
    #pragma omp parallel for
    for (int i = elems / 4 * 4; i < elems; i++) {
        result->data[i] = mat1->data[i] - mat2->data[i];
    }
    return 0;
}

/*
 * Store the result of multiplying mat1 and mat2 to `result`.
 * Return 0 upon success and a nonzero value upon failure.
 * Remember that matrix multiplication is not the same as multiplying individual elements.
 */
int mul_matrix(matrix *result, matrix *mat1, matrix *mat2) {
    /* TODO: YOUR CODE HERE */
    int mat1rows = mat1->rows;
    int mat1cols = mat1->cols;
    int mat2cols = mat2->cols;

    #pragma omp parallel for
    for (int i = 0; i < mat1rows; i++) {
        for (int j = 0; j < mat2cols; j++) {
            result->data[i+j*mat2cols]= 0.0;
            for (int k = 0; k < mat1cols; k++) {
                result->data[i+j*mat2cols] += mat1->data[i+k*mat1rows] * mat2->data[k+j*mat1cols];
            }
        }
    }
    return 0;
}

/*
 * Store the result of raising mat to the (pow)th power to `result`.
 * Return 0 upon success and a nonzero value upon failure.
 * Remember that pow is defined with matrix multiplication, not element-wise multiplication.
 */
int pow_matrix(matrix *result, matrix *mat, int pow) {
    /* TODO: YOUR CODE HERE */
    int rows = mat->rows;
    int cols = mat->cols;

    matrix *temp = NULL;
    matrix *matSq = NULL;
    allocate_matrix(&temp, rows, cols);
    allocate_matrix(&matSq, rows, cols);

    if (rows !=  cols) return -1;
    fill_matrix(result, 0.0);

    #pragma omp parallel for
    for (int i = 0; i < rows; i++) {
        result->data[i*rows + i] = 1.0;
    }

    memcpy(matSq->data, mat->data, rows*cols*sizeof(double));
    while (pow) {
        if (pow % 2) { // odd power 
            mul_matrix(temp, matSq, result);
            memcpy(result->data, temp->data, rows*cols*sizeof(double));
            pow -= 1;
        } else {
            mul_matrix(temp, matSq, matSq);
            memcpy(matSq->data, temp->data, rows*cols*sizeof(double));
            pow /= 2;
        }
    }

    deallocate_matrix(temp);
    deallocate_matrix(matSq);
    return 0;
}

/*
 * Store the result of element-wise negating mat's entries to `result`.
 * Return 0 upon success and a nonzero value upon failure.
 */
int neg_matrix(matrix *result, matrix *mat) {
    /* TODO: YOUR CODE HERE */
    int elems = mat->rows * mat->cols;

    __m256d _neg = _mm256_set1_pd(-1.0);
    #pragma omp parallel for
    for (int i = 0; i < elems / 4 * 4; i+= 4) {
        __m256d matVector = _mm256_loadu_pd(mat->data + i);
        _mm256_storeu_pd(result->data + i, _mm256_mul_pd(matVector, _neg));
    }

    // tailcase
    #pragma omp parallel for
    for (int i = elems / 4 * 4; i < elems; i++) {
        result->data[i] = -mat->data[i];
    }
    return 0;
}

/*
 * Store the result of taking the absolute value element-wise to `result`.
 * Return 0 upon success and a nonzero value upon failure.
 */
int abs_matrix(matrix *result, matrix *mat) {
    /* TODO: YOUR CODE HERE */
    int elems = mat->rows * mat->cols;

    __m256d _neg = _mm256_set1_pd(-1.0);
    #pragma omp parallel for
    for (int i = 0; i < elems / 4 * 4; i+= 4) {
        __m256d matVector = _mm256_loadu_pd(mat->data + i);
        _mm256_storeu_pd(result->data + i, _mm256_max_pd(matVector, _mm256_mul_pd(matVector, _neg)));
    }

    // tailcase
    #pragma omp parallel for
    for (int i = elems / 4 * 4; i < elems; i++) {
        result->data[i] = fabs(mat->data[i]);
    }
    return 0;

}