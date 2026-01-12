#include <stdio.h>
#include <stdlib.h>

struct node {
    char data;
    struct node *next;
};

struct node *head = NULL;

/* Insert character at end */
void insertChar(char ch) {
    struct node *newNode = (struct node *)malloc(sizeof(struct node));
    newNode->data = ch;
    newNode->next = NULL;

    if (head == NULL) {
        head = newNode;
        return;
    }

    struct node *temp = head;
    while (temp->next != NULL)
        temp = temp->next;

    temp->next = newNode;
}

/* Print linked list in reverse (WITHOUT reversing) */
void printReverse(struct node *temp) {
    if (temp == NULL)
        return;

    printReverse(temp->next);
    printf("%c", temp->data);
}

/* Display original list */
void display() {
    struct node *temp = head;
    while (temp != NULL) {
        printf("%c", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

int main() {
    char name[50];

    printf("Enter your name: ");
    scanf("%s", name);

    /* Store each character in linked list */
    for (int i = 0; name[i] != '\0'; i++) {
        insertChar(name[i]);
    }

    printf("Original name: ");
    display();

    printf("Reversed name: ");
    printReverse(head);
    printf("\n");

    return 0;
}
