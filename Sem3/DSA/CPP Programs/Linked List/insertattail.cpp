#include <bits/stdc++.h>
using namespace std;
struct node{
	int data;
	struct node *next;
};

struct node *head;

void insertNodeAtTail(int d)
{
	struct node *t;
	t->data=d;
	t->next=NULL;
	if(head==NULL)
	{
		head=t;
	}
	else
	{
		struct node *p=head;
		while(p->next!=NULL)
		{
			p=p->next;
		}
		p->next=t;
		
	}
}

void display()
{
	
}
