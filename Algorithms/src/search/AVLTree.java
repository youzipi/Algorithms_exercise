package search;

/**
 * project_name:Algorithms
 * package_name:search
 * user: youzipi
 * date: 2015/4/20
 */
public class AVLTree<Key extends Comparable<Key>, Value> extends BST {

    private Node root;

    private class Node {
        protected Key key;        //key为排序依据
        protected Value value;
        protected Node left, right;
        protected int N;//以该节点为根的树的节点总数（含该节点）
        protected int height;

        public Node(Key key, Value value, int n,int height) {
            this.key = key;
            this.value = value;
            this.N = n;
            this.height = height;
        }
    }

    public int height() {
//        return root.height;
        return height(root);
    }
    public int height(Node x) {
        if (x == null)
            return 0;
        else            //else要不要
            return x.height;
    }

    private boolean checkBalance(Node x){
        int balance = x.right.height - x.left.height;
        if((balance <= 1) && (balance >= -1))
            return true;
        return false;
    }

    private Node rightRotate(Node x){
        Node n = x.right;
        x.right = n.left;
        n.left = x;

        x.height = max(height(x.left), height(x.right))+1;
        n.height = max(height(n.left), height(n.right))+1;
        return n;//x -> x.right.left
    }

    private Node leftRotate(Node x){
        Node n = x.left;
        x.left = n.right;
        n.right = x;

        x.height = max(height(x.left), height(x.right))+1;
        n.height = max(height(n.left), height(n.right))+1;
        return n;
    }

    private Node leftRightRotate(Node x){
        x.left = leftRotate(x.left);
        return rightRotate(x);
    }

    private Node rightLeftRotate(Node x){
        x.right = rightRotate(x.right);
        return leftRotate(x);
    }

    private void put(Key key, Value value) {
        root = put(root, key, value);//从root节点开始更新树

    }

    public Node put(Node x, Key key, Value value) {

        if (x == null) {
            return new Node(key, value, 1,1);//1:当前树中只有一个节点，该节点本身
        }

        int cmp = key.compareTo(x.key);
        if (cmp < 0) {
            x.left = put(x.left, key, value);//递归更新子树
            int balance = height(x.left) - height(x.right);
            if(balance == 2){
                x = leftRotate(x);
            }
            else if (balance == -2){
                x = rightLeftRotate(x);
            }

        } else if (cmp > 0) {
            x.right = put(x.right, key, value);//递归更新子树
            int balance = height(x.left) - height(x.right);
            if(balance == 2){
                x = leftRightRotate(x);
            }
            else if (balance == -2){
                x = rightRotate(x);
            }
        } else if (cmp == 0) {
            x.value = value;    //更新值
        }
        x.N = size(x.left) + size(x.right) + 1;

        x.height = max(height(x.left), height(x.right))+1;

        return x;
    }

    private int max(int a,int b){
        return a>=b?a:b;
    }

    private int size(Node x) {
        if (x == null)
            return 0;
        else            //else要不要
            return x.N;
    }

    private void print() {
        print(root);
    }

    private void print(Node x) {
        if (x == null) {
            return;
        }
        if (x.left != null) {
            System.out.println(x.value + "->" + x.left.value);
        }
        if (x.right != null) {
            System.out.println(x.value + "->" + x.right.value);
        }
        print(x.left);
        print(x.right);

    }

    private void printKey(Node x) {
        if (x == null) {
            return;
        }
        if (x.left != null) {
            System.out.println(x.key + "->" + x.left.key);
        }
        if (x.right != null) {
            System.out.println(x.key + "->" + x.right.key);
        }
        print(x.left);
        print(x.right);

    }


    public static void main(String[] args) {
        AVLTree<Integer, Integer> tree = new AVLTree<Integer, Integer>();
        Integer[] list = {1, 6, 8, 9, 5, 4, 3};
        for (Integer i : list) {
            tree.put(i, i * i);
            System.out.println("add"+i);
            tree.print();
        }
        System.out.println(tree.get(5));
        tree.put(7, 49);
        tree.print();
        System.out.println("height=" + tree.height());



    }

}
