package concurrent;

/**
 * project_name:Algorithms
 * package_name:concurrent
 * user: youzipi
 * date: 2015/4/6
 */
public class Actor extends Thread {
    @Override
    public void run() {
        System.out.println(getName()+" is an actor");
        int count = 0;
        boolean keepRunning = true;
        while(keepRunning){
            System.out.println(getName()+" is on the stage "+count);
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
        System.out.println(getName()+" fnished");
    }

    public static void main(String[] args) {
        Thread actor = new Actor();
        Thread actress = new Thread(new Actress(),"Mrs. Runnable");
        actor.setName("Mr. Thread");
        actor.start();
        actress.start();
    }
}

