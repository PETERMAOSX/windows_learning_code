//#include<iostream>
//#include<vector>
//#include<algorithm>
//using namespace std;
//
////¶ş·Ö²éÕÒ
//int binary_serach(int * arr,int n,int key) {
//	int low = 0;
//	int high = n - 1;
//	int mid;
//	if (high < low) {
//		return -1;
//	}
//	while (high >= low) {
//		//mid = low + ((high - low) >> 1);
//		mid = (low + high) >>1;
//		if (arr[mid] == key) {
//			return mid;
//		}
//		else if (arr[mid] > key) {
//			high = mid - 1;
//		}
//		else
//			low = mid + 1;
//	}
//	return -1;
//}
//
//int main() {
//	int arr[] = { 1,2,3,4,5,6,7,8,9 };
//	cout << binary_serach(arr, 9, 3) << endl;
//	return 0;
//}