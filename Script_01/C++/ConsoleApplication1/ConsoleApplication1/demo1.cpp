//#include<iostream>
//using namespace std;
//
//class Begin {
//private:
//	float speed = 1;
//	float timer = 5;
//	float begintime = 0;
//	bool isIn = false;
//	bool hasShoe = false;
//	int numberOfshoe = 0;
//public:
//	Begin(float speed, float timer) {
//		this->timer = timer;
//		this->speed = speed;
//	}
//	Begin() {}
//	bool isEmpty() {
//		return hasShoe;
//	}
//	bool isWantPushShoe() {
//		cout << "������Ҫ��Ь����" << endl;
//		cout << "Ҫ�Ļ�������1" << endl;
//		int a;
//		cin >> a;
//		if (a == 1) {
//			cout << "�ɹ�����һ˫Ь��" << endl;
//			this->hasShoe = true;
//			this->numberOfshoe++;
//			this->start();
//		}
//		else {
//			cout << "��������" << endl;
//		}
//	}
//	void start() {
//		if (!this->isEmpty() && !this->isIn) {
//			cout << "�������Ь�ӣ���ʼ����" << endl;
//			while (this->begintime < this->timer) {
//				this->running();
//				this->begintime++;
//			}
//			if (this->begintime == this->timer) {
//				cout << "Ь�ӷ���ɹ�" << endl;
//				this->begintime = 0;
//				this->hasShoe = false;
//				this->isIn = true;
//			}
//		}
//		if (this->isEmpty() && this->isIn) {
//			cout << "Ь���Ѿ������ɣ�����׼���Ѱ����˳���" << endl;
//			while (this->begintime < this->timer) {
//				this->running();
//				this->begintime++;
//			}
//			if (this->begintime == this->timer) {
//				cout << "�����Ƴ���ϣ����ڵȴ���һ˫Ь��" << endl;
//				this->begintime = 0;
//				this->hasShoe = false;
//				this->isIn = false;
//			}
//		}
//	}
//	void running() {
//		cout << "��������ת��" << endl;
//	}
//
//};
//
//int main() {
//	Begin begin = Begin();
//	begin.isWantPushShoe();
//	return 0;
//}