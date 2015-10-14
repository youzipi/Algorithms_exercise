package concurrent.base;

/**
 * project_name:Algorithms
 * package_name:concurrent.base
 * user: youzipi
 * date: 2015/4/6
 */
public class KeyPersonThread extends Thread {
    @Override
    public void run() {
        System.out.println(getName()+" start");

        for (int i = 0; i < 10; i++) {
            System.out.println(getName()+" attack "+i);
        }
        System.out.println(getName()+" finished");
    }
}
