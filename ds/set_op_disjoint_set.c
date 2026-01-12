#include <stdio.h>

int parent[20];
int n;

/* ---------- FIND OPERATION ---------- */
int find(int x) {
    if (parent[x] == x)
        return x;
    return find(parent[x]);
}

/* ---------- UNION OPERATION ---------- */
void unionSet(int x, int y) {
    int px = find(x);
    int py = find(y);

    if (px != py) {
        parent[py] = px;
        printf("Union of %d and %d done.\n", x, y);
    } else {
        printf("Elements %d and %d are already in the same set.\n", x, y);
    }
}

/* ---------- DISPLAY PARENT ARRAY ---------- */
void displayParentArray() {
    printf("\nElement : Parent\n");
    for (int i = 0; i < n; i++) {
        printf("   %d    :   %d\n", i, parent[i]);
    }
}

/* ---------- DISPLAY JOINED SETS CLEARLY ---------- */
void displayJoinedSets() {
    int printed[20] = {0};

    printf("\nDisjoint Sets:\n");

    for (int i = 0; i < n; i++) {
        int root = find(i);

        if (!printed[root]) {
            printed[root] = 1;
            printf("{ ");

            for (int j = 0; j < n; j++) {
                if (find(j) == root)
                    printf("%d ", j);
            }

            printf("}\n");
        }
    }
}

/* ---------- MAIN FUNCTION ---------- */
int main() {
    int choice, x, y;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    /* Make-Set */
    for (int i = 0; i < n; i++)
        parent[i] = i;

    do {
        printf("\n--- MENU ---\n");
        printf("1. Find Set (Representative)\n");
        printf("2. Union Sets\n");
        printf("3. Display Parent Array\n");
        printf("4. Display Joined Sets\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter element: ");
                scanf("%d", &x);
                printf("Representative of %d is %d\n", x, find(x));
                break;

            case 2:
                printf("Enter two elements to union: ");
                scanf("%d %d", &x, &y);
                unionSet(x, y);
                break;

            case 3:
                displayParentArray();
                break;

            case 4:
                displayJoinedSets();
                break;

            case 5:
                printf("Exiting program...\n");
                break;

            default:
                printf("Invalid choice! Try again.\n");
        }
    } while (choice != 5);

    return 0;
}
