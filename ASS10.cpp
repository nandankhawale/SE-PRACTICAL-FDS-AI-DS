#include <iostream>
#include <cctype>
#include <string>

using namespace std;

class Stack
{
private:
    char *data;
    int top;
    int capacity;

public:
    Stack(int size)
    {
        data = new char[size];
        top = -1;
        capacity = size;
    }
    ~Stack()
    {
        delete[] data;
    }
    void push(char element)
    {
        if (top < capacity - 1)
        {
            data[++top] = element;
        }
        else
        {
            cout << "Stack Overflow" << endl;
        }
    }
    char pop()
    {
        if (top >= 0)
        {
            return data[top--];
        }
        else
        {
            cout << "Stack Underflow" << endl;
            return '\0'; // Return null character for simplicity
        }
    }
    char peek()
    {
        if (top >= 0)
        {
            return data[top];
        }
        else
        {
            cout << "Stack is empty" << endl;
            return '\0'; // Return null character for simplicity
        }
    }
    bool isEmpty()
    {
        return (top == -1);
    }
};
bool isOperator(char c)
{
    return (c == '+' || c == '-' || c == '*' || c == '/');
}
int getPrecedence(char c)
{
    if (c == '+' || c == '-')
        return 1;
    else if (c == '*' || c == '/')
        return 2;
    return 0;
}
string infixToPostfix(const string &infix)
{
    string postfix = "";
    Stack operators(100);
    for (char c : infix)
    {
        if (isalnum(c))
        {
            postfix += c;
        }
        else if (c == '(')
        {
            operators.push(c);
        }
        else if (c == ')')
        {
            while (!operators.isEmpty() && operators.peek() != '(')
            {
                postfix += operators.pop();
            }
            operators.pop(); // Pop '(' from the stack
        }
        else if (isOperator(c))
        {
            while (!operators.isEmpty() && getPrecedence(operators.peek()) >= getPrecedence(c))
            {
                postfix += operators.pop();
            }
            operators.push(c);
        }
    }
    while (!operators.isEmpty())
    {
        postfix += operators.pop();
    }

    return postfix;
}
int main() {
    string infixExpression;
    cout << "Enter infix expression: ";
    cin >> infixExpression;

    string postfixExpression = infixToPostfix(infixExpression);
    cout << "Postfix expression: " << postfixExpression << endl;

    return 0;
}
