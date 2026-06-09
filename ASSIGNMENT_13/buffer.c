#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char *data;
    size_t length;
    size_t capacity;
} StringBuffer;

/* Initialize StringBuffer */
StringBuffer* sb_init(size_t initial_capacity) {

    StringBuffer *sb = (StringBuffer *)malloc(sizeof(StringBuffer));

    if (sb == NULL) {
        printf("Memory allocation failed for StringBuffer.\n");
        return NULL;
    }

    sb->data = (char *)malloc(initial_capacity * sizeof(char));

    if (sb->data == NULL) {
        printf("Memory allocation failed for data buffer.\n");
        free(sb);
        return NULL;
    }

    sb->length = 0;
    sb->capacity = initial_capacity;
    sb->data[0] = '\0';

    return sb;
}

/* Append string */
void sb_append(StringBuffer *sb, const char *str) {

    size_t str_len = strlen(str);

    /* Increase capacity if needed */
    while (sb->length + str_len + 1 > sb->capacity) {

        size_t new_capacity = sb->capacity * 2;

        char *temp = (char *)realloc(sb->data, new_capacity);

        if (temp == NULL) {
            printf("Reallocation failed.\n");
            return;
        }

        sb->data = temp;
        sb->capacity = new_capacity;

        printf("\n[Buffer Resized] New Capacity = %zu\n",
               sb->capacity);
    }

    strcat(sb->data, str);
    sb->length += str_len;
}

/* Free memory */
void sb_free(StringBuffer *sb) {

    if (sb != NULL) {
        free(sb->data);
        free(sb);
    }
}

int main() {

    size_t initial_capacity;
    int choice;

    char input[200];

    printf("=========================================\n");
    printf("      DYNAMIC STRING BUFFER IN C\n");
    printf("=========================================\n");

    printf("Enter initial buffer capacity: ");
    scanf("%zu", &initial_capacity);

    getchar(); /* remove newline */

    StringBuffer *sb = sb_init(initial_capacity);

    if (sb == NULL) {
        return 1;
    }

    do {

        printf("\n------------- MENU -------------\n");
        printf("1. Append String\n");
        printf("2. Display Current String\n");
        printf("3. Display Buffer Details\n");
        printf("4. Exit\n");
        printf("--------------------------------\n");

        printf("Enter your choice: ");
        scanf("%d", &choice);

        getchar(); /* remove newline */

        switch(choice) {

            case 1:

                printf("Enter string to append: ");
                fgets(input, sizeof(input), stdin);

                /* Remove newline */
                input[strcspn(input, "\n")] = '\0';

                sb_append(sb, input);

                printf("String appended successfully.\n");

                break;

            case 2:

                printf("\nCurrent String:\n");
                printf("%s\n", sb->data);

                break;

            case 3:

                printf("\nBuffer Details:\n");
                printf("Length   = %zu\n", sb->length);
                printf("Capacity = %zu\n", sb->capacity);

                break;

            case 4:

                printf("\nFreeing memory...\n");
                sb_free(sb);

                printf("Memory freed successfully.\n");
                printf("Program terminated.\n");

                break;

            default:

                printf("Invalid choice. Try again.\n");
        }

    } while(choice != 4);

    return 0;
}