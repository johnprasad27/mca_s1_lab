#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};

struct node *head = NULL;

/* Create new node */
struct node* createNode(int value) {
    struct node* newNode = (struct node*)malloc(sizeof(struct node));
    newNode->data = value;
    newNode->next = NULL;
    return newNode;
}

/* Insert at beginning */
void insertBegin(int value) {
    struct node* newNode = createNode(value);
    newNode->next = head;
    head = newNode;
}

/* Insert at end */
void insertEnd(int value) {
    struct node* newNode = createNode(value);

    if (head == NULL) {
        head = newNode;
        return;
    }

    struct node* temp = head;
    while (temp->next != NULL)
        temp = temp->next;

    temp->next = newNode;
}

/* Insert at any position */
void insertAtPosition(int value, int pos) {
    if (pos == 1) {
        insertBegin(value);
        return;
    }

    struct node* temp = head;
    for (int i = 1; i < pos - 1 && temp != NULL; i++)
        temp = temp->next;

    if (temp == NULL) {
        printf("Invalid position\n");
        return;
    }

    struct node* newNode = createNode(value);
    newNode->next = temp->next;
    temp->next = newNode;
}

/* Delete from beginning */
void deleteBegin() {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }

    struct node* temp = head;
    head = head->next;
    free(temp);
}

/* Delete from end */
void deleteEnd() {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }

    if (head->next == NULL) {
        free(head);
        head = NULL;
        return;
    }

    struct node* temp = head;
    while (temp->next->next != NULL)
        temp = temp->next;

    free(temp->next);
    temp->next = NULL;
}

/* Delete at any position */
void deleteAtPosition(int pos) {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }

    if (pos == 1) {
        deleteBegin();
        return;
    }

    struct node* temp = head;
    for (int i = 1; i < pos - 1 && temp->next != NULL; i++)
        temp = temp->next;

    if (temp->next == NULL) {
        printf("Invalid position\n");
        return;
    }

    struct node* del = temp->next;
    temp->next = del->next;
    free(del);
}

/* Display list */
void display() {
    struct node* temp = head;

    if (temp == NULL) {
        printf("List is empty\n");
        return;
    }

    printf("Linked List: ");
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

/* MAIN */
int main() {
    int choice, value, pos;

    do {
        printf("\n--- SINGLY LINKED LIST MENU ---\n");
        printf("1. Insert at Beginning\n");
        printf("2. Insert at End\n");
        printf("3. Insert at Any Position\n");
        printf("4. Delete from Beginning\n");
        printf("5. Delete from End\n");
        printf("6. Delete at Any Position\n");
        printf("7. Display\n");
        printf("8. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter value: ");
                scanf("%d", &value);
                insertBegin(value);
                break;

            case 2:
                printf("Enter value: ");
                scanf("%d", &value);
                insertEnd(value);
                break;

            case 3:
                printf("Enter value and position: ");
                scanf("%d %d", &value, &pos);
                insertAtPosition(value, pos);
                break;

            case 4:
                deleteBegin();
                break;

            case 5:
                deleteEnd();
                break;

            case 6:
                printf("Enter position: ");
                scanf("%d", &pos);
                deleteAtPosition(pos);
                break;

            case 7:
                display();
                break;

            case 8:
                printf("Exiting program...\n");
                break;

            default:
                printf("Invalid choice!\n");
        }
    } while (choice != 8);

    return 0;
}
