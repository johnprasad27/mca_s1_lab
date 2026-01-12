#include <stdio.h>

int n;
int adj[20][20];
int visited[20];

/* ---------- DFS (Recursive) ---------- */
void dfs(int v) {
    visited[v] = 1;
    printf("%d ", v);

    for(int i = 0; i < n; i++) {
        if(adj[v][i] == 1 && visited[i] == 0) {
            dfs(i);
        }
    }
}

/* ---------- BFS ---------- */
void bfs(int start) {
    int queue[20], front = 0, rear = 0;

    for(int i = 0; i < n; i++)
        visited[i] = 0;

    visited[start] = 1;
    queue[rear++] = start;

    printf("%d ", start);

    while(front < rear) {
        int u = queue[front++];

        for(int v = 0; v < n; v++) {
            if(adj[u][v] == 1 && visited[v] == 0) {
                visited[v] = 1;
                printf("%d ", v);
                queue[rear++] = v;
            }
        }
    }
}

int main() {
    int choice, start;

    printf("Enter number of vertices: ");
    scanf("%d", &n);

    printf("Enter adjacency matrix (0 or 1):\n");
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            scanf("%d", &adj[i][j]);
        }
    }

    do {
        printf("\n--- MENU ---\n");
        printf("1. DFS\n");
        printf("2. BFS\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch(choice) {
            case 1:
                for(int i = 0; i < n; i++)
                    visited[i] = 0;

                printf("Enter starting vertex for DFS: ");
                scanf("%d", &start);

                printf("DFS Traversal: ");
                dfs(start);
                printf("\n");
                break;

            case 2:
                printf("Enter starting vertex for BFS: ");
                scanf("%d", &start);

                printf("BFS Traversal: ");
                bfs(start);
                printf("\n");
                break;

            case 3:
                printf("Exiting program...\n");
                break;

            default:
                printf("Invalid choice! Try again.\n");
        }
    } while(choice != 3);

    return 0;
}
