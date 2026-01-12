#include <stdio.h>
#define MAX 10

int stack[MAX];
int top = -1;

/* Push operation */
void push(int value) {
    if (top == MAX - 1) {
        printf("Stack Overflow! Cannot push.\n");
        return;
    }
    stack[++top] = value;
    printf("%d pushed into stack.\n", value);
}

/* Pop operation */
void pop() {
    if (top == -1) {
        printf("Stack Underflow! Cannot pop.\n");
        return;
    }
    printf("%d popped from stack.\n", stack[top--]);
}

/* Peek operation */
void peek() {
    if (top == -1) {
        printf("Stack is empty.\n");
        return;
    }
    printf("Top element is %d\n", stack[top]);
}

/* Display stack */
void display() {
    if (top == -1) {
        printf("Stack is empty.\n");
        return;
    }

    printf("Stack elements:\n");
    for (int i = top; i >= 0; i--)
        printf("%d\n", stack[i]);
}

/* MAIN */
int main() {
    int choice, value;

    do {
        printf("\n--- STACK MENU ---\n");
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. Peek\n");
        printf("4. Display\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter value to push: ");
                scanf("%d", &value);
                push(value);
                break;

            case 2:
                pop();
                break;

            case 3:
                peek();
                break;

            case 4:
                display();
                break;

            case 5:
                printf("Exiting program...\n");
                break;

            default:
                printf("Invalid choice!\n");
        }
    } while (choice != 5);

    return 0;
}
