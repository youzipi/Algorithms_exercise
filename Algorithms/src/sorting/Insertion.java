package sorting;

/**
 * project_name:Algorithms
 * package_name:sorting
 * user: youzipi
 * date: 2015/3/16
 */
public class Insertion extends Sort{
    public static void sort(Comparable[] a){
        int N = a.length;

            for(int i = 0;i < N;i++){
                for(int j = i;j >0 && less(a[j],a[j-1]);j--){
                    exch(a,i,i-1);
                }
            }
    }

    public static void main(String[] args) {
        Integer[] a = new Integer[]{1,4,5,6,2,5,3};
        Insertion.sort(a);
        show(a);

    }
}
