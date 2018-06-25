#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int a = 0, b = 0, c = 0, sum = 0;
        ListNode *rst = NULL, *p, *q;
        int f1 = 1, f2 = 1;
        while (1) {
            if (l1 == NULL) {
                a = 0;
                f1 = 0;
            } else {
                a = l1->val;
                l1 = l1->next;
            }

            if (l2 == NULL) {
                b = 0;
                f2 = 0;
            } else { 
                b = l2->val;
                l2 = l2->next;
            }
            if (f1 == 0 && f2 == 0 && c == 0) {
                break;
            }

            sum = a + b + c;
            c = sum / 10;

            q = (ListNode *) malloc(sizeof(ListNode));
            q->val = sum % 10;
            q->next = NULL;
            if (rst == NULL) {
                rst = q;
                p = q;
            } else {
                p->next = q;
                p = q;
            } 
        }
        return rst;
    }
};

int main() {
    return 0;
}