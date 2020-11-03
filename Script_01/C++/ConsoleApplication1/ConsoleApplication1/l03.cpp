//#include<iostream>
//#include<vector>
//#include<unordered_map>
//using namespace std;
//class Solution {
//public:
//	vector<int> twosum(vector<int>& nums, int target) {
//		unordered_map<int, int> mp;
//		for (int i = 0; i < nums.size(); i++) {
//			mp[nums[i]] = i;
//		}
//		vector<int> result;
//		for (int i = 0; i < nums.size(); i++) {
//			const int gap = target - nums[i];
//			if (mp.find(gap) != mp.end()) {
//				result.push_back(i+1);
//				result.push_back(mp[gap] + 1);
//				break;
//			}
//		}
//		return result;
//	}
//};
//int main() {
//	vector<int> vec;
//	vec = { 2,7,11,15 };
//	Solution so = Solution();
//	vector<int> a = so.twosum(vec, 9);
//	for (auto i : a) {
//		cout << i << " ";
//	}
//	cout << endl;
//
//	return 0;
//}