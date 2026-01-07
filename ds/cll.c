#include<stdio.h>
#include<stdlib.h>

typedef struct node{
    int data;
    struct node* next;
}node;

node* createNode(int value){
    node* newnode=(node*)malloc(sizeof(node));
    
}

