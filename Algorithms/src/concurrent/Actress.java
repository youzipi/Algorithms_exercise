package concurrent;

/**
 * project_name:Algorithms
 * package_name:concurrent
 * user: youzipi
 * date: 2015/4/6
 */
public class Actress implements Runnable {
    @Override
    public void run() {
        System.out.println(Thread.currentThread().getName()+" is an actress");
        int count = 0;
        boolean keepRunning = true;
        while(keepRunning){
            System.out.println(Thread.currentThread().getName()+" is on the stage "+count);
            count++;
            if((count%10) == 0){
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            if(count >= 100){
                keepRunning = false;
            }
        }
        System.out.println(Thread.currentThread().getName()+" fnished");
    }
}
