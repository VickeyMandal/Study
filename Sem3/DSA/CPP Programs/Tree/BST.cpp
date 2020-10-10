#include <iostream>
#include <cstdlib>
using namespace std;

struct node
{
    int info;
    struct node *left;
    struct node *right;
}*root,*par;


node *find(int item){
	node *ptr, *save;
	if(root==NULL)
    { 
    	par=NULL;
        return NULL;
    }
    else if(item==root->info)
	{
		par=NULL;
		return root;
		}
	else if(item<root->info)
	{
		ptr=root->left;
		save=root;
	}	
	else{
		ptr=root->right;
		save=root;
	}
	
	while(ptr!=NULL){
		if(item==ptr->info){
			par=save;
			return ptr;
		}
		else if(item<ptr->info){
			save=ptr;
			ptr=ptr->left;
		}
		else{
			save=ptr;
			ptr=ptr->right;
		}
	}
	par=save;
	return NULL;
}

void insert(int item)
{
    node* loc =find(item);
    if(loc!=NULL)
    {
    	return;
	}
	node *t=new node;
	t->info=item;
	t->left=NULL;
	t->right=NULL;
	if(par==NULL)
	{
		root=t;
	}
	else if(item<par->info)
	{
		par->left=t;
	}
	else {
		par->right=t;
	}
}

void preorder(node *r){
	if(r!=NULL)
	{
		cout<<r->info;
		preorder(r->left);
		preorder(r->right);
	}
}
void postorder(node *r){
	if(r!=NULL)
	{	
		preorder(r->left);
		preorder(r->right);
		cout<<r->info;
	}
}

void inorder(node *r){
	if(r!=NULL)
	{	
		preorder(r->left);
		cout<<r->info;
		preorder(r->right);
		
	}
}

int main(){
	insert(2);
	insert(7);
	insert(3);
	insert(1);
	preorder(root);
	cout<<"\n";
	postorder(root);
	cout<<"\n";
	inorder(root);
	
}
