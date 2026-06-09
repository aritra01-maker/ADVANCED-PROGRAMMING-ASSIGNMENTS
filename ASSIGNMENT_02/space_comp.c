#include <stdio.h>
#include <stdlib.h>

/* --------------------------------------------
   CONSTANT SPACE ALGORITHM  -> O(1)
   Find maximum element in an array, no extra space is used.
-------------------------------------------- */
int constantSpaceMax(int arr[], int n, size_t *auxMem)
{
    int max = arr[0];

    *auxMem = 0; // no auxiliary memory

    for (int i = 1; i < n; i++)
        if (arr[i] > max)
            max = arr[i];

    return max;
}

/* --------------------------------------------
   LINEAR SPACE ALGORITHM  -> O(n)
   Reverse array using extra array, that extra array is the auxiliary space used.
-------------------------------------------- */
void linearSpaceReverse(int arr[], int n, size_t *auxMem)
{
    int *rev = (int *)malloc(n * sizeof(int));
    if (!rev)
        return;

    *auxMem = n * sizeof(int); // auxiliary array

    for (int i = 0; i < n; i++)
        rev[i] = arr[n - i - 1];

    free(rev);
}

/* --------------------------------------------
   QUADRATIC SPACE ALGORITHM  -> O(n^2)
   Graph adjacency matrix.The matrix itself is the auxiliary space used,
    which grows quadratically with n.
-------------------------------------------- */
void quadraticSpaceGraph(int n, size_t *auxMem)
{
    int **adj = (int **)malloc(n * sizeof(int *));
    if (!adj)
        return;

    for (int i = 0; i < n; i++)
        adj[i] = (int *)malloc(n * sizeof(int));

    *auxMem = (n * sizeof(int *)) + (n * n * sizeof(int));

    /* Initialize matrix */
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            adj[i][j] = (i == j) ? 0 : 1;

    for (int i = 0; i < n; i++)
        free(adj[i]);
    free(adj);
}

int main()
{
    int n;
    size_t auxMem;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    int *arr = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++)
        arr[i] = i + 1;

    /* ---------- CONSTANT SPACE ---------- */
    printf("\n===== CONSTANT SPACE =====\n");
    printf("Maximum Element: %d\n",
           constantSpaceMax(arr, n, &auxMem));
    printf("Auxiliary Memory Used: %zu bytes\n", auxMem);
    printf("Space Complexity: O(1)\n");

    /* ---------- LINEAR SPACE ---------- */
    printf("\n===== LINEAR SPACE =====\n");
    linearSpaceReverse(arr, n, &auxMem);
    printf("Auxiliary Memory Used: %zu bytes\n", auxMem);
    printf("Space Complexity: O(n)\n");

    /* ---------- QUADRATIC SPACE ---------- */
    printf("\n===== QUADRATIC SPACE =====\n");
    quadraticSpaceGraph(n, &auxMem);
    printf("Auxiliary Memory Used: %zu bytes\n", auxMem);
    printf("Space Complexity: O(n^2)\n");

    free(arr);
    return 0;
}
