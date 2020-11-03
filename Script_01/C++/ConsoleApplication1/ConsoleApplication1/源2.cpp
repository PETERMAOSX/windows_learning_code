//#include<iostream>
//using namespace std;
//
//class MyQueue {
//private:
//	int *m_pQueue;
//	int m_iQueueCapacity;
//	int m_iQueueLen;
//	int m_iHead;
//	int m_iTail;
//public:
//	MyQueue(int capacity) {
//		this->m_iQueueCapacity = capacity;
//		this->m_iHead = 0;
//		this->m_iTail = 0;
//		this->m_iQueueLen = 0;
//		this->m_pQueue = new int[this->m_iQueueCapacity];
//	}
//	~MyQueue() {
//		delete[] m_pQueue;
//		this->m_pQueue = NULL;
//	}
//	void ClearQueue() {
//		this->m_iHead = 0;
//		this->m_iTail = 0;
//		this->m_iQueueLen = 0;
//	}
//	bool isEmpty() {
//		return this->m_iQueueLen == 0;
//	}
//	bool isFull() {
//		return this->m_iQueueLen = this->m_iQueueCapacity;
//	}
//	int getLength() {
//		return this->m_iQueueLen;
//	}
//	bool EnQueue(int element) {
//		if (this->isFull()) {
//			cout << "Queue is Full" << endl;
//			return false;
//		}
//		else {
//			this->m_pQueue[this->m_iTail++] = element;
//			this->m_iTail = this->m_iTail % this->m_iQueueCapacity;
//			this->m_iQueueLen++;
//			return true;
//		}
//	}
//	int DeQueue() {
//		int temp = -1;
//		if (this->isEmpty()) {
//			cout << "Queue is Empty" << endl;
//			return temp;
//		}
//		else {
//			temp = this->m_pQueue[this->m_iHead--];
//			this->m_iHead = this->m_iHead % this->m_iQueueCapacity;
//			this->m_iQueueLen--;
//			return temp;
//		}
//	}
//	void show() {
//		for (int i = this->m_iHead; i < this->m_iQueueCapacity + this->m_iHead; i++) {
//			cout << this->m_pQueue[i % this->m_iQueueCapacity] << endl;
//		}
//	}
//};
//
//int main() {
//	MyQueue* queue = new MyQueue(4);
//	queue->EnQueue(4);
//	queue->EnQueue(6);
//	queue->EnQueue(8);
//	queue->EnQueue(10);
//	queue->show();
//	system("pause");
//	return 0;
//}