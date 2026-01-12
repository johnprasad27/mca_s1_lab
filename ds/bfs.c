#include <stdio.h>

int main() {
    int n;
    printf("Enter number of vertices: ");
    scanf("%d", &n);

    int adj[n][n];
    printf("Enter adjacency matrix (0 or 1):\n");

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            scanf("%d", &adj[i][j]);
        }
    }

    int visited[n];
    for(int i = 0; i < n; i++)
        visited[i] = 0;

    int queue[n], front = 0, rear = 0;

    int start;
    printf("Enter starting vertex: ");
    scanf("%d", &start);

    visited[start] = 1;
    queue[rear++] = start;

    printf("\nBFS Traversal: ");

    while(front < rear) {
        int u = queue[front++];
        printf("%d ", u);

        for(int v = 0; v < n; v++) {
            if(adj[u][v] == 1 && visited[v] == 0) {
                visited[v] = 1;
                queue[rear++] = v;
            }
        }
    }

    return 0;
}
