package concurrent;

/**
 * project_name:Algorithms
 * package_name:concurrent
 * user: youzipi
 * date: 2015/4/7
 */

public class ThreadDemo {

    public static void main(String[] args) {
        Apple n = new Apple();

        Thread a1 = new Thread(new Producer(n), "Producer");
        Thread a2 = new Thread(new Consumer(n), "Consumer");

        a1.start();
//        try{
//            Thread.sleep(1000) ;
//        }catch(InterruptedException e){
//            e.printStackTrace() ;
//        }
        a2.start();
    }

}

class Producer implements Runnable {
    Apple n;

    public Producer(Apple n) {
        this.n = n;
    }

    volatile boolean keepRunning = true;

    @Override
    public void run() {
        while (true) {
            while (keepRunning) {
                if (n.getCount() < 5) {
                    n.produce();

                }
                if (n.getCount() >= 5) {
                    keepRunning = false;
                }
                Thread.yield();
            }
            if (n.getCount() < 5) {
                keepRunning = true;

            }
        }

    }
}

class Consumer implements Runnable {
    Apple n;

    public Consumer(Apple n) {
        this.n = n;
    }

    volatile boolean keepRunning = true;

    @Override
    public void run() {
        while (true) {
            while (keepRunning) {
                if (n.getCount() <= 5 && n.getCount() > 0) {
                    n.consume();
                    System.out.println(n.getType());
                }
                if (n.getCount() <= 0) {
                    keepRunning = false;
                }

                Thread.yield();
            }
            if (n.getCount() > 0) {
                keepRunning = true;
            }
        }

    }

}

class Apple {
    private int count = 0;
    private int type = 1;

    public int getType() {
        return type;
    }

    public synchronized int getCount() {
        return count;
    }

    public synchronized void produce() {
        count++;
        System.out.println(Thread.currentThread().getName()
                + " produced an apple，" + getCount() + " apple(s) left");
    }

    public synchronized void consume() {
        count--;//here is 4
        System.out.println(Thread.currentThread().getName()
                + " consumed an apple," + getCount() + " apple(s) left");////here is 5
    }

}

