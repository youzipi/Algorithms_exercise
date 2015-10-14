package sorting;

/**
 * project_name:Algorithms
 * package_name:sorting
 * user: youzipi
 * date: 2015/3/16
 */
public abstract class Sort {

    protected static boolean less(Comparable a,Comparable b){
        return a.compareTo(b) < 0;
    }

    protected static boolean lessorEqual(Comparable a,Comparable b){
        return a.compareTo(b) <= 0;
    }

    // exchange a[i] and a[j]
    protected static void exch(Object[] a, int i, int j) {
        Object swap = a[i];
        a[i] = a[j];
        a[j] = swap;
    }

    // print array to standard output
    protected static void show(Comparable[] a) {
        for (Comparable anA : a) {
            System.out.print(anA + ",");
        }
        System.out.println();
    }
}
