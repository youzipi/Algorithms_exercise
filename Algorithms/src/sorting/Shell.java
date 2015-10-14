package sorting;

/**
 * project_name:Algorithms
 * package_name:PACKAGE_NAME
 * user: youzipi
 * date: 2015/3/16
 */
public class Shell extends Sort{
    public static void sort(Comparable[] a){
        int N = a.length;
        int h = N/3+1;
        while (h >= 1){
            for(int i = h;i < N;i++){
                for(int j = i;j >= h && less(a[j],a[j-h]);j -= h){
                    exch(a,i,i-h);
                }
            }
            h = h/3;
        }
    }

    public static void main(String[] args) {
        Integer[] a = new Integer[]{1,4,5,6,2,5,3};
        Shell.sort(a);
        show(a);

    }
}
