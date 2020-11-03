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
//		cout << "请问你要放鞋子吗？" << endl;
//		cout << "要的话请输入1" << endl;
//		int a;
//		cin >> a;
//		if (a == 1) {
//			cout << "成功放上一双鞋子" << endl;
//			this->hasShoe = true;
//			this->numberOfshoe++;
//			this->start();
//		}
//		else {
//			cout << "输入有误" << endl;
//		}
//	}
//	void start() {
//		if (!this->isEmpty() && !this->isIn) {
//			cout << "上面放了鞋子，开始启动" << endl;
//			while (this->begintime < this->timer) {
//				this->running();
//				this->begintime++;
//			}
//			if (this->begintime == this->timer) {
//				cout << "鞋子放入成功" << endl;
//				this->begintime = 0;
//				this->hasShoe = false;
//				this->isIn = true;
//			}
//		}
//		if (this->isEmpty() && this->isIn) {
//			cout << "鞋子已经入库完成，正在准备把板子退出来" << endl;
//			while (this->begintime < this->timer) {
//				this->running();
//				this->begintime++;
//			}
//			if (this->begintime == this->timer) {
//				cout << "板子推出完毕，正在等待下一双鞋子" << endl;
//				this->begintime = 0;
//				this->hasShoe = false;
//				this->isIn = false;
//			}
//		}
//	}
//	void running() {
//		cout << "轮子正在转动" << endl;
//	}
//
//};
//
//int main() {
//	Begin begin = Begin();
//	begin.isWantPushShoe();
//	return 0;
//}