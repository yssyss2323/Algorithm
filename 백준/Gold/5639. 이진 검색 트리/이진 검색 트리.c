#include <stdio.h>
#include <stdlib.h>
#define MAX 10000

typedef struct TreeNode {
    int key;
    struct TreeNode* left;
    struct TreeNode* right;
} TreeNode;

TreeNode* create_node(int key);
TreeNode* insert_node(TreeNode* root, int key);
void postorder(TreeNode* root);

int main() {
    int arr[MAX];
    int tmp;
    int cnt = 0;
    while (scanf("%d", &tmp) != EOF) {
        arr[cnt++] = tmp;
    }

    TreeNode* root = NULL;
    for (int i = 0; i < cnt; i++) {
        root = insert_node(root, arr[i]);
    }

    postorder(root);

    return 0;

}

TreeNode* create_node(int key) {
    TreeNode* node = malloc(sizeof(TreeNode));
    node->key = key;
    node->left = NULL;
    node->right = NULL;
    return node;
}

TreeNode* insert_node(TreeNode* root, int key) {
    if (root == NULL) {
        TreeNode* node = create_node(key);
        return node;
    }
    if (root->key < key) {
        root->right = insert_node(root->right, key);
    }
    else if (root->key > key) {
        root->left = insert_node(root->left, key);
    }
    return root;
}

void postorder(TreeNode* root) {
    if (root != NULL) {
        postorder(root->left);
        postorder(root->right);
        printf("%d\n", root->key);    
    }
}