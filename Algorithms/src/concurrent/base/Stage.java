package concurrent.base;

/**
 * project_name:Algorithms
 * package_name:concurrent.base
 * user: youzipi
 * date: 2015/4/6
 */
public class Stage extends Thread {
    @Override
    public void run() {
        ArmyRunnable armyTaskOfSui = new ArmyRunnable();
        ArmyRunnable armyTaskOfRevolt = new ArmyRunnable();
        Thread armyOfSui = new Thread(armyTaskOfSui, "Sui");
        Thread armyOfRevolt = new Thread(armyTaskOfRevolt, "Revolt");

        armyOfSui.start();
        armyOfRevolt.start();

        try {
            Thread.sleep(50);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }



        System.out.println("A KeyPerson appeard");

        Thread hero = new KeyPersonThread();
        hero.setName("Hero");

        armyTaskOfSui.keepRunning = false;
        armyTaskOfRevolt.keepRunning = false;

        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        hero.start();
        try {
            hero.join();//hero执行完，其他才会去执行
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("The battle finished");
        System.out.println("FINISHED");

//        try {
//            armyOfRevolt.join();
//        } catch (InterruptedException e) {
//            e.printStackTrace();
//        }
    }

    public static void main(String[] args) {
        new Stage().start();
    }
}
