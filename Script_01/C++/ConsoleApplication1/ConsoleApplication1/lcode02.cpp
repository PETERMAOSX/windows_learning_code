//#include<iostream>
//#include<vector>
//#include<map>
//#include<unordered_map>
//#include <algorithm>
//using namespace std;
//
//class Solution {
//public:
//	int longestConsecutive(const vector<int>& nums) {
//		unordered_map<int, bool> used;
//		for (auto i : nums) used[i] = false;
//		int maxlength = 0;
//		for (auto i : nums) {
//			if (used[i]) continue;
//			int length = 1;
//			for (int j = i + 1; used.find(j) != used.end(); j++) {
//				used[i] = true;
//				++length;
//			}
//			for (int j = i - 1; used.find(j) != used.end(); j--) {
//				used[i] = true;
//				++length;
//			}
//			maxlength = max(length, maxlength);
//		}
//		return maxlength;
//	}
//};
//
//int main() {
//	/*vector<int> vec = { 100,4,200,1,3,2 };
//	Solution so = Solution();
//	int length = so.longestConsecutive(vec);
//	cout << length << endl;*/
//	unordered_map<int, bool> mp;
//	mp[1] = false;
//	mp[2] = false;
//	mp[10] = false;
//	cout << (bool)(mp.find(10) != mp.end()) << endl;
//	return 0;
//}