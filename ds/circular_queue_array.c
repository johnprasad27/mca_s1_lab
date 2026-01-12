#include <stdio.h>
#define MAX 5

int cq[MAX];
int front = -1, rear = -1;

/* Enqueue operation */
void enqueue(int value) {
    if ((front == (rear + 1) % MAX)) {
        printf("Queue Overflow! Circular Queue is full.\n");
        return;
    }

    if (front == -1) {   // first insertion
        front = rear = 0;
    } else {
        rear = (rear + 1) % MAX;
    }

    cq[rear] = value;
    printf("%d inserted into queue.\n", value);
}

/* Dequeue operation */
void dequeue() {
    if (front == -1) {
        printf("Queue Underflow! Circular Queue is empty.\n");
        return;
    }

    printf("%d removed from queue.\n", cq[front]);

    if (front == rear) {
        // queue becomes empty
        front = rear = -1;
    } else {
        front = (front + 1) % MAX;
    }
}

/* Peek operation */
void peek() {
    if (front == -1) {
        printf("Queue is empty.\n");
        return;
    }
    printf("Front element is %d\n", cq[front]);
}

/* Display queue */
void display() {
    if (front == -1) {
        printf("Queue is empty.\n");
        return;
    }

    printf("Queue elements: ");
    int i = front;

    while (1) {
        printf("%d ", cq[i]);
        if (i == rear)
            break;
        i = (i + 1) % MAX;
    }
    printf("\n");
}

/* MAIN */
int main() {
    int choice, value;

    do {
        printf("\n--- CIRCULAR QUEUE MENU ---\n");
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
