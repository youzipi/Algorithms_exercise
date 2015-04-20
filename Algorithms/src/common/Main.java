package common;

import java.util.Scanner;

/**
 * project_name:Algorithms
 * package_name:common
 * user: youzipi
 * date: 2015/4/19
 */
public class Main {



    public static void main(String[] args) {
        Main mainObj = new Main();
        Scanner in = new Scanner(System.in);
        int t;
        t = in.nextInt();
        for(int i = 0;i < t;i++){
            mainObj.cal();
        }
    }



    int value(char c){
        int temp_sum;
        if((c >='A') && ('Z' >= c)){
            temp_sum = (c - 'A'+1);
        }
        else{
            temp_sum = c-'a'+1;
        }
//        System.out.println(temp_sum);
        return temp_sum;
    }
    void cal(){
        Scanner s = new Scanner(System.in);
        String string;
        string = s.next();

        int l=string.length();
        int k=0,sum=0;
        char temp = string.charAt(0);
        k = init_k(temp);


        for(int i=1;i<l;i++){
            char c = string.charAt(i);
            if((c == temp)){
                k += init_k(c);
            }
            else if((c-'A') == (temp-'a')){
//                System.out.println("double");
                k = k+2;
            }
            else {
                sum += k*k*value(temp);
                temp=c;
                k=init_k(temp);
            }
        }
        sum += k*k*value(temp);
        System.out.println(sum);
    }

    int init_k(char temp) {
        int k;
        if((temp >='A') && ('Z' >= temp)){
            k=2;
        }
        else {
            k=1;
        }
        return k;
    }
}
