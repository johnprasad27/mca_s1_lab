#include <stdio.h>
#define INF 9999

int main() {
    int n;
    printf("Enter number of vertices: ");
    scanf("%d", &n);

    int cost[n][n];
    printf("Enter cost adjacency matrix (0 if no edge):\n");

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            scanf("%d", &cost[i][j]);
            if(cost[i][j] == 0)
                cost[i][j] = INF;
        }
    }

    int parent[n];
    for(int i = 0; i < n; i++)
        parent[i] = i;

    int edges = 0, total = 0;

    printf("\nEdges in MST:\n");

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
            printf("%d - %d  weight: %d\n", u, v, min);
            total += min;

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

    printf("\nTotal cost of MST = %d\n", total);
    return 0;
}
