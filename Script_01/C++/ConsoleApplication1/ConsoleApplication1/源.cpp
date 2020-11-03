//#include<iostream>
//using namespace std;
//int Average(int a, int b) {
//	return (a + b) / 2;
//}
//float Sum(int n) {
//	float sum = 1.0;
//	for (int i = 1; i <= n; i++) {
//		sum += 1.0 / (i * (i + 1));
//	}
//	return sum;
//}
//float Sum_Pro(int n) {
//	return 2 - 1.0 / (n + 1);
//}
//void build() {
//	int i, V[26];
//	V[0] = 'a';
//	for (int i = 1; i <= 25; i++) {
//		V[i] = V[i - 1] + 1;
//	}
//	for (char i : V) {
//		cout << i << endl;
//	}
//}
////typedef struct card {
////	int num;
////	char name[20];
////	char author[10];
////	char publisher[30];
////	float price;
////}DATATYPE;
//typedef int ElemType;
//#define LIST_INIT_SIZE 1000
//typedef struct {
//	ElemType* elem;
//	int length;
//	int listsize;
//}SqList;
//int InitList_Sq(SqList* L, int ms) {
//	int size = ms * sizeof(ElemType);
//	L->elem = (ElemType*)malloc(size);
//	L->length = 0;
//	L->listsize = ms;
//	return 1;
//}
//int main() {
//	/*int* p1, * p2, a[3] = { 0,4,5 };
//	p1 = a;
//	p2 = &a[2];
//	cout << "p1: " << *p1 << endl;
//	cout << "p2: " << *p2 << endl;
//	cout << p2 - p1 << endl;
//	int ans = p2 - p1;
//	cout << ans << endl;*/
//	/*int* s;
//	s = (int*)malloc(sizeof(int));
//	free(s);*/
//	/*
//	c++中 malloc是申请空间使用的
//	free是清空空间使用的
//	*/
//	//cout << Average(20000, 30000) << endl;
//	/*cout << Sum(2) << endl;
//	cout << Sum_Pro(2) << endl;*/
//	/*build();*/
//	return 0;
//}