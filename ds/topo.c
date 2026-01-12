#include<stdio.h>

int main(){
    int n;
    printf("enter the number of vertices:");
    scanf("%d",&n);

    int adj[n][n];
    printf("Enter the adjacency matrix:");
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            scanf("%d",&adj[i][j]);
        }
    }

    int indegree[n];

    for(int i=0;i<n;i++){
        indegree[i]=0;
    }

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(adj[i][j]==1)
                indegree[j]++;
        }
    }

    int queue[n],front=0,rear=0;
    // Push all vertices with indegree 0
    for(int i=0;i<n;i++){
        if (indegree[i] == 0)
            queue[rear++] = i;
    }

    int topo[n],k=0;

    while(front<rear){
        int u =queue[front++];
        topo[k++]=u;

        for(int v=0;v<n;v++){
            if(adj[u][v]==1){
                indegree[v]--;
                if(indegree[v]==0)
                    queue[rear++]=v;
            }
        }
    }

    if (k != n) {
        printf("\nCycle detected! Topological sort not possible.\n");
        return 0;
    }
   
     printf("\nTopological order (Kahn): ");
    for (int i = 0; i < n; i++)
        printf("%d ", topo[i]);

    return 0;
}