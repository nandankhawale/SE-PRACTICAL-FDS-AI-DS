#include <iostream>
using namespace std;
class PizzaParlor
{
private:
    int front;
    int rear;
    int *queue;
    int capacity;

public:
    PizzaParlor(int capacity) : capacity(capacity)
    {
        queue = new int[capacity]{}; // Initialize with zeros
        front = 0;
        rear = 0;
    }
    ~PizzaParlor()
    {
        delete[] queue; // Deallocate dynamic array in the destructor
    }

    void enqueue(int order)
    {
        if (isFull())
        {
            cout << "Queue is full, cannot add new order" << endl;
            return;
        }

        queue[rear] = order;
        rear = (rear + 1) % capacity;
    }
    int dequeue()
    {
        if (isEmpty())
        {
            cout << "Queue is empty, cannot remove order" << endl;
            return -1;
        }

        int order = queue[front];
        front = (front + 1) % capacity;
        return order;
    }
    bool isFull()
    {
        return ((rear + 1) % capacity == front);
    }

    bool isEmpty()
    {
        return (front == rear);
    }
    void displayQueue()
    {
        cout << "Queue: [";
        if (!isEmpty())
        {
            int i = front;
            do
            {
                cout << queue[i] << ", ";
                i = (i + 1) % capacity;
            } while (i != front);
        }
        cout << "]" << endl;
    }
};
int main() {
    int capacity;
    cout << "Enter the capacity for the PizzaParlor: ";
    cin >> capacity;
    PizzaParlor parlor(capacity);
     int order;
    while (1) {
        cout << "Enter order (0 to exit): ";
        cin >> order;


        if (order == 0) {
            break;
        }

        parlor.enqueue(order);
        parlor.displayQueue();
        cout<<"YOUR ORDER HAS BEEN TAKEN"<<endl;
    }
    
    cout << "Serving orders..." << endl;
    while (!parlor.isEmpty()) {
        cout << "Serving order: " << parlor.dequeue() << endl;
    }

    return 0;
}

