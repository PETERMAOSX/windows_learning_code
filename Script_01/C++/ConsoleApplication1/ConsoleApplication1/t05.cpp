//#include<iostream>
//#include<vector>
//#include<list>
//#include<map>
//#include<set>
//#include<algorithm>
//using namespace std;
//
//int main() {
//	vector<int> vec;
//	list<int> lst;
//	map<int, int> mp;
//	set<int> st;
//	for (int i = 0; i < 10; i++) {
//		vec.push_back(i);
//		lst.push_back(i);
//		mp.insert(make_pair(i, i));
//		st.insert(i);
//	}
//	cout << "Vector: " << endl;
//	vector<int>::const_iterator iterVec(vec.begin());
//	while (iterVec != vec.end()) {
//		cout << *iterVec << endl;
//		iterVec++;
//	}
//	cout << "\nlist: " << endl;
//	list<int> ::const_iterator iterList(lst.begin());
//	while (iterList != lst.end()) {
//		cout << *iterList << endl;
//		iterList++;
//	}
//	cout << "\nmap: " << endl;
//	map<int, int>::const_iterator iterMap(mp.begin());
//	while (iterMap != mp.end()) {
//		cout << "Key = " << iterMap->first
//			<< "Value = " << iterMap->second
//			<< endl;
//		iterMap++;
//	}
//	cout << "\nset: " << endl;
//	set<int> ::const_iterator iterSet(st.begin());
//	while (iterSet != st.end()) {
//		cout << *iterSet << endl;
//		iterSet++;
//	}
//
//	return 0;
//}