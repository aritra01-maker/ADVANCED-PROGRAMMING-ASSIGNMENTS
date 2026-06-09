#include <stdio.h>
#include <time.h>
#include <math.h>

#define REPEAT 1000000

/* ---------- Algorithms ---------- */

int constant_time_algo(int a[], int index)
{
    return a[index];
}

int linear_Search_algo(int a[], int n, int key)
{
    for (int i = 0; i < n; i++)
        if (a[i] == key)
            return i;
    return -1;
}

int binary_Search_iterative(int a[], int n, int key)
{
    int l = 0, r = n - 1;
    while (l <= r)
    {
        int m = l + (r - l) / 2;
        if (a[m] == key)
            return m;
        else if (a[m] < key)
            l = m + 1;
        else
            r = m - 1;
    }
    return -1;
}

int binary_Search_recursive(int a[], int l, int r, int key)
{
    if (l > r)
        return -1;

    int m = l + (r - l) / 2;

    if (a[m] == key)
        return m;
    else if (a[m] < key)
        return binary_Search_recursive(a, m + 1, r, key);
    else
        return binary_Search_recursive(a, l, m - 1, key);
}

void selection_Sort_algo(int a[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        int min = i;
        for (int j = i + 1; j < n; j++)
            if (a[j] < a[min])
                min = j;
        int t = a[i];
        a[i] = a[min];
        a[min] = t;
    }
}

/* ---------- Space Estimation Functions ---------- */
/* These return auxiliary space per call in bytes */

size_t space_constant() { return sizeof(int); }           // index
size_t space_linear() { return sizeof(int) * 2; }         // i, key
size_t space_binary_iter() { return sizeof(int) * 3; }    // l, r, m
size_t space_binary_rec_one() { return sizeof(int) * 3; } // l, r, m per call
size_t space_selection() { return sizeof(int) * 4; }      // i, j, min, t

int main()
{
    int n, key;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    int a[n], b[n];
    printf("Enter %d elements:\n", n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
        b[i] = a[i];
    }

    printf("Enter element to search: ");
    scanf("%d", &key);

    /* -------- Timing -------- */

    clock_t s1 = clock();
    for (int i = 0; i < REPEAT; i++)
        linear_Search_algo(a, n, key);
    clock_t e1 = clock();

    clock_t s2 = clock();
    for (int i = 0; i < REPEAT; i++)
        selection_Sort_algo(b, n);
    clock_t e2 = clock();

    clock_t s3 = clock();
    for (int i = 0; i < REPEAT; i++)
        binary_Search_iterative(b, n, key);
    clock_t e3 = clock();

    clock_t s4 = clock();
    for (int i = 0; i < REPEAT; i++)
        binary_Search_recursive(b, 0, n - 1, key);
    clock_t e4 = clock();

    clock_t s5 = clock();
    for (int i = 0; i < REPEAT; i++)
        constant_time_algo(a, 0);
    clock_t e5 = clock();

    /* -------- Space Estimation -------- */

    int depth = (int)ceil(log2(n + 1)); // recursion depth ≈ log2 n

    size_t space_const_bytes = space_constant();
    size_t space_linear_bytes = space_linear();
    size_t space_binary_iter_bytes = space_binary_iter();
    size_t space_binary_rec_bytes = space_binary_rec_one() * depth;
    size_t space_selection_bytes = space_selection();

    /* -------- Output -------- */

    printf("\n========= TIME COMPLEXITY =========\n");
    printf("Linear Search (O(n))                 : %f seconds\n",
           (double)(e1 - s1) / CLOCKS_PER_SEC);
    printf("Selection Sort (O(n^2))             : %f seconds\n",
           (double)(e2 - s2) / CLOCKS_PER_SEC);
    printf("Binary Search Iterative (O(log n))  : %f seconds\n",
           (double)(e3 - s3) / CLOCKS_PER_SEC);
    printf("Binary Search Recursive (O(log n))  : %f seconds\n",
           (double)(e4 - s4) / CLOCKS_PER_SEC);
    printf("Constant Time (O(1))                : %f seconds\n",
           (double)(e5 - s5) / CLOCKS_PER_SEC);

    printf("\n========= SPACE COMPLEXITY =========\n");
    printf("Constant Access        : %zu bytes --> O(1)\n", space_const_bytes);
    printf("Linear Search          : %zu bytes --> O(1)\n", space_linear_bytes);
    printf("Binary Search Iterative: %zu bytes --> O(1)\n", space_binary_iter_bytes);
    printf("Binary Search Recursive: %zu bytes --> O(log n)  %d stack frames\n",
           space_binary_rec_bytes, depth);
    printf("Selection Sort         : %zu bytes --> O(1)\n", space_selection_bytes);

    return 0;
}
