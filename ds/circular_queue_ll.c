#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};

struct node *front = NULL;
struct node *rear = NULL;

/* Enqueue operation */
void enqueue(int value) {
    struct node *newNode = (struct node *)malloc(sizeof(struct node));

    if (newNode == NULL) {
        printf("Heap Overflow! Memory not allocated.\n");
        return;
    }

    newNode->data = value;

    if (front == NULL) {
        // First node
        front = rear = newNode;
        newNode->next = front;
    } else {
        rear->next = newNode;
        rear = newNode;
        rear->next = front;
    }

    printf("%d inserted into circular queue.\n", value);
}

/* Dequeue operation */
void dequeue() {
    if (front == NULL) {
        printf("Queue Underflow! Circular queue is empty.\n");
        return;
    }

    // Only one node
    if (front == rear) {
        printf("%d removed from queue.\n", front->data);
        free(front);
        front = rear = NULL;
    } else {
        struct node *temp = front;
        printf("%d removed from queue.\n", temp->data);
        front = front->next;
        rear->next = front;
        free(temp);
    }
}

/* Peek operation */
void peek() {
    if (front == NULL) {
        printf("Queue is empty.\n");
        return;
    }
    printf("Front element is %d\n", front->data);
}

/* Display queue */
void display() {
    if (front == NULL) {
        printf("Queue is empty.\n");
        return;
    }

    struct node *temp = front;
    printf("Circular Queue elements: ");

    do {
        printf("%d ", temp->data);
        temp = temp->next;
    } while (temp != front);

    printf("\n");
}

/* MAIN */
int main() {
    int choice, value;

    do {
        printf("\n--- CIRCULAR QUEUE MENU (Linked List) ---\n");
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
