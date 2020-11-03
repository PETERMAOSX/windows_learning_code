//#include<iostream>
//#include<stdlib.h>
//#include<vector>
//#include<algorithm>
//using namespace std;
//
//int Find_K(int a[], int low, int high, int k) {
//	if (k <= 0) {
//		return -1;
//	}
//	if (k > high - low + 1) {
//		return -1;
//	}
//	int pivot = low + rand() % (high - low + 1);
//	swap(a[low], a[pivot]);
//	int m = low;
//	int count = -1;
//	for (int i = low + 1; i <= high; i++) {
//		if (a[i] > a[low]) {
//			swap(a[++m], a[i]);
//			count++;
//		}
//	}
//	swap(a[m], a[low]);
//	if (count > k) {
//		return Find_K(a, low, m - 1, k);
//	}
//	else if (count < k) {
//		return Find_K(a, m + 1, high, k - count);
//	}
//	else {
//		return m;
//	}
//}
//
//void FindMinTopK(vector<int>& vec, int k) {
//	vector<int> heap(vec.begin(), vec.begin() + k);
//	make_heap(heap.begin(), heap.end());
//	int i;
//	for (i = k; i < vec.size(); i++) {
//		if (vec[i] < heap[0]) {
//			pop_heap(heap.begin(), heap.end());
//			heap.pop_back();
//			heap.push_back(vec[i]);
//			push_heap(heap.begin(), heap.end()); 
//		}
//	}
//	for (i = 0; i < heap.size(); i++) {
//		cout << heap[i] << endl;
//	}
//}
//
//
//int main() {
//
//	return 0;
//}