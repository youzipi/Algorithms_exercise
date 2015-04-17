package sorting;

import java.util.Random;

/**
 * project_name:Algorithms
 * package_name:common
 * user: youzipi
 * date: 2015/4/6
 */
public class QuickSort extends Sort {
    public static void sort(Comparable[] a) {
        int left = 0;
        int right = a.length;
        if (right <= left)
            return;
        Random random = new Random();
        int p = random.nextInt(right);

        exch(a, 0, p);
        int last = left;

        for (int i = left+1; i <= right; i++) {
            if(less(a[left],a[right])){
                exch(a,last,i);
                last++;
            }
        }
        exch(a,left,right);
//        sort(a[left:last-1]);



    }

    public static void main(String[] args) {
        Integer[] a = new Integer[]{1, 4, 5, 6, 2, 5, 3};
        QuickSort.sort(a);
        show(a);
    }
}
