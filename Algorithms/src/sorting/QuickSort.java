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
        sort(a, 0, a.length - 1);
    }

    public static void sort(Comparable[] a, int left, int right) {

        if (right <= left)
            return;
        Random random = new Random();
        int mid = random.nextInt(right);
        int r = right;
        int l = left;

        exch(a, 0, mid);
        Comparable flag = a[0];
        l++;
        while (true) {
            while (lessorEqual(a[l], flag)) {
                l++;
                if (l == right)
                    break;
            }
            while (lessorEqual(flag, a[r])) {
                r--;
                if (r == 0)
                    break;
            }
            if (l >= r)
                break;
            else
                exch(a, l, r);
        }
        exch(a, r, 0);
        sort(a, 0, l - 1);
        sort(a, l+1, right);
    }

    public static void main(String[] args) {
        Integer[] a = new Integer[]{2,6,8,9,3,5,4,7,0};
        show(a);
        QuickSort.sort(a);
        show(a);
    }
}
