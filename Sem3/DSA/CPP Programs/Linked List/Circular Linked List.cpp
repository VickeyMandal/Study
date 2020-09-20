#include<iostream>
using namespace std;

struct node{
	int data;
	struct node *next;
};
struct node *head;

//--------------------------------------------------------------------------//

void insertAfter(int d, int item)
{
	struct node *t = new node;
	t->data=d;
	node *p = head;
	if(head==NULL){
		cout<<"List is empty!";
		delete t;
	}
	else
	{
				
		do{
			if(item==p->data)
			{
				t->next=p->next;
				p->next=t;
				return;	
			}
			else
			{
				p=p->next;
			}	
		}while(p!=head);
			
			
	}
	
}

//--------------------------------------------------------------------------//


void insertBefore(int d, int item)
{
	struct node *t = new node;
	t->data=d;
	node *p = head;
	if(head==NULL){
		cout<<"List is empty!";
		delete t;
	}
	else
	{
				
		do{
			if(item==p->next->data)
			{
				t->next=p->next;
				p->next=t;
				return;	
			}
			else
			{
				p=p->next;
			}	
		}while(p!=head);
			
			
	}
	
}

//--------------------------------------------------------------------------//

void insertBegin(int d)
{
	struct node *t = new node;
	t->data=d;
	if(head==NULL)
	{
		head=t;
		t->next=t;
	}
	else
	{
		node *p=head;
		while(p!=head)
		{
			p=p->next;
		}
		
		p->next=t;
		t->next=head;
		head=t;
		
	}
	
}

//--------------------------------------------------------------------------//

void insertLast(int d)
{
	struct node *t = new node;
	t->data=d;
	if(head==NULL)
	{
		head=t;
		t->next=t;
	}
	else
	{
		node *p=head;
		while(p->next!=head)
		{
			p=p->next;
		}
		p->next=t;
		t->next=head;
	}
		
}

//--------------------------------------------------------------------------//

void display()
{
	if(head==NULL)
	{
		cout<<"Empty";
	}
	else
	{
		node *p=head;
		cout<<"List contains : ";
		do
		{
		cout<<p->data<<"\t";
		p=p->next;	
		} while(p!=head);
		
	}
}


int main()
{
	insertBegin(4);
	insertBegin(7);
	insertLast(9);
	insertLast(8);
	insertAfter(3,8);
	insertBefore(5,8);
	display();
}















