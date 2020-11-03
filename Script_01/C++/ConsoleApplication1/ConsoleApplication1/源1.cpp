//#include<iostream>
//using namespace std;
//class MyQueue {
//public:
//	MyQueue(int queueCapacity); //initQueue(&Q) 创建队列
//	virtual ~MyQueue();   //销毁
//	void ClearQueue();	//清空
//	bool QueueEmpty() const;   //判空
// 	int QueueLength() const;  //得到长度
//	bool QueueFull() const;
//	bool EnQueue(int element); //新元素入队
//	bool DeQueue(int& element); //首元素出队
//	void QueueTraverse(); //遍历队列
//private:
//	int* m_pQueue;  //队列数组指针
//	int m_iQueueLen;  //队列元素个数
//	int m_iQueueCapacity;   //队列数组容量
//	int m_iHead;
//	int m_iTail;
//};
//MyQueue::MyQueue(int queueCapacity) {
//	this->m_iQueueCapacity = queueCapacity;
//	this->m_iHead = 0;
//	this->m_iTail = 0;
//	this->m_pQueue = new int[this->m_iQueueCapacity];
//	this->m_iQueueLen = 0;
//}
//MyQueue::~MyQueue() {
//	delete[] this->m_pQueue;
//	this->m_pQueue = NULL;
//}
//void MyQueue::ClearQueue() {
//	this->m_iHead = 0;
//	this->m_iTail = 0;
//	this->m_iQueueLen = 0;
//}
//bool MyQueue::QueueEmpty() const {
//	return this->m_iQueueLen == 0;
//}
//
//int MyQueue::QueueLength()const {
//	return this->m_iQueueLen;
//}
//bool MyQueue::QueueFull() const {
//	return this->m_iQueueCapacity == this->m_iQueueLen;
//}
//bool MyQueue::EnQueue(int element) {
//	if (this->QueueFull()) {
//		return false;
//	}
//	else {
//		this->m_pQueue[m_iTail] = element;
//		this->m_iTail++;
//		this->m_iTail = m_iTail % m_iQueueCapacity;
//		this->m_iQueueLen++;
//		return true; //插入已经完成
//	}
//}
//bool MyQueue::DeQueue(int& element) {
//	if (this->QueueEmpty()) {
//		cout << "Queue is Empty" << endl;
//		return false;
//	}
//	element = m_pQueue[m_iHead];
//	m_iHead++;
//	this->m_iHead = this->m_iHead % this->m_iQueueCapacity;
//	this->m_iQueueLen--;
//	return true;
//}
//void MyQueue::QueueTraverse() {
//	for (int i = this->m_iHead; i < this->m_iQueueLen + m_iHead; i++) {
//		cout << m_pQueue[i % m_iQueueLen] << endl;
//	}
//}
//
//int main() {
//	MyQueue* p = new MyQueue(4);
//	p->EnQueue(10);
//	p->EnQueue(12);
//	p->EnQueue(14);
//	p->EnQueue(18);
//	int e = 0;
//	p->QueueTraverse();
//	p->DeQueue(e);
//	cout << e << endl;
//	delete p;
//	system("pause");
//	return 0;
//}