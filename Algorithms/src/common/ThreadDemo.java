package common;

import java.util.concurrent.locks.Lock;

/**
 * project_name:Algorithms
 * package_name:concurrent
 * user: youzipi
 * date: 2015/4/7
 */

public class ThreadDemo {

    public static void main(String[] args) {
        Apple n = new Apple();
        Object obj = new Object();

        // 使用Runnable接口创建线程
        Thread a1 = new Thread(new Producer(obj, n), "Producer");
        Thread a2 = new Thread(new Consumer(obj, n), "Consumer");
//        Producer p = new Producer(obj,n);
//        Consumer c = new Consumer(obj,n);
//        System.out.println(p.flag);
//        System.out.println(c.flag);
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
    Object flag;

    public Producer(Object flag, Apple n) {
        this.flag = flag;
        this.n = n;
    }


    volatile boolean keepRunning = true;

    @Override
    public void run() {
        while (true) {
            while (keepRunning) {
                synchronized (lock.getL()) {
                    if (n.getCount() < 5) {
                        n.addMub();
                        System.out.println(Thread.currentThread().getName()
                                + "增加了一个苹果，现在有" + n.getCount() + "个苹果");
                    }
                    if (n.getCount() >= 5) {
                        keepRunning = false;
                    }
                    Thread.yield();

                }
            }
            if (n.getCount() < 5) {
                keepRunning = true;
            }
        }

    }
}

class Consumer implements Runnable {
    Apple n;
    Object flag;


    public Consumer(Object flag, Apple n) {
        this.flag = flag;
        this.n = n;
    }

    volatile boolean keepRunning = true;

    @Override
    public void run() {
        while (true) {
            while (keepRunning) {
                synchronized (lock.getL()) {
                    if (n.getCount() <= 5 && n.getCount() > 0) {
                        n.CMub();
                        System.out.println(Thread.currentThread().getName()
                                + "拿了一个苹果，现在有" + n.getCount() + "个苹果");
                    }
                    if (n.getCount() <= 0) {
                        keepRunning = false;
                    }
                }
                // 让出了处理器时间
                Thread.yield();
            }
            if (n.getCount() > 0) {
                keepRunning = true;
            }
        }
    }
}


class lock {
    static Object l = new Object();
    public static Object getL() {
        return l;
    }
}

class Apple {
    private int count = 0;
    Object flag = new Object();
    public int getCount() {
        return count;
    }
    public void addMub() {
        this.count++;
    }

    public void CMub() {
        this.count--;
    }

}

