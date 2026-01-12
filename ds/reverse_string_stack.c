#include <stdio.h>
#include <string.h>
#define MAX 50

char stack[MAX];
int top = -1;

/* Push character into stack */
void push(char ch) {
    stack[++top] = ch;
}

/* Pop character from stack */
char pop() {
    return stack[top--];
}

int main() {
    char name[MAX];
    int i, len;

    printf("Enter your name: ");
    scanf("%s", name);

    len = strlen(name);

    /* Push each character into stack */
    for (i = 0; i < len; i++) {
        push(name[i]);
    }

    printf("Reversed name: ");

    /* Pop and print */
    while (top != -1) {
        printf("%c", pop());
    }

    printf("\n");
    return 0;
}
