//#include<iostream>
//#include<vector>
//#include<string>
//#include<algorithm>
//#include<utility>
//using namespace std;
//
//int main() {
//	vector<string> vec;
//	vec.push_back("one");
//	vec.push_back("three");
//	vec.push_back("right");
//	auto iter = vec.insert(++vec.begin(), "two");
//	string more[] = { "five","six","seven" };
//	auto iter1 = vec.insert(--end(vec), begin(more), end(more));
//	auto iter2 = vec.insert(end(vec), "ten");
//	auto iter3 = vec.insert(end(vec)-1,2, "nine");  //��vec end��ǰ���������nine
//	auto iter4 = vec.insert(end(vec), { {"twelve"},{"thirteen"} });
//	vec[9] = "ele";
//	vec.pop_back();  //ɾ��β����Ԫ�أ���python��pop()һ��
//	swap(vec[0], vec[vec.size()-1]);
//	vec.pop_back();
//	for (int i = 0; i < vec.size(); i++) {
//		cout << vec[i] << " ";
//	}
//	cout << vec.size();
//	cout << endl;
//	return 0;
//}