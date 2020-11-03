#include<iostream>
using namespace std;

struct node {
	int data;
	struct node* next;
};

int main() {
	struct node* head, * q, * p,*temp;
	head = NULL;
	int i, n, t;
	cin >> n;
	for (i = 1; i <= n; i++) {
		cin >> t;
		p = (struct node*)malloc(sizeof(struct node));
		p->data = t;
		p->next = NULL;
		if (head == NULL) {
			head = p;
		}
		else {
			q->next = p;
		}
		q = p;
	}
	temp = head;
	while (temp != NULL) {
		cout << temp->data << " ";
		temp = temp->next;
	}
	cout << endl;
	return 0;
}