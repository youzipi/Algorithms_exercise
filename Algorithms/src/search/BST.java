package search;

/**
 * project_name:Algorithms
 * package_name:search
 * user: youzipi
 * date: 2015/4/17
 */
public class BST<Key extends Comparable<Key>, Value> {

    private Node root;

    private class Node {
        private Key key;
        private Value value;
        private Node left, right;
        private int N;//以该节点为根的树的节点总数（含该节点）

        public Node(Key key, Value value, int n) {
            this.key = key;
            this.value = value;
            N = n;
        }
    }

    public Value get(Key key) {
        return get(root,key);
    }

    private Value get(Node x,Key key) {
        Value value = null;
        if(x == null){
            return null;
        }
        int cmp = key.compareTo(x.key);
        if (cmp < 0) {
            value = get(x.left, key);//递归更新子树

        } else if (cmp > 0) {
            value = get(x.right, key);//递归更新子树
        } else if (cmp == 0) {
            value = x.value;
        }
        return value;
    }


    public void put(Key key, Value value) {
        root = put(root, key, value);//从root节点开始更新树

    }

    public Node put(Node x, Key key, Value value) {

        if (x == null) {
            return new Node(key, value, 1);//1:当前树中只有一个节点，该节点本身
        }

        int cmp = key.compareTo(x.key);
        if (cmp < 0) {
            x.left = put(x.left, key, value);//递归更新子树

        } else if (cmp > 0) {
            x.right = put(x.right, key, value);//递归更新子树
        } else if (cmp == 0) {
            x.value = value;    //更新值
        }
        x.N = size(x.left) + size(x.right) + 1;
        return x;
    }

    private int size(Node x) {
        if (x == null)
            return 0;
        else            //else要不要
            return x.N;
    }

    public void print() {
        print(root);
    }

    public void print(Node x) {
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


    public static void main(String[] args) {
        BST<Integer, Integer> tree = new BST<Integer, Integer>();
        Integer[] list = {1, 6, 7, 8, 5, 4, 3};
        for (Integer i : list) {
            tree.put(i, i*i);
        }
        tree.print();
        System.out.println(tree.get(5));

    }
}
