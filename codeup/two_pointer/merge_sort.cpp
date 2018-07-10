#include <iostream>
#include <vector>
using namespace std;

int n, m;

// [L1, R1]
void merge(vector<int> &A, int L1, int R1, int L2, int R2) {
    int i = L1;
    int j = L2;
    vector<int> tmp;
    while (i <= R1 && j <= R2) {
        if (A[i] <= A[j]) {
            tmp.push_back(A[i]);
            i++;
        } else {
            tmp.push_back(A[j]);
            j++;
        }
    }
    while (i <= R1) {
        tmp.push_back(A[i]);
        i++;
    }
    while (j <= R2) {
        tmp.push_back(A[j]);
        j++;
    }
    for (int i = 0; i < tmp.size(); i++) {
        A[L1 + i] = tmp[i];
    }
}

void merge_sort(vector<int> &A, int left, int right) {
    if (left < right) {
        int mid = (left + right) / 2;
        merge_sort(A, left, mid);
        merge_sort(A, mid + 1, right);
        merge(A, left, mid, mid + 1, right);
    }

}

int main() {
    scanf("%d", &n);
    for (int v = 0; v < n; v++) {
        scanf("%d", &m);
        vector<int> info;
        info.resize(m);
        for (int i = 0; i < m; i++) {
            scanf("%d", &info[i]);
        }
        merge_sort(info, 0, info.size() - 1);
        for (int i = 0; i < info.size(); i++) {
            printf("%d\n", info[i]);
        }
    }
    return 0;
}