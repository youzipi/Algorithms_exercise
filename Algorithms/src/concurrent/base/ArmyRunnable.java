package concurrent.base;

/**
 * project_name:Algorithms
 * package_name:concurrent.base
 * user: youzipi
 * date: 2015/4/6
 */
public class ArmyRunnable implements Runnable {
    volatile boolean keepRunning = true;//

    @Override
    public void run() {
        while (keepRunning){
            for (int i = 0; i < 5; i++) {
                System.out.println(Thread.currentThread().getName()+" attack "+i);
                Thread.yield();//让出处理器时间
            }
        }
        System.out.println(Thread.currentThread().getName()+" finished");
    }
}
