#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *prev;
    struct node *next;
};

struct node *head = NULL;

/* Create new node */
struct node* createNode(int value) {
    struct node* newNode = (struct node*)malloc(sizeof(struct node));
    newNode->data = value;
    newNode->prev = NULL;
    newNode->next = NULL;
    return newNode;
}

/* Insert at beginning */
void insertBegin(int value) {
    struct node* newNode = createNode(value);

    if (head != NULL) {
        head->prev = newNode;
        newNode->next = head;
    }
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
    newNode->prev = temp;
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
    newNode->prev = temp;

    if (temp->next != NULL)
        temp->next->prev = newNode;

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

    if (head != NULL)
        head->prev = NULL;

    free(temp);
}

/* Delete from end */
void deleteEnd() {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }

    struct node* temp = head;
    while (temp->next != NULL)
        temp = temp->next;

    if (temp->prev != NULL)
        temp->prev->next = NULL;
    else
        head = NULL;

    free(temp);
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
    for (int i = 1; i < pos && temp != NULL; i++)
        temp = temp->next;

    if (temp == NULL) {
        printf("Invalid position\n");
        return;
    }

    temp->prev->next = temp->next;

    if (temp->next != NULL)
        temp->next->prev = temp->prev;

    free(temp);
}

/* Display forward */
void displayForward() {
    struct node* temp = head;
    if (temp == NULL) {
        printf("List is empty\n");
        return;
    }

    printf("Forward: ");
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

/* Display backward */
void displayBackward() {
    struct node* temp = head;
    if (temp == NULL) {
        printf("List is empty\n");
        return;
    }

    while (temp->next != NULL)
        temp = temp->next;

    printf("Backward: ");
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->prev;
    }
    printf("\n");
}

/* MAIN */
int main() {
    int choice, value, pos;

    do {
        printf("\n--- DOUBLY LINKED LIST MENU ---\n");
        printf("1. Insert at Beginning\n");
        printf("2. Insert at End\n");
        printf("3. Insert at Any Position\n");
        printf("4. Delete from Beginning\n");
        printf("5. Delete from End\n");
        printf("6. Delete at Any Position\n");
        printf("7. Display Forward\n");
        printf("8. Display Backward\n");
        printf("9. Exit\n");
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
                displayForward();
                break;

            case 8:
                displayBackward();
                break;

            case 9:
                printf("Exiting program...\n");
                break;

            default:
                printf("Invalid choice!\n");
        }
    } while (choice != 9);

    return 0;
}
