#include <stdio.h>
#define MAX 10

int queue[MAX];
int front = -1, rear = -1;

/* Enqueue operation */
void enqueue(int value) {
    if (rear == MAX - 1) {
        printf("Queue Overflow! Cannot insert.\n");
        return;
    }

    if (front == -1)
        front = 0;

    queue[++rear] = value;
    printf("%d inserted into queue.\n", value);
}

/* Dequeue operation */
void dequeue() {
    if (front == -1 || front > rear) {
        printf("Queue Underflow! Queue is empty.\n");
        return;
    }

    printf("%d removed from queue.\n", queue[front++]);

    if (front > rear)
        front = rear = -1;
}

/* Peek operation */
void peek() {
    if (front == -1) {
        printf("Queue is empty.\n");
        return;
    }
    printf("Front element is %d\n", queue[front]);
}

/* Display queue */
void display() {
    if (front == -1) {
        printf("Queue is empty.\n");
        return;
    }

    printf("Queue elements:\n");
    for (int i = front; i <= rear; i++)
        printf("%d ", queue[i]);
    printf("\n");
}

/* MAIN */
int main() {
    int choice, value;

    do {
        printf("\n--- QUEUE MENU (Array) ---\n");
        printf("1. Enqueue\n");
        printf("2. Dequeue\n");
        printf("3. Peek\n");
        printf("4. Display\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter value to insert: ");
                scanf("%d", &value);
                enqueue(value);
                break;

            case 2:
                dequeue();
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
