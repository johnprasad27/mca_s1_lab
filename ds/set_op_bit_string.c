#include <stdio.h>

int main() {
    int n, i, choice;
    int A[20], B[20], result[20];

    printf("Enter number of elements in universal set: ");
    scanf("%d", &n);

    printf("\nEnter bit string for Set A:\n");
    for(i = 0; i < n; i++)
        scanf("%d", &A[i]);

    printf("\nEnter bit string for Set B:\n");
    for(i = 0; i < n; i++)
        scanf("%d", &B[i]);

    do {
        printf("\n--- MENU ---\n");
        printf("1. Union (A ∪ B)\n");
        printf("2. Intersection (A ∩ B)\n");
        printf("3. Difference (A − B)\n");
        printf("4. Complement of A\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch(choice) {
            case 1:   // Union
                for(i = 0; i < n; i++)
                    result[i] = A[i] || B[i];

                printf("Union: ");
                for(i = 0; i < n; i++)
                    printf("%d ", result[i]);
                printf("\n");
                break;

            case 2:   // Intersection
                for(i = 0; i < n; i++)
                    result[i] = A[i] && B[i];

                printf("Intersection: ");
                for(i = 0; i < n; i++)
                    printf("%d ", result[i]);
                printf("\n");
                break;

            case 3:   // Difference A - B
                for(i = 0; i < n; i++)
                    result[i] = A[i] && !B[i];

                printf("Difference (A - B): ");
                for(i = 0; i < n; i++)
                    printf("%d ", result[i]);
                printf("\n");
                break;

            case 4:   // Complement of A
                for(i = 0; i < n; i++)
                    result[i] = !A[i];

                printf("Complement of A: ");
                for(i = 0; i < n; i++)
                    printf("%d ", result[i]);
                printf("\n");
                break;

            case 5:
                printf("Exiting program...\n");
                break;

            default:
                printf("Invalid choice!\n");
        }
    } while(choice != 5);

    return 0;
}
