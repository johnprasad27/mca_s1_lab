#include <stdio.h>
#define INF 9999

int main() {
    int n;
    printf("Enter number of vertices: ");
    scanf("%d", &n);

    int cost[n][n];

    printf("\nEnter the cost between vertices\n");
    printf("(Enter 0 if there is no edge)\n\n");

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            if(i == j) {
                cost[i][j] = INF;
            } else {
                printf("Cost from %d to %d: ", i, j);
                scanf("%d", &cost[i][j]);

                if(cost[i][j] == 0)
                    cost[i][j] = INF;
            }
        }
    }

    int visited[n];
    for(int i = 0; i < n; i++)
        visited[i] = 0;

    visited[0] = 1;   // start from vertex 0

    int edge_count = 0;
    int total_cost = 0;

    printf("\nEdge Selection Table:\n");
    printf("Edge\tWeight\n");

    while(edge_count < n - 1) {
        int min = INF;
        int u = -1, v = -1;

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

    printf("\nTotal cost of MST = %d\n", total_cost);

    return 0;
}
