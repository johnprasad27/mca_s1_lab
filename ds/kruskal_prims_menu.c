#include <stdio.h>
#define INF 9999

/* ---------- PRIM'S ALGORITHM ---------- */
void prims(int n, int cost[20][20]) {
    int visited[20] = {0};
    int edge_count = 0, total_cost = 0;

    visited[0] = 1;   // start from vertex 0

    printf("\nPrim's MST (Edge Selection Table):\n");
    printf("Edge\tWeight\n");

    while(edge_count < n - 1) {
        int min = INF, u = -1, v = -1;

        for(int i = 0; i < n; i++) {
            if(visited[i]) {
                for(int j = 0; j < n; j++) {
                    if(!visited[j] && cost[i][j] < min) {
                        min = cost[i][j];
                        u = i;
                        v = j;
                    }
                }
            }
        }

        printf("%d - %d\t%d\n", u, v, min);
        total_cost += min;
        visited[v] = 1;
        edge_count++;
    }

    printf("Total cost of MST = %d\n", total_cost);
}

/* ---------- KRUSKAL'S ALGORITHM ---------- */
void kruskal(int n, int cost[20][20]) {
    int parent[20];
    for(int i = 0; i < n; i++)
        parent[i] = i;

    int edges = 0, total_cost = 0;

    printf("\nKruskal's MST:\n");
    printf("Edge\tWeight\n");

    while(edges < n - 1) {
        int min = INF, u = -1, v = -1;

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(cost[i][j] < min) {
                    min = cost[i][j];
                    u = i;
                    v = j;
                }
            }
        }

        if(parent[u] != parent[v]) {
            printf("%d - %d\t%d\n", u, v, min);
            total_cost += min;

            int old = parent[v];
            int new = parent[u];
            for(int i = 0; i < n; i++) {
                if(parent[i] == old)
                    parent[i] = new;
            }

            edges++;
        }

        cost[u][v] = cost[v][u] = INF;
    }

    printf("Total cost of MST = %d\n", total_cost);
}

/* ---------- MAIN MENU ---------- */
int main() {
    int n, choice;
    int cost[20][20];

    printf("Enter number of vertices: ");
    scanf("%d", &n);

    printf("\nEnter cost adjacency matrix (0 if no edge):\n");
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            scanf("%d", &cost[i][j]);
            if(cost[i][j] == 0)
                cost[i][j] = INF;
        }
    }

    do {
        printf("\n--- MENU ---\n");
        printf("1. Prim's Algorithm\n");
        printf("2. Kruskal's Algorithm\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch(choice) {
            case 1:
                prims(n, cost);
                break;

            case 2:
                kruskal(n, cost);
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
