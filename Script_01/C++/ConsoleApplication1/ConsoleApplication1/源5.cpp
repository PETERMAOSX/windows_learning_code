//#include<iostream>
//#include<vector>
//using namespace std;
//
//typedef struct list_node ListNode;
//struct list_node {
//	struct list_node* next;
//	int value;
//};
///*
//≥ı ºªØList 
//*/
//void Init_List(ListNode*& head, int* array, int n) {
//	head = NULL;
//	ListNode* temp;
//	ListNode* record;
//	for (int i = 1; i <= n; i++) {
//		temp = new ListNode;
//		temp->next = NULL;
//		temp->value = array[i - 1];
//		if (head == NULL) {
//			head = temp;
//			record = head;
//		}
//		else {
//			record->next = temp;
//			record = temp;
//		}
//	}
//}
//
//void print_list(ListNode* list) {
//	ListNode* tmp = list;
//	while (tmp != NULL) {
//		cout << tmp->value << endl;
//		tmp = tmp->next;
//	}
//}
//
//
//int main() {
//
//	return 0;
//}