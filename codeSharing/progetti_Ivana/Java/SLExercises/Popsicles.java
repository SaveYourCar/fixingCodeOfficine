import java.util.Scanner;

public class Popsicles
{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int siblings = input.nextInt();
        int popsicles = input.nextInt();
        
        if( popsicles % siblings == 0)
        {  
        giveAway();
        }
        else
        {
        eatThem();
        }
        
        input.close();
    }
    
    static void giveAway() {
        System.out.println("give away");
    }

    static void eatThem() {
        System.out.println("eat them yourself");
    } 
}



