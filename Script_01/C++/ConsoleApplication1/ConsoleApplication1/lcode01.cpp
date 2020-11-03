//#include<iostream>
//#include<vector>
//using namespace std;
//
//class solution {
//public:
//	//int removeDuplicates(vector<int>& nums) {
//	//	if (nums.empty()) return 0;
//	//	int index = 0;
//	//	for (int i = 1; i < nums.size(); i++) {
//	//		if (nums[index] != nums[i]) {
//	//			index++;
//	//			nums[index] = nums[i];
//	//		}
//	//	}
//	//	return index + 1;
//	//	//删除数组中相邻元素中相同的元素
//	//	//1、index = 0
//	//	//2、i = 1
//	//	//3、if(nums[index] != nums[i])
//	//	//4、index ++
//	//	//5、nums[index] = nums[i]
//	//	//6、return index + 1
//	//}
//	/*int removeDuplicates(vector<int>& nums) {
//		if (nums.size() <= 2) return nums.size();
//		int index = 2;
//		for (int i = 2; i < nums.size(); i++) {
//			if (nums[i] != nums[index - 2]) {
//				nums[index] = nums[i];
//				index++;
//			}
//		}
//		return index;
//	}*/
//	int search(const vector<int>& nums, int target) {
//		int first = 0, last = nums.size();
//		while (first != last) {
//			const int mid = first + (last - first) / 2;
//			if(nums[mid] == target){
//				return mid;
//			}
//			if (nums[first] <= nums[mid]) {
//				if (nums[first] <= target && target < nums[mid]) {
//					last = mid;
//				}
//				else {
//					first = mid + 1;
//				}
//			}
//			else {
//				if (nums[mid] < target && target <= nums[last - 1]) {
//					first = mid + 1;
//				}
//				else {
//					last = mid;
//				}
//			}
//			
//		}
//		return -1;
//	}
//
//};
//
//int main() {
//	vector<int> a = {1,2,3,4,5,6,7,8,9,10};
//	solution so = solution();
//	int b = so.search(a, 4);
//	cout << b << endl;
//	
//	return 0;
//}